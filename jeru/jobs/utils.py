from requests import post
from scrapy.http import HtmlResponse


def parse_higa(response):
    try:
        products_cards = response.css("div.card-body").getall()

        for card in products_cards:
            card_html = HtmlResponse(url=card, body=card, encoding="utf-8")
            product_name = card_html.css("h3::text").get().replace(",", "").strip()
            price = card_html.css("div>span::text").get().replace(",", ".").strip()

            with open("./higa_prod.csv", "a") as file:
                file.write(f"{product_name},{price}\n")
    except AttributeError:
        return


def parse_enxuto(response):
    a = response.css("div.prodmain").getall()

    for prod in a:
        current_response = HtmlResponse(url=prod, body=prod, encoding="utf-8")
        price = (
            current_response.css("div.price-box>span>span.price>span::text")
            .get()
            .replace(",", ".")
        )
        product_name = (
            current_response.css("a.prodname::text").get().replace(",", "").strip()
        )

        with open("./enxuto_prod.csv", "a") as file:
            file.write(f"{product_name},{price}\n")


def load_from_csv():
    # try:
    with open("./enxuto_prod.csv", "r") as file_enxuto, open(
        "./higa_prod.csv", "r"
    ) as file_higa:
        for line in file_enxuto.readlines()[1:]:
            name, price = line.split(",")
            post(
                url="http://localhost:5000/product",
                json={"name": name, "price": float(price[2:]), "seller_id": 1},
                headers={"Authorization": "Bearer tokena"},
            )

        for line_higa in file_higa.readlines()[1:]:
            name_prod_higa, price_prod_higa = line_higa.split(",")
            post(
                url="http://localhost:5000/product",
                json={
                    "name": name_prod_higa,
                    "price": float(price_prod_higa[2:]),
                    "seller_id": 2,
                },
                headers={"Authorization": "Bearer tokena"},
            )

        return True


# except:
#     return False
