from models import Product


def get_all_products():
    return Product.select()

def get_product_from_category(category: str):
    return Product.select().where(Product.category == category)

def get_all_categories():
    return Product.select(Product.category).distinct().order_by(Product.category)

def product_exists(name:str) -> bool:
    return Product.select().where(Product.name == name).exists()

def add_product(name:str, price: float, category: str):
    return Product.create(name = name, price = price, category = category)