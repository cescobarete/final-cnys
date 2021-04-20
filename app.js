// imports
const express = require('express')
const mysql = require('mysql');
const app = express()
const port = 3001

const con = mysql.createConnection({
    host: "localhost",
    user: "ms_user_two",
    password: "manageuser",
    database: "CustomerDb"
});

con.connect((err) => {
    if (err) {
        console.log('Connection established to MySql');
    }
});

// static Files
app.use(express.static('./public'))

// Listeen on port 3000
app.listen(port, () => console.info('Listening on port 3000'))
