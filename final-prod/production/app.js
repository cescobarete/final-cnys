// Import configuration
const express = require("express");
const CosmosClient = require("@azure/cosmos").CosmosClient;
const config = require("./config");
const dbContext = require("./data/databaseContext");
const app = express();
const handlebars = require("express-handlebars")
const bodyParser = require("body-parser");

//bodyParse parses in the incoming requests before handling the request
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//handlebars: Used to render web page to the client side 
//from data on the server-side
app.engine(".handlebars", handlebars({
  defaultlayout: "main"
}));

app.set("view engine", "handlebars");

//Async is a utility module which provides straight-forward, 
//powerful functions for working with asynchronous JavaScript
async function main(newItem) {
  
  // Create client object database container
  //Takes the endpoint,key, database name customer-db, and db continer customer
  const { endpoint, key, databaseId, containerId } = config;
  const client = new CosmosClient({ endpoint, key });
  const database = client.database(databaseId);
  const container = database.container(containerId);

  // Make sure Tasks database is already setup. If not, create it.
  await dbContext.create(client, databaseId, containerId);
  // Create client object database container
  try {
    // <Query items>
    console.log(`Querying container: Items`);

    // query to return all items
    //Seects all the fields ID, name, pname, pcategory, pid 
    //and grabs it from the customer container
    const querySpec = {
      query: "SELECT * from Customer"
    };
    
    // read all items in the Items container
    //takes variable queryspec, gives access to all items in the container
    const { resources: items } = await container.items
      .query(querySpec)
      .fetchAll();
    
    //Display each item in console
    items.forEach(item => {
      console.log(`${item.id} - ${item.name}`);
      console.log(`${item.Pname} - ${item.Pcategory} -  ${item.Pid}`);

    });
    // </QueryItems>
    
    // <CreateItem>
    /** Create new item
     * newItem is defined at the top of this file
     */
    const { resource: createdItem } = await container.items.create(newItem);
    
    console.log(`\r\nCreated new item: ${createdItem.id} - ${createdItem.name}\r\n`);
    console.log(`\r\nCreated new item: ${createdItem.Pname} - ${createdItem.Pcategory} - ${createdItem.Pid} \r\n`);
    
    // </CreateItem>
  } catch (err) {
    console.log(err.message);
  }
}

async function maindelete(newItem) {
  
  // Create client object database container
  const { endpoint, key, databaseId, containerId } = config;
  const client = new CosmosClient({ endpoint, key });
  const database = client.database(databaseId);
  const container = database.container(containerId);

  // Make sure Tasks database is already setup. If not, create it.
  await dbContext.create(client, databaseId, containerId);
  // Create client object database container
  try {
    // <Query items>
    console.log(`Querying container: Items`);

    // query to return all items
    const querySpec = {
      query: "SELECT * from Customer"
    };
    
    // read all items in the Items container
    const { resources: items } = await container.items
      .query(querySpec)
      .fetchAll();

    items.forEach(item => {
      console.log(`${item.id} - ${item.name}`);
    });
    // </QueryItems>

    const { id, name } = newItem;
  
    const { resource: result } = await container.item(id, name).delete();
    console.log(`Deleted item with id: ${id}`);
    // </DeleteItem> */
  } catch (err) {
    console.log(err.message);
  }
}

async function mainupdate(newItem) {
  
  // Create client object database container
  const { endpoint, key, databaseId, containerId } = config;
  const client = new CosmosClient({ endpoint, key });
  const database = client.database(databaseId);
  const container = database.container(containerId);

  // Make sure Tasks database is already setup. If not, create it.
  await dbContext.create(client, databaseId, containerId);
  // Create client object database container
  try {
    // <Query items>
    console.log(`Querying container: Items`);

    // query to return all items
    const querySpec = {
      query: "SELECT * from Customer"
    };
    
    // read all items in the Items container
    const { resources: items } = await container.items
      .query(querySpec)
      .fetchAll();

    items.forEach(item => {
      console.log(`${item.id} - ${item.name}`);
    });
    // </QueryItems>
    
    // <UpdateItem>
    /** Update item
     * Pull the id and partition key value from the newly created item.
     * Update the isComplete field to true.
     */
    const { id, name } = newItem;

    const { resource: updatedItem } = await container
      .item(id, name)
      .replace(newItem);

    console.log(`Updated item: ${updatedItem.id} - ${updatedItem.name}`); 
   //</UpdateItem>
  } catch (err) {
    console.log(err.message);
  }
}

async function CustomerProd(newItem) {
  
  // Create client object database container
  const { endpoint, key, databaseId, containerId } = config;
  const client = new CosmosClient({ endpoint, key });
  const database = client.database(databaseId);
  const container = database.container(containerId);

  // Make sure Tasks database is already setup. If not, create it.
  await dbContext.create(client, databaseId, containerId);
  // Create client object database container
  try {
    // <Query items>
    console.log(`Querying container: Items`);

    // query to return all items
    const querySpec = {
      query: "SELECT * from Customer"
    };
    
    // read all items in the Items container
    const { resources: items } = await container.items
      .query(querySpec)
      .fetchAll();

    items.forEach(item => {
      console.log(`${item.Pname} - ${item.Pcategory} -  ${item.Pid}`);
    });

    const { resource: createdItem } = await container.items.create(newItem);
    
    console.log(`\r\nCreated new item: ${createdItem.Pname} - ${createdItem.Pcategory} - ${createdItem.Pid} \r\n`);
    
  } catch (err) {
    console.log(err.message);
  }
}

//Sends user input to db
app.get("/", (req, res)=> {
  res.sendFile('./index.hsb.html', {root: __dirname})
});

app.get("/test/enter", (req, res)=> {
  res.sendFile('./index.hsb.html', {root: __dirname})
});

//Displays user input to console from db
app.post("/test/enter", async (req, res)=> {
  await main(req.body);
  console.log("Posted!!!!")
});

//Sends user input for delete to db
app.get("/test/delete", (req, res)=> {
  res.sendFile('./index.hsb.html', {root: __dirname})
});

//Displays user input to console from db
app.post("/test/delete", async (req, res)=> {
  await maindelete(req.body);
  console.log("Deleted!!!!")
});

//Sends user response from form to db
app.get("/test/update", (req, res)=> {
  res.sendFile('./index.hsb.html', {root: __dirname})
});

//Displays updated list
app.post("/test/update", async (req, res)=> {
  await mainupdate(req.body);
  console.log("Updated!!!!")
});

//Sends user input to db 
app.get("/Customer/Product", (req, res)=> {
  res.sendFile('./index.hsb.html', {root: __dirname})
});

//Displays user input to console
app.post("/Customer/Product", async (req, res)=> {
  await CustomerProd(req.body);
  console.log("New Product")
});

app.listen(3002, (req, res) => {});