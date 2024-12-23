from database import db

order_products = db.Table(
    "order_products",
    db.Column('order_id', db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.ForeignKey('products.id'), primary_key=True),
    db.Column('quantity', db.Integer)
)
