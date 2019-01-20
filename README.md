# ShoppingCartAPI
A simple and easy to use shopping cart API developed using Python Flask framework.
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
  
## Steps to interact with the API
  - Install python 3.6
  - Install python flask 
  - Clone the repository(or copy the files to a folder in your system)
  - Run query_input.py file to create the database with a product table(with sample values added)
  - Run api_final.py
  - Use url http://127.0.0.1:5000/ and the above table to interact with the API.
  
Note: API secure(partly) against sql injection attacks while querying.( By the usage of a placeholder '?' in the query instead of a '%s' string formatting syntax which is vulnerable against sql-injection attacks).
