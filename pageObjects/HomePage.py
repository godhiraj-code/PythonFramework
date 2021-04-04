from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    autoPopUp = (By.CSS_SELECTOR, "[class*='autopop']")
    modalLogIn = (By.CSS_SELECTOR, "[class*='modalLogin']")
    cityClick = (By.ID, "city")
    cityEditBox = (By.XPATH, "//input[contains(@placeholder,'Enter city')]")
    listOfCities = (By.XPATH, "//li[@role='option']//p")
    cityBoxAfterSelecting = (By.XPATH, "//*[@id='city']")
    firstdatePickerPopUp = (By.CSS_SELECTOR, "[class*='DayPicker-Day--selected']")
    seconddatePickerPopUp = (By.XPATH, "(//*[contains(@class,'DayPicker-Day--selected')])[2]")
    clearDatePickerPopUp = (By.XPATH, "//div[@class='hsBackDrop']")
    searchButton = (By.ID, "hsw_search_button")

    def city(self):
        return self.driver.find_element(*HomePage.cityClick)

    def pop_up(self):
        return self.driver.find_element(*HomePage.autoPopUp)

    def modal_login(self):
        return self.driver.find_element(*HomePage.modalLogIn)

    def city_edit_box(self):
        return self.driver.find_element(*HomePage.cityEditBox)

    def city_lists(self):
        return self.driver.find_elements(*HomePage.listOfCities)

    def city_after_selecting(self):
        return self.driver.find_element(*HomePage.cityBoxAfterSelecting)

    def date_picker_pop_up(self):
        return self.driver.find_element(*HomePage.firstdatePickerPopUp)

    def date_picker_return(self):
        return self.driver.find_element(*HomePage.seconddatePickerPopUp)

    def clear_date_picker_pop_up(self):
        return self.driver.find_element(*HomePage.clearDatePickerPopUp)

    def search_button(self):
        return self.driver.find_element(*HomePage.searchButton)
