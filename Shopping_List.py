from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def start_page():
    return "Welcome to eShopping"


Shopping_list = [
    {
        "_id": "U1IT00010",
        "item_name": "blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340
    },
    {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    },
    {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    },
    {
        "_id": "BF00001CFOOD",
        "item_name": "Bread",
        "quantity": 2,
        "ingredients": "all-purpose flour"
    }
]


@app.route('/Shopping_list')
def get_shopping_list():
    return jsonify(Shopping_list)


@app.route('/Shopping_list', methods=['POST'])
def add_shopping_list():
    Shopping_list.append(request.get_json())
    return 'Item Added'


if __name__ == "__main__":
    app.run(debug=True)
