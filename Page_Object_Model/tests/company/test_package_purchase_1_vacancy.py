import time

import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.user_personal_account_page import UserPersonalAccountPage
from Page_Object_Model.pages.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage

@pytest.mark.parametrize('language', ["", "/ua"])
def test_package_purchase_1_vacancy_and_orders_processing_and_activating_it_on_site(browser, language):  # покупка пакета "1 вакансия" и проведение заказа в админке и активация его на сайте
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.check_for_user_authorization()  # проверка на авторизацию пользователя
    page.go_to_personal_account_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    user_personal_account_page = UserPersonalAccountPage(browser, browser.current_url)
    user_personal_account_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
    services_and_prices_page.browser.execute_script("window.scrollBy(0, 500);")
    id_product = services_and_prices_page.adding_to_cart_1_vacancy_and_getting_product_id()  # добавление в корзину "1 вакансия" и получение id продукта
    services_and_prices_page.click_button_buy_in_basket()  # нажатие кнопки "Курить" в корзине
    services_and_prices_page.verification_of_message_after_purchase()  # проверка сообщения после покупки

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_order_page()  # переход на страницу заказов

    if language == "/ua":
        admin_page.search_for_user_orders_by_email_ua()  # поиск заказов пользователя по e-mail ua
    else:
        admin_page.search_for_user_orders_by_email_ru()  # поиск заказов пользователя по e-mail ru

    admin_page.order_processing()  # проведение заказа, изменение статуса заказа с "Новый" на "Проведенный"
    id_order = admin_page.getting_last_order_id_of_user()  # получение последнего id заказа пользователя

    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_user_purchases_page()  # переход на страницу "Покупки пользователей"
    id_purchase = admin_page.getting_id_of_purchase(id_order)  # получение id покупки

    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    # page.age_confirmation()  # подтверждение возраста больше 21 года
    # page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    # page.user_authorization()  # авторизация пользователя
    page.check_for_user_authorization()  # проверка на авторизацию пользователя
    page.go_to_personal_account_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    user_personal_account_page = UserPersonalAccountPage(browser, browser.current_url)
    user_personal_account_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
    # services_and_prices_page.switch_to_tab_Not_activated()  # переход на вкладку "Не активированные"
    services_and_prices_page.availability_of_product_in_not_activated_services(id_product, id_purchase)  # наличие "1 вакансия" в не активированных услугах
    services_and_prices_page.product_activation(id_purchase)  # активация продукта
    services_and_prices_page.product_availability_in_activated_services(id_product, id_purchase)  # наличие "1 вакансия" в активированных услугах

