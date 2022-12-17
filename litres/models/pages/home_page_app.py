import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import be, have
from selene.support.shared import browser


class HomePage:
    def __int__(self):
        return

    def open_home_page(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_skip')).click()
        time.sleep(12)
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent')).click()
        return self

    def select_language(self):
        #browser.element((AppiumBy.))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
        return self

    def skip_info(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btn_onboarding_litres_app_skip')).click()
        return self

    def adult_content(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/btnEnableAdultContent')).click()
        time.sleep(10)
        return self

    def open_my_book(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/nav_my_audiobooks')).click()
        return self

    def open_profile(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item')).click()
        time.sleep(7)
        return self

    def open_genre_page(self):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.LinearLayout[@content-desc="Genres"]/android.widget.TextView')).click()
        time.sleep(20)
        return self

    def open_search(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/nav_search')).click()
        return self

    def check_open_home_page(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/listTitleButton')).should(be.visible)
        return self
