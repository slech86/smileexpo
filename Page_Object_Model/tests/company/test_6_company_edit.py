from Page_Object_Model.data_for_testing import UrlStartPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_edit_page import CompanyEditPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage



def test_changing_all_company_data(browser, language):  # изменение всех данных компании
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

    company_edit_page = CompanyEditPage(browser, browser.current_url)
    company_edit_page.change_data_in_all_fields(language)  # изменение данных во всех полях
    company_edit_page.submitting_form_for_moderation_after_changing_data()  # отправка формы на регистрацию
    company_edit_page.checking_message_after_saving_changes_to_personal_information()  # проверка сообщения после сохранения изменений личной информации