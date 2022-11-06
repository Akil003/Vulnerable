const express = require('express');
const allowAuth = require('../middlewares/allowAllAuth');
const router = express.Router();
const checkAuth = require("../middlewares/checkAuth");
const redirectIfAuth = require("../middlewares/redirectIfAuth");
const csrfProt = require("../middlewares/csrfProt");

router.get('/', csrfProt, redirectIfAuth, function(req, res, next) {
  res.render('csrf/index');
});


router.get('/transfer', csrfProt, checkAuth, function(req, res, next) {
  res.render('csrf/transfer', { acc_no: req.cookies.acc_no });
});

module.exports = router;
