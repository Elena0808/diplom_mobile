import os
from enum import Enum
from selene import have, be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy
from litres.models.pages.home_page_app import HomePage


class ProfilePage(HomePage):
    def __int__(self):
        return self

    def open_login_form(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button')).click()
        return self

    def set_login_and_password(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/login')).type(os.getenv('LOGIN'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/password')).type(os.getenv('PASSWORD'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/sign_in_btn')).click()
        return self

    def check_login(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/user_name')).should(have.text('Registered reader'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/user_login')).should(have.text('autotest123@rambler.ru'))
        browser.element((AppiumBy.ID, 'ru.litres.android:id/add_money_button')).should(be.visible)
        return self

    def open_select_language(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/spinner_value')).click()
        return self

    def language_select(self, language: Enum):
        browser.element((AppiumBy.XPATH, f'/hierarchy/android.widget.FrameLayout/android.widget'
                                         f'.LinearLayout/android.widget.FrameLayout/android.view'
                                         f'.ViewGroup/android.widget.LinearLayout[2]/android.widget'
                                         f'.FrameLayout/androidx.recyclerview.widget.RecyclerView/android'
                                         f'.widget.LinearLayout[{language.value}]/android.widget.RadioButton')) \
            .click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/md_buttonDefaultPositive')).click()
        return self

    def check_language_change(self, text):
        browser.element((AppiumBy.ID, "ru.litres.android:id/spinner_value")).should(have.text(f'{text}'))
        return self

    def open_promotion(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/new_profile_bonuses')).click()
        return self

    def check_open_promotion_page(self):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/title')).should(have.text('Fourth book for free'))
        return self
