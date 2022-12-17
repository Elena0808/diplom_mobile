import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import be
from selene.support.shared import browser
from litres.models.pages.home_page_app import HomePage


class SearchPage(HomePage):
    def __int__(self):
        return

    def search_book(self, search_book_name):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/nav_search')).click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')).type(search_book_name)
        return self

    def open_search_book(self):
        browser.element()
        return self

    def check_search(self):
        time.sleep(8)
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="All results"]/android'
                                         '.widget.TextView')).should(be.visible)
        return self
