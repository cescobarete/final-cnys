<<<<<<< HEAD
// imports
const express = require('express')
const prod = express()
const port = 3000

// static Files
prod.use(express.static('./production'))

// Listeen on port 3000
prod.listen(port, () => console.info('Listening on port 3000'))
=======
const { Router } = require("express");

const config = {
    endpoint: "<https://manage.documents.azure.com:443/>",
    key: "qXbT2LG82V09OhvsqfVNxyaN5hcaR7pA4fyuoJc12IvwZNgUu2EnAee6u5Z6v8aoJtbN3jp8as84TRb0iVMc1A==",
    databaseId: "customer-db",
    containerId: "Customer",
    partitionKey: { kind: "Hash", paths: ["/category"] }
  };
  
  module.exports = config;

>>>>>>> 3e479ae1c82d2de43d1324043f8975fbcfc1c590
