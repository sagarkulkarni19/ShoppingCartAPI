import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row): 
	"""Converts rows that need to be retrieved into a dictionary object. This function replaces the existing row_factory attribute of the sqlite3 connection object.z"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
	"""This is the home page of the API."""
    return "<h1>Shopify Backend assignment</h1><p>This site is a prototype for shopping cart API.</p>"


@app.route('/v1/items/all', methods=['GET']) 
def api_all():
	"""Displays all the products present in the database."""
    conn = sqlite3.connect('Shopify_products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_products = cur.execute('SELECT * FROM products;').fetchall()
    return jsonify(all_products)

@app.route('/v1/items', methods=['GET'])
def api_search():
	"""Search for products on the basis of 'id' or 'title' values.Eg: Use /v1/items?id=3 to search for the product whose id equals to 3."""
    if 'id' in request.args:
        id = int(request.args['id'])
        flag_id=1
        flag_title=0
    elif 'title' in request.args:
    	title = request.args['title']
    	flag_title=1
    	flag_id=0
    else:
        return "Error: No id/title field provided. Please specify an id/title."

    conn = sqlite3.connect('Shopify_products.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    # Create an empty list for our results
    if flag_id==1:
    	t = (id,)
    	products = cur.execute('SELECT * FROM products WHERE id=? ',t).fetchone()
    	return jsonify(products)
    else:
    	t = (title,)
    	products = cur.execute('SELECT * FROM products WHERE title=? ',t).fetchone()
    	return jsonify(products)

@app.route('/v1/cart/add',methods=['GET'])
def api_add_cart():
	"""Add products to the cart based on the id provided. Eg: Use /v1/cart/add?id=2 to add product whose id equals 2."""
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided. Please specify an id."

	conn = sqlite3.connect('Shopify_products.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS cart(id real PRIMARY KEY, title text, inventory_count real, price real)''')
	count= cur.execute('SELECT COUNT(*) FROM cart WHERE id=? ',(id,)).fetchone()
	#print(count)
	if count['COUNT(*)']>=1:
		return "Already in the cart"
	else:
		record = cur.execute('SELECT * FROM products WHERE products.id=?',(id,)).fetchone()
		if record==None:
			return "No such product exists"
		cur.execute('INSERT INTO cart VALUES(?,?,?,?)',(record['id'],record['title'],record['inventory_count'],record['price']))
		conn.commit()
		return "Item has been added to the cart"

@app.route('/v1/cart/',methods=['GET'])
def api_display_cart():
	"""Display all the products present in the cart."""
	conn = sqlite3.connect('Shopify_products.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	cart = cur.execute('SELECT * FROM cart;').fetchall()
	cart.append(cur.execute('SELECT SUM(price) from cart;').fetchone())
	return jsonify(cart)

@app.route('/v1/cart/delete',methods=['GET'])
def api_delete_cart():
	"""Delete products from the cart based on the id provided. Eg: Use /v1/cart/delete?id=2 to delete product from cart whose id equals to 2."""
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided. Please specify an id."

	conn = sqlite3.connect('Shopify_products.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	count= cur.execute('SELECT COUNT(*) FROM cart WHERE id=? ',(id,)).fetchone()
	if count['COUNT(*)']==0:
		return "Error:The item you want to delete is not available in the cart"
	else:
		cur.execute('DELETE FROM cart WHERE id=?',(id,))
		conn.commit()
		return 'Successfully deleted the item'



@app.route('/v1/cart/confirm',methods=['GET'])
def api_confirm_cart():
	"""Complete the purchase of the current cart(Decreses the inventory count of the products)."""
	conn = sqlite3.connect('Shopify_products.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	for row in cur.execute('SELECT * FROM cart').fetchall():
		(id1,title,count,price) = row['id'], row['title'], row['inventory_count'],row['price']
		print(row)
		cur.execute('UPDATE products SET inventory_count = inventory_count-1 WHERE id=? AND inventory_count>0',(id1,))
		print("Reduced from "+ str(count)+"/n")
	p= cur.execute('SELECT * FROM products').fetchall()
	cur.execute('DELETE FROM cart;')
	conn.commit()
	return jsonify(p)
	#return "Cart has been purchased!Thank you for shopping"



app.run()

