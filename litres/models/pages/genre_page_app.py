import time

from selene import have
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from litres.models.pages.home_page_app import HomePage
from typing import Tuple


class GenrePage:
    def __int__(self):
        return self

    def select_genre(self):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                        '.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view'
                        '.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx'
                        '.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.Button'))\
            .click()
        return self

    def select_subgenre_history(self):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                        '.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget'
                        '.ScrollView/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx'
                        '.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android'
                        '.view.ViewGroup[2]')).click()
        return self

    def check_open_genre(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/subgenreTitleTextView"))\
            .should(have.text('Biographies and memoirs'))
        return self


