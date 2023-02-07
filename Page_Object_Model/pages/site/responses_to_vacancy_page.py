from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ResponsesToVacancyPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResponsesToVacancyPage(BasePage):
    def checking_for_unread_response_flag(self):  # проверка наличия метки не прочитанного отклика
        assert self.is_element_present(*ResponsesToVacancyPageLocators.MARK_NOT_VIEWED_RESPONSE), "Нет метки не прочитанного отклика"

    def go_to_resume_page_of_response(self, resume_id):  # нажатие на резюме отклика для перехода на его страницу
        resume_locator = ResponsesToVacancyPageLocators()
        locators = resume_locator.assembly_of_locators_with_id_resume(resume_id)
        self.browser.find_element(*locators['resume_in_responses_to_vacancy']).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def deviation_of_response(self, resume_id, language):  # отклонение отклика
        resume_locator = ResponsesToVacancyPageLocators()
        locators = resume_locator.assembly_of_locators_with_id_resume(resume_id)
        self.browser.find_element(*locators['button_reject']).click()
        if language == "":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element(locators['status_response'], 'Вы отклонили это резюме'))
        elif language == "/ua":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element(locators['status_response'], 'Ви відхилили цю резюме'))
        elif language == "/en":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element(locators['status_response'], 'You can only leave one review for a company!'))
