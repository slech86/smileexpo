from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData


class JobSeekerRegistrationPageLocators():
    inputPrefix = 'jobseekerregistrationform-'

    FIELD_LOGIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'login'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'password'))
    FIELD_REPEAT_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'repeatpassword'))
    # блок "Данные для авторизации"

    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayy > option:nth-child(4)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdaym > option:nth-child(12)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayd > option:nth-child(31)'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="2"] + .radio-custom'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(2)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(8)'))
    # блок "Личная информация"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#button-registration'))


class JobSeekerEditPageLocators():
    inputPrefix = 'jobseekereditform-'

    BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#personal-information .post-resume-title + .btn-edit'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayy > option:nth-child(2)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdaym > option:nth-child(2)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayd > option:nth-child(2)'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="1"] + .radio-custom'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(4)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(5)'))
    # блок "Личная информация"

    BUTTON_EDIT_IN_SETTINGS_BLOCK = (By.CSS_SELECTOR, ('#other-settings .post-resume-title + .btn-edit'))
    DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'mail_language"]'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="0"]'))  # русский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="1"]'))  # украинский
    # блок "Настройки"

    BUTTON_SAVE_CHANGES = (By.CSS_SELECTOR, ('#submit-publish'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации


class JobSeekerPersonalCabinetPageLocators():
    MY_RESUME = (By.XPATH, ('//a[contains(@href, "/resume/my")]/div[@class="employer-card"]'))
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/job-seeker/edit")]/div[@class="employer-card"]'))


class MyResumePageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_ADD_RESUME = (By.CSS_SELECTOR, ('.btn-wrap > .btn.btn-blue'))

    INFO_TEXT_AFTER_SUBMITTING_RESUME_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после отправки резюме на модерацию
    CROSS_IN_POP_UP_AFTER_SUBMITTING_RESUME_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после отправки резюме на модерацию


class AddResumePageLocators():
    inputPrefix = 'resumeaddform-'

    FIELD_PHOTO = (By.CSS_SELECTOR, ('#' + inputPrefix + 'photo'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))

    DROPDOWN_YEAR = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'birthdayy"]'))
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'birthdayy [data-original-index="21"]'))
    DROPDOWN_MONTH = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'birthdaym"]'))
    MONTH_SEPTEMBER = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'birthdaym [data-original-index="9"]'))
    DROPDOWN_DAY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'birthdayd"]'))
    DAY_5 = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'birthdayd [data-original-index="5"]'))

    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="2"] + .radio-custom'))

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_UKRAINE = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'country_id [data-original-index="1"]'))
    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITI_ODESSA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'city_id [data-original-index="14"]'))
    DROPDOWN_WILLING_TO_RELOCATE = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'willing_relocate"]'))
    NOT_READY_TO_RELOCATE = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'willing_relocate [data-original-index="2"]'))
    # блок "Личная информация"

    FIELD_PHONE_1 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    BUTTON_ADD_PHONE = (By.CSS_SELECTOR, ('.show-addBtn .addPhone'))
    FIELD_PHONE_2 = (By.CSS_SELECTOR, ('#resume-phone-add1'))

    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    FIELD_PORTFOLIO = (By.CSS_SELECTOR, ('#' + inputPrefix + 'portfolio'))

    BUTTON_FACEBOOK = (By.CSS_SELECTOR, ('[aria-controls="facebookCollapse"]'))
    BUTTON_LINKEDIN = (By.CSS_SELECTOR, ('[aria-controls="lnCollapse"]'))
    BUTTON_INSTAGRAM = (By.CSS_SELECTOR, ('[aria-controls="inCollapse"]'))
    BUTTON_TELEGRAM = (By.CSS_SELECTOR, ('[aria-controls="telCollapse"]'))
    BUTTON_TWITTER = (By.CSS_SELECTOR, ('[aria-controls="twCollapse"]'))
    BUTTON_VK = (By.CSS_SELECTOR, ('[aria-controls="vkCollapse"]'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'facebook'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'linkedin'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'instagram'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'telegram'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'twitter'))
    FIELD_VK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'vk'))
    # блок "Контактная информация"

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    CATEGORY_RESUME = "document.getElementsByName('ResumeAddForm[category_id][]')[7].click()"
    SUBCATEGORIES = (By.CSS_SELECTOR, ('[for="subcategories_id-70"]'))
    DISTANT_WORK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'employment > .checkbox:nth-child(3) > label'))  # удаленная работа
    SALARY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'salary'))
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'currency"]'))
    CURRENCY_UAH = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'currency [data-original-index="1"]'))
    # блок "Желаемая должность"

    BUTTON_ADD_SKILLS = (By.CSS_SELECTOR, ('#addSkill'))
    IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, ('#cke_resumeaddform-skills iframe'))
    # блок "Навыки и достижения"

    BUTTON_ADD_WORK_EXPERIENCE = (By.CSS_SELECTOR, ('#addExperiencel'))
    FIELD_COMPANY_NAME = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[1]//input[contains(@id, "resumeworkexperienceform")]'))
    FIELD_SITE_COMPANY = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[2]//input[contains(@id, "resumeworkexperienceform")]'))
    SCOPE_OF_COMPANY_CASINO_STAFF = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//div[contains(@id, "resumeworkexperienceform")]//div[@class="custom-control checkbox"][3]/label'))
    FIELD_POSITION = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[4]//input[contains(@id, "resumeworkexperienceform")]'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_AUGUST_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[9]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[6]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_MARCH_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[6]//iframe'))

    BUTTON_ADD_WORK_EXPERIENCE_2 = (By.CSS_SELECTOR, ('.resume-item-link.js-add-work-place'))
    FIELD_COMPANY_NAME_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[1]//input[contains(@id, "resumeworkexperienceform")]'))
    FIELD_SITE_COMPANY_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[2]//input[contains(@id, "resumeworkexperienceform")]'))
    SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//div[contains(@id, "resumeworkexperienceform")]//div[@class="custom-control checkbox"][6]/label'))
    FIELD_POSITION_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[4]//input[contains(@id, "resumeworkexperienceform")]'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_APRIL_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    WORKING_NOW_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[2]/a'))
    # DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    # YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[6]//iframe'))
    # блок "Опыт работы"

    DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'gambling_experience"]'))
    WITHOUT_EXPERIENCE = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'gambling_experience [data-original-index="1"]'))
    # блок "Опыт работы в игорной идустрии"

    BUTTON_ADD_EDUCATION = (By.CSS_SELECTOR, ('#addEducation'))
    FIELD_NAME_OF_INSTITUTION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[1]//input[contains(@id, "resumeeducationform")]'))
    DROPDOWN_LEVEL_OF_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[2]//button'))
    HIGHER_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[2]//li[2]/a'))

    DROPDOWN_COUNTRY_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[3]//button'))
    COUNTRY_UKRAINE_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[3]//li[2]/a'))
    DROPDOWN_CITI_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[4]//button'))
    CITI_KHARKOV_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[4]//li[24]/a'))

    FIELD_DEPARTMENT_AND_SPECIALITY = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[5]//input[contains(@id, "resumeeducationform")]'))

    DROPDOWN_MONTH_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_SEPTEMBER_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[10]/a'))
    DROPDOWN_YEAR_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[14]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_MAY_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[7]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[9]/a'))

    BUTTON_ADD_EDUCATION_2 = (By.CSS_SELECTOR, ('.resume-item-link.js-add-education'))
    FIELD_NAME_OF_INSTITUTION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[1]//input[contains(@id, "resumeeducationform")]'))
    DROPDOWN_LEVEL_OF_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[2]//button'))
    SECONDARY_SPECIAL_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[2]//li[4]/a'))

    DROPDOWN_COUNTRY_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[3]//button'))
    COUNTRY_BELARUS_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[3]//li[5]/a'))
    DROPDOWN_CITI_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[4]//button'))
    CITI_MINSK_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[4]//li[6]/a'))

    FIELD_DEPARTMENT_AND_SPECIALITY_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[5]//input[contains(@id, "resumeeducationform")]'))

    DROPDOWN_MONTH_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_NOVEMBER_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[12]/a'))
    DROPDOWN_YEAR_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[6]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JANUARY_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[3]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[4]/a'))
    # блок "Образование"

    BUTTON_ADD_COURSES_AND_CERTIFICATES = (By.CSS_SELECTOR, ('#addCourses'))
    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[1]//input[contains(@id, "resumecourseform")]'))

    DROPDOWN_MONTH_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JUNE_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[7]/a'))
    DROPDOWN_YEAR_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    DROPDOWN_MONTH_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JUNE_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[8]/a'))
    DROPDOWN_YEAR_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[3]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[3]//iframe'))

    BUTTON_ADD_COURSES_AND_CERTIFICATES_2 = (By.CSS_SELECTOR, ('.resume-item-link.js-add-courses'))
    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[1]//input[contains(@id, "resumecourseform")]'))

    DROPDOWN_MONTH_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_OCTOBER_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[11]/a'))
    DROPDOWN_YEAR_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[10]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_OCTOBER_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[9]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[3]//iframe'))
    # блок "Курсы и сертификаты"

    BUTTON_ADD_LANGUAGE = (By.CSS_SELECTOR, ('#addLanguages'))
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-language"]'))
    POLISH_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-language [data-original-index="34"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-level"]'))
    HIGH_LEVEL_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-level [data-original-index="5"]'))

    BUTTON_ADD_LANGUAGE_2 = (By.CSS_SELECTOR, ('.resume-item-link.js-add-languages'))
    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-language"]'))
    GERMAN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-language [data-original-index="4"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-level"]'))
    FREE_LEVEL_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-level [data-original-index="6"]'))
    # блок "Знание языков"

    RADIO_I_DONT_HAVE_DISABILITY = (By.CSS_SELECTOR, ('#disability #resumeaddform-disability > label:nth-child(1) > input'))
    I_HAVE_DISABILITY = (By.CSS_SELECTOR, ('#disability #resumeaddform-disability > label:nth-child(2)'))
    # блок "Инвалидность"

    BUTTON_ADD_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#addAdd'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_resumeaddform-additionally_information iframe'))
    # блок "Дополнительная информация"

    DROPDOWN_JOB_SEARCH_STATUS = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'job_search_status"]'))
    ACTIVELY_LOOKING_FOR_JOB = (By.CSS_SELECTOR, ('#resume-visibility-settings li[data-original-index="2"] > a'))
    # блок "Статус поиска работы"

    RESUME_COMPLETED_ON = (By.CSS_SELECTOR, ('.post-resume-status span.resume-rate'))
    STATUS_OF_YOUR_RESUME = (By.CSS_SELECTOR, ('.post-resume-status span.small-text.d-block'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков

    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-button'))