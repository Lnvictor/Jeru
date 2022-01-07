import datetime

from sqlalchemy_serializer import SerializerMixin

from .ext.db import db


class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(80), unique=True)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    birthday = db.Column("birthday", db.DateTime)
    password = db.Column("password", db.String(15))
    has_email_verified = db.Column("has_email_verified", db.Boolean, default=False)
    last_email_sended_at = db.Column(
        "las_email_sended_at", db.DateTime, default=datetime.datetime.now()
    )
    last_token_sended = db.Column(
        "last_token_sended", db.String(15), default=None, nullable=True
    )

    def __repr__(self):
        return self.email


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column("id", db.Integer, primary_key=True, increment=1)
    name = db.Column("name", db.String(30), unique=True, nullable=False)
    gtin = db.Column("gtin", db.String(30), unique=True, nullable=False)
    producer_id = db.Column("producer_id", db.ForeignKey("producer.id"))

    def __repr__(self) -> str:
        return super().__repr__()


class Producer(db.Model):
    __tablename__ = "producer"

    id = db.Column("id", db.Integer, primary_key=True, start=1, increment=1)
    name = db.Column("name", db.String(30), unique=True, nullable=False)
    cnpj = db.Column("cnpj", db.String(15), nullable=False, unique=True)
    sector = db.Column(
        "sector",
        db.String(15),
    )

    products = db.relationship("Product", backref="producer")

    def __repr__(self) -> str:
        return f"name: {self.name}, cnpj: {self.cnpj}"


class Seller(db.Model):
    __tablename__ = "seller"

    id = db.Column("id", db.Integer, primary_key=True, start=1, increment=1)
    name = db.Column("name", db.String(30), unique=True, nullable=False)
    sector = db.Column(
        "sector",
        db.String(15),
    )

    products = db.relationship("Product", backref="producer")


class ProductSeller(db.Model):
    __tablename__ = "product_seller"

    id = db.Column("id", db.Integer, primary_key=True, start=1, increment=1)
    seller_id = db.Column("seller_id", db.ForeignKey("seller.id"))
    product_id = db.Column("product_id", db.ForeignKey("product.id"))
    price = db.Column("price", db.Decimal)


# class ProductList():
#     """Not implemented yet"""
#     pass
