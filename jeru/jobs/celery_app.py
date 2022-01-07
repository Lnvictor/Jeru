from time import sleep

from celery import Celery
from celery.schedules import crontab

from prices_crawler import PricesCrawler

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def run():
    prices_crawler = PricesCrawler()
    prices_crawler.run_crawler()
    sleep(3)
    load_from_csv()


app.conf.beat_schedule = {
    "add-every-30-seconds": {
        "task": "celery_app.run",
        "schedule": crontab(hour=2, minute=14),
        "args": (),
    },
}
app.conf.timezone = "UTC"
