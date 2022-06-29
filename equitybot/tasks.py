from __future__ import absolute_import, unicode_literals

from celery import shared_task


from .utils import setup_driver, login_to_mql5, scrape_data

from .models import Equity



@shared_task
def add_latest_data():
    driver = setup_driver()
    login_to_mql5(driver)
    market_watch, balance, equity = scrape_data(driver)
    Equity.objects.create(market_watch=market_watch, balance=balance, equity=equity)
