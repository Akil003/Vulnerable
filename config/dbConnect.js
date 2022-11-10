const mysql = require("mysql2");

const db = mysql.createConnection({
  host: 'localhost',
  user: "root",
  port: 3306,
  password: "pass",
  database: "isaa_db",
  multipleStatements: true
});

module.exports = db;
