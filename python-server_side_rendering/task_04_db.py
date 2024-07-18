from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def load_items_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def load_items_from_csv(file_path):
    items = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                items.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except FileNotFoundError:
        return []
    except Exception:
        return []
    return items

def load_items_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        items = cursor.fetchall()
        conn.close()
        return [{'id': item[0], 'name': item[1], 'category': item[2], 'price': item[3]} for item in items]
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        items = load_items_from_json('products.json')
    elif source == 'csv':
        items = load_items_from_csv('products.csv')
    elif source == 'sql':
        items = load_items_from_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        filtered_items = [item for item in items if item.get('id') == product_id]
        if not filtered_items:
            return render_template('product_display.html', error="Product not found")
        items = filtered_items
    
    return render_template('product_display.html', products=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
