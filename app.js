// imports
const express = require('express')
const app = express()
const port = 3000

// static Files
app.use(express.static('./public'))

// Listeen on port 3000
app.listen(port, () => console.info('Listening on port 3000'))
