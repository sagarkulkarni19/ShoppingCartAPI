# ShoppingCartAPI
A shopping cart API using Python Flask framework.
The shopping cart has the following functionalities:
  - Display all products available(with inventory count)
  - Search for a particular product with id or title of product.
  - Add products to a shopping cart.
  - Delete products from a shopping cart
  - Display all the products added to the shopping cart
  - Complete the purchase of all the items in the shopping cart(Subsequently reduce the inventory count of those products from the main database).
  

### API routes(Methods used:[GET]):

|Route|Description|
|------|------|
|/| Home page of the API|
|/v1/items/all|Displays all the products present in the database|
|/v1/items?parameter=value|Search for products on the basis of 'id' or 'title' parameter|
|/v1/cart/|Display all the products present in the cart||
/v1/cart/add?id=value|Add products to the cart based on the id provided|
|/v1/cart/delete?id=value|Delete products from the cart based on the id provided|
|/v1/cart/confirm|Complete the purchase of the current cart(Decreses the inventory count of the products)|
  
