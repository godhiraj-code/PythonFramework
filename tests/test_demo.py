import time

import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test(BaseClass):
    def test_demo(self):
        log = self.getLogger()
        log.info("Demo Test Execution starting")
        home_page = HomePage(self.driver)
        try:
            log.info("Clicking the city box in MakeMyTrip.com hotels page")
            home_page.city().click()
        except Exception as e:
            log.warning("Not able to click the city box")
            #print("Not able to click the link , try again clicking")

        #time.sleep(3)
        try:
            if home_page.pop_up().is_displayed():
                log.info("login pop up displayed, clearing the login pop up")
                home_page.modal_login().click()
                log.info("Clicking the city box in MakeMyTrip.com hotels page")
                home_page.city().click()
        except Exception as e:
            log.warning("No Login pop up displayed")
            #print("No autopop up element found ", e)

        # driver.find_element_by_id("city").click()
        time.sleep(3)
        log.info("entering first 5 chars of a city in city suggestion box")
        self.inputData(home_page.city_edit_box(), "Northern Areas")
        time.sleep(5)
        log.info("finding the total number of cities suggested and searching for the desired one")
        cities = home_page.city_lists()

        for city in cities:
            if city.text == "Northern Areas, Australia":
                log.info("clicking the desired city Northern Areas, Australia")
                city.click()
                break

        time.sleep(3)
        assert home_page.city_after_selecting().get_attribute("value") in "Northern Areas, Australia"
        assert home_page.city_after_selecting().get_attribute("value") in "NEWZEALAND"

        time.sleep(3)

