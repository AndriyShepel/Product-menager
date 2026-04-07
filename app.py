from flask import Flask, render_template, request, flash, redirect, url_for
from models import _init_db


app = Flask(__name__)

app.secret_key = "$#Python&"
items = []
_init_db()

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("product_name")
        price = request.form.get("product_price")
        category = request.form.get("product_category")
        for item in items:
            if item.get("name") == name:
                flash("Такий товар вже існує")
                break
            else:
                add_product = {"name": name, "price":price, "category":category}
                items.append(add_product)

        redirect(url_for("index"))  

    choice_category = request.args.get('category', 'all')

    if choice_category == 'all':
        filter_products = items
    else:
        filter_products = filter(lambda item: item['category'] == choice_category, items)

    return render_template("index.html", items=items)

@app.route("/delete/<index>")
def delete(index):
    delete_product = items.pop(index)
    name = delete_product.get("name")
    flash(f"Товар {name} успішно видаленно!")

app.run(debug=True)