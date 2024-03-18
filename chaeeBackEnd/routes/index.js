var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.post('/api/chess', function(req, res, next) {
  console.log(req.body)
   res.json(123);
});

module.exports = router;
