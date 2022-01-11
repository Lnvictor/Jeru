import json

from ...ext.db import db
from ...models import Product


def create_product(data):
    prod = Product(**data)
    db.session.add(prod)
    db.session.commit()


def search_product(data):
    result = db.engine.execute(
        f"""SELECT * FROM product WHERE LOWER(name) LIKE '%{data["input"]}%'"""
    )
    records = [row for row in result]
    records.sort(key=lambda x: x[2])
    return {
        "Name": records[0][1],
        "Price": records[0][2],
        "Supermarket": "Enxuto" if records[0][3] == 1 else "Higa",
    }
