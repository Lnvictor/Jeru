import pytest

from jeru.blueprints.product.controllers import create_product, search_product

from .test_auth import client


def test_create_product(client):
    data = {"name": "Batatinha", "price": 13.14, "seller_id": 1}
    product = create_product(data)
    assert product.name == "Batatinha"


def test_search_product():
    """
    TODO:
    """
    pass
