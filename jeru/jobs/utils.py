from scrapy.http import HtmlResponse


def parse_higa(response):
    products_cards = response.css("div.card-body").getall()

    for card in products_cards:
        card_html = HtmlResponse(url=card, body=card, encoding="utf-8")
        product_name = card_html.css("h3::text").get()
        price = card_html.css("div>span::text").get().strip()

        with open("./higa_prod.csv", "a") as file:
            file.write(f"{product_name},{price}\n")


def parse_enxuto(response):
    a = response.css("div.prodmain").getall()

    for prod in a:
        current_response = HtmlResponse(url=prod, body=prod, encoding="utf-8")
        product_name = current_response.css(
            "div.price-box>span>span.price>span::text"
        ).get()
        price = current_response.css("a.prodname::text").get()

        with open("./enxuto_prod.csv", "a") as file:
            file.write(f"{product_name},{price}\n")


def load_from_csv():
    """TODO: Implementar metodo que lê arquivos csv e salva produtos no banco"""
    pass
