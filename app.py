from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Hello world!"}

# Created some test data to display.
products = [
    {"id": 0, "name": "Pen", "price": "1000"},
    {"id": 1, "name": "Biro", "price": "6000"},
    {"id": 2, "name": "Book", "price": "5000"},
    {"id": 3, "name": "Cup", "price": "1500"},
]

# A route to return all products.
@app.route("/api/v1/products", methods=["GET"])
def get_all_products():

    # use the jsonify function to convert list of dictionaries to JSON format
    return jsonify(products)

# A route to get a specific product by the id
@app.route("/api/v1/products/<int:id>", methods=["GET"])
def get_product(id):
    result = []

    # looped through the list of products to get an ID that matches
    for product in products:
        if product["id"] == id:
            result.append(product)

    return jsonify(result)

app.run()