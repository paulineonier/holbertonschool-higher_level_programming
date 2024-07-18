from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        items = load_items_from_json('products.json')
    else:
        items = load_items_from_csv('products.csv')

    if product_id:
        items = [item for item in items if item.get('id') == product_id]
        if not items:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
