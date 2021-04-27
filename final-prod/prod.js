// @ts-check

const config = {
    endpoint: "<https://manage.documents.azure.com:443/>",
    key: "<qXbT2LG82V09OhvsqfVNxyaN5hcaR7pA4fyuoJc12IvwZNgUu2EnAee6u5Z6v8aoJtbN3jp8as84TRb0iVMc1A==>",
    databaseId: "Tasks",
    containerId: "Items",
    partitionKey: { kind: "Hash", paths: ["/category"] }
  };
  
  module.exports = config;