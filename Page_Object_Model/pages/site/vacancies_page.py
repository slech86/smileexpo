from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import VacanciesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.singleton import Singleton
import time


class VacanciesPage(BasePage):
    def search_vacancy_by_job_title(self):  # поиск вакансии по названию
        self.browser.find_element(*VacanciesPageLocators.FIELD_JOB_TITLE_TO_SEARCH).send_keys(TestDataEditing.job_title_vacancy)
        self.browser.find_element(*VacanciesPageLocators.BUTTON_SEARCH).click()

    def go_to_vacancy_page(self):  # нажатие на блок вакансии для перехода на ее страницу
        vacancy_locator = VacanciesPageLocators()
        vacancy = vacancy_locator.assembly_of_locators_with_id_vacancies()
        self.browser.find_element(*vacancy).click()