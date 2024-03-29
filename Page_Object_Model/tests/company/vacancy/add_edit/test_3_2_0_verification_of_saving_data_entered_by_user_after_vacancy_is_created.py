import pytest
from Page_Object_Model.configuration import UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.users import users_variables
from Page_Object_Model.tests.company.vacancy import _resources_vacancy


def test_verification_of_saving_data_entered_by_user_after_vacancy_is_created(browser):  # проверка сохранения введенных пользователем данных после создания вакансии
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title(TestData.job_title_vacancy)  # поиск вакансии по названию должности
    admin_page.go_to_object_editing_page()  # переход на страницу редактирования вакансии

    admin_vacancy_edit_page = AdminVacancyEditPage(browser, browser.current_url)
    admin_vacancy_edit_page.verification_of_saving_data_entered_by_user_after_vacancy_is_created_ru(users_variables[_resources_vacancy.user_vacancy]["login"])  # проверка сохранения введенных пользователем данных после создания вакансии RU
