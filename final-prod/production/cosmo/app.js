// Import configuration
const express = require("express");
const CosmosClient = require("@azure/cosmos").CosmosClient;
const config = require("./config");
const dbContext = require("./data/databaseContext");
const app = express();

// Define new item
const newItem = {
  id: "108",
  name: "Sashaa"
};

//Async is a utility module which provides straight-forward, 
//powerful functions for working with asynchronous JavaScript
async function main() {
  
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
    
    // <CreateItem>
    /** Create new item
     * newItem is defined at the top of this file
     */
    const { resource: createdItem } = await container.items.create(newItem);
    
    console.log(`\r\nCreated new item: ${createdItem.id} - ${createdItem.name}\r\n`);
    // </CreateItem>
    
    // <UpdateItem>
    /** Update item
     * Pull the id and partition key value from the newly created item.
     * Update the isComplete field to true.
     */
    const { id, name } = createdItem;

    const { resource: updatedItem } = await container
      .item(id, name)
      .replace(createdItem);

    console.log(`Updated item: ${updatedItem.id} - ${updatedItem.name}`); 
    // </UpdateItem>
    
    // <DeleteItem>    
    /**
     * Delete item
     * Pass the id and partition key value to delete the item
     */
    //const { resource: result } = await container.item(id, name).delete();
    //console.log(`Deleted item with id: ${id}`);
    // </DeleteItem>  
    
  } catch (err) {
    console.log(err.message);
  }
}

app.get("/", (req, res)=> {
  res.send("hello")
});

app.get("/test/enter", (req, res)=> {
  res.render("index");
});

app.post("/test/enter", (req, res)=> {
  main();
});

app.listen(3001, (req, res) => {});