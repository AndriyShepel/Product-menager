from flask import Flask, render_template, request, flash


app = Flask(__name__)

items = []

@app.route('/', methods=["POST", "GET"])
def index():
    global items
    if request.method == "Post":
        product_name = request.form.get("product_name")
        product_price = request.form.get("product_price")
        product_category = request.form.get("product_category")
        for item in items:
            if item.get("name") == product_name:
                flash("Такий товар вже існує")
                break
        else:
            add_product = {"name": product_name, "price":product_price, "category":product_category}
            item.append(add_product)
    return render_template("index.html")

app.run(debug=True)