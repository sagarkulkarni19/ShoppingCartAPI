import sqlite3

conn = sqlite3.connect('Shopify_products.db')
c = conn.cursor()
c.execute('DROP TABLE products;')
c.execute('''CREATE TABLE products(id real PRIMARY KEY, title text, inventory_count real, price real)''')
storage = [(0,'item1',5,200),(1,'item2',3,200),(2,'item3',2,4000),(3,'item4',7,3200),(4,'item5',10,50),]
c.executemany('INSERT INTO products VALUES (?,?,?,?)',storage)
conn.commit()

#conn.commit()

