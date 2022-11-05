const csrf = require("csurf");

const csrfProt = csrf({ cookie: true });
module.exports = csrfProt;
