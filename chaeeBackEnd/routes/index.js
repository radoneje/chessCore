const express = require('express');
const router = express.Router();
const moment = require('moment');

const capitalizeFirstLetter = (string) => {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

/* GET home page. */
router.get('/', async  (req, res, next)=> {
  let devices=await req.knex("t_devices").orderBy("id", "desc")
  res.render('index', { title: 'chess', devices });
});

router.get('/api/currPosition/:deviceId', async  (req, res, next)=> {
  let position=(await req.knex("t_devicePosition").where({deviceId:req.params.deviceId}).orderBy("id", "desc").limit(1))[0]
  
  let figurePosition=await req.knex("v_figurePosition").where({devicePositionId:position.id})
  res.json({figurePosition, date:moment(position.date).format("DD.MM.YYYY HH:mm:ss")})
});


router.post('/api/chess/:deviceSN', async (req, res, next) => {
  try {
    let devices=await req.knex("t_devices").where({sn:req.params.deviceSN})
    if(devices.length==0)
      devices=await req.knex("t_devices").insert({sn:req.params.deviceSN, title:req.params.deviceSN},"*")
    let deviceId=devices[0].id;
    let devicePosition = (await req.knex("t_devicePosition").insert({
      date: new Date(req.body.time * 1000),
      deviceId: deviceId
    }, "*"))[0]
    for (let field of req.body.board) {
      let fieldName = Object.keys(field)[0]
      let figure = field[fieldName];
      if (figure.role && figure.color) {
        figure.title = capitalizeFirstLetter(figure.color) + " " + capitalizeFirstLetter(figure.role)
        let item = await req.knex("t_figure").where({ title: figure.title })
        if (item.length == 0) {
          item = await req.knex("t_figure").insert({
            title: figure.title,
            color: figure.color,
            short: Array.from(figure.title)[0],
            isBlack: figure.color == "black"
          }, "*")
        }
        let figureId = item[0].id
        await req.knex("t_figurePosition").insert({
          figureId,
          position: fieldName,
          devicePositionId: devicePosition.id,
        })
      }
    }


    for (let vector of req.body.vectors) {
      console.log(vector)
      let fieldName = Object.keys(vector)[0]
      let figure = vector[fieldName];
      let figureId = null;
      if (figure.role) {
        figure.title = capitalizeFirstLetter(figure.color) + " " + capitalizeFirstLetter(figure.role)
        let item = await req.knex("t_figure").where({ title: figure.title })
        if (item.length == 0) {
          item = await req.knex("t_figure").insert({
            title: figure.title,
            color: figure.color,
            short: Array.from(figure.title)[0],
            isBlack: figure.color == "black"
          }, "*")
        }
        figureId = item[0].id
      }
      await req.knex("t_deviceVectors").insert({
        figureId,
        field: fieldName,
        date: new Date(vector.time * 1000),
        positionId: devicePosition.id,
      })

      //{ e8: { role: 'knight', color: 'white' }, time: 1710839458.1040058 }

    }

    res.json(parseInt(devicePosition.id));
  }
  catch (e) {
    console.warn(e)
    res.json(0);
  }

});

module.exports = router;
