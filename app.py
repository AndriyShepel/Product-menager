from flask import Flask, render_template, request, flash, redirect, url_for
from models import _init_db
from action_db import *


app = Flask(__name__)

app.secret_key = "$#Python&"
_init_db()

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("product_name")
        price = float(request.form.get("product_price"))
        category = request.form.get("product_category")
        if product_exists(name):
            flash("Такий товар вже є!")
        else:
            add_product(name, price, category)

        redirect(url_for("index"))  

    all_categories = get_all_categories()

    choice_category = request.args.get("category", "all")

    if choice_category == 'all':
        filter_products = get_all_products()
    else:
        filter_products = get_product_from_category(choice_category)

    return render_template("index.html", items=filter_products, choice_category=choice_category, categories=all_categories)

@app.route("/delete/<index>")
def delete(index):
    delete_product(index)

app.run(debug=True)