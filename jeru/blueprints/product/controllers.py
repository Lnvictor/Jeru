from ...ext.db import db
from ...models import Product


def create_product(data):
    prod = Product(**data)
    db.session.add(prod)
    db.session.commit()
