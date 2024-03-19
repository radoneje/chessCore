const express = require('express');
const router = express.Router();
const moment = require('moment');

const capitalizeFirstLetter = (string) => {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', { title: 'Express' });
});
router.post('/api/chess/:deviceId', async (req, res, next) => {
  try {
    let devicePosition = (await req.knex("t_devicePosition").insert({
      date: new Date(req.body.time * 1000),
      deviceId: req.params.deviceId
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
