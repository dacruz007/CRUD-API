from flask import Flask, request, jsonify
import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "productDB.db")
app = Flask(__name__)

@app.route('/product', methods=['GET'])
def api_get_all():
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        query = 'SELECT * FROM products'
        products = cur.execute(query).fetchall()
        return jsonify(products), 200

@app.route('/product/<int:id>', methods=['GET'])
def api_get_id(id):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        id = request.args['id']
        query = 'SELECT * FROM products WHERE id = ?', id
        product = cur.execute(query)
        return jsonify(product), 200
	
@app.route('/product', methods=['POST'])
def api_post():
    id = request.args['id']
    product_name = request.args['product_name']
    price = request.args['price']
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        item = (id, product_name, price)
        cur.execute('INSERT INTO products(id,product_name,price) VALUES (?,?,?)',item)
        conn.commit()
    return jsonify('Posted'), 200
    conn.close()

@app.route('/product', methods=['DELETE'])
def api_delete_id():
    id = request.args['id']
    with sqlite3.connect(db_path) as conn:
        try:
             cur = conn.cursor()
             cur.execute('DELETE FROM products WHERE id = ?', id)
             return jsonify('Deleted'), 200  
        except:  
            msg = "No Record Found for Deletion"  
    
        
@app.route('/product', methods=['PUT'])
def api_update():
    with sqlite3.connect(db_path) as conn:
        id = request.args['id']
        price = request.args['price']
        product_name = request.args['product_name']
        cur = conn.cursor()
        query = 'UPDATE products SE'
        cur.execute('UPDATE products SET price = ?, product_name = ? WHERE id = ?',(price, product_name, id))
        conn.commit()
        return jsonify('Updated'),200



app.run(debug=True)