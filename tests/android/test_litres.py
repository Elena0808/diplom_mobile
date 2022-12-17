import allure
from allure_commons.types import Severity
from litres.models import app
from litres.models.data import data_search_book_app
from litres.models.data.data_profile import Languages


@allure.tag('mobile')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Главная страница')
@allure.story('Открытие главной страницы')
def test_open_home_page():
    with allure.step('Открываем приложение, выбираем язык и закрываем предупреждение'):
        app.home_page.select_language() \
            .skip_info() \
            .adult_content()
    with allure.step('Проверяем открытие главной страницы'):
        app.home_page.check_open_home_page()


@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Elena0808')
@allure.description('Изменение языка')
@allure.feature('Изменение языка приложения на Русский язык')
def test_select_language():
    with allure.step('Открываем приложение и переходим на страницу профиля'):
        app.home_page.open_home_page() \
            .open_profile()
    with allure.step('Меняем язык приложения на Русский язык'):
        app.profile_page.open_select_language() \
            .language_select(Languages.Russian)
    with allure.step('Проверяем, что язык изменился'):
        app.profile_page.check_language_change('Русский')


@allure.tag('mobile')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Поиск книг')
@allure.feature('Поиск книги с валидным названием')
def test_search_book():
    with allure.step('Открываем приложение и открываем поиск'):
        app.home_page.open_home_page() \
            .open_search()
    with allure.step(f'Вводим в строку поиска название книги {data_search_book_app.search_book_name}'):
        app.search_page.search_book(data_search_book_app.search_book_name)
    with allure.step('Проверяем результат поиска'):
        app.search_page.check_search()


@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena0808')
@allure.description('Жанры')
@allure.feature('Открытие страницы жанра "История"')
def test_open_history_book():
    with allure.step('Открываем приложение и переходим на страницу "Жанры"'):
        app.home_page.open_home_page() \
            .open_genre_page()
    with allure.step('Выбираем жанр "История'):
        app.genre_page.select_genre()
    with allure.step('Проверяем открытие страницы жанра "История"'):
        app.genre_page.check_open_genre()


@allure.tag('mobile')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Авторизация')
@allure.feature('Авторизация с валидными логином и паролем')
def test_auth():
    with allure.step('Открываем приложение и переходимна страницу профиля'):
        app.home_page.open_home_page() \
            .open_profile()
    with allure.step('Авторизуемся'):
        app.profile_page.open_login_form() \
            .set_login_and_password()
    with allure.step('Проверяем успешную авторизацию'):
        app.profile_page.check_login()


@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena0808')
@allure.description('Раздел "Акции и бонусы"')
@allure.story('Проверка открытия страницы с акциями и бонусами')
def test_open_promotion():
    with allure.step('Открываю приложение и перехожу на главную страницу'):
        app.home_page.open_home_page()
    with allure.step('Перехожу на страницу профиля'):
        app.home_page.open_profile()
    with allure.step('Открываю страницу с акциями и бонусами'):
        app.profile_page.open_promotion()
    with allure.step('Проверяю, что страница открыта'):
        app.profile_page.check_open_promotion_page()
