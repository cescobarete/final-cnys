// imports
const express = require('express')
const prod = express()
const port = 3000

// static Files
prod.use(express.static('./production'))

// Listeen on port 3000
prod.listen(port, () => console.info('Listening on port 3000'))