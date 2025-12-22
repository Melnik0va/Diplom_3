from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from data import TIMEOUT

class BasePage: 

    def __init__ (self, driver):
        self.driver = driver

    def wait_loading(self, locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def open_url(self, locator, url): 
        self.driver.get(url)
        self.wait_loading(locator)

    def click_to_element(self, locator_1, locator, timeout=TIMEOUT):
        self.wait_loading(locator_1)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()
    
    def find_element_with_wait(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def add_text_to_element(self, locator, text, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).send_keys(text)

    
    def get_attribute(self, locator, attribute, timeout=TIMEOUT):
        return (WebDriverWait(self.driver, timeout).
                until(EC.visibility_of_element_located(locator)).get_attribute(attribute))

    def get_visible_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until((EC.visibility_of_element_located(locator)))
    
    def get_visible_elements(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until((EC.visibility_of_all_elements_located(locator)))
    
    def check_invisible_element(self, locator, timeout=TIMEOUT): 
        element = self.driver.find_element(*locator)
        return element.is_displayed()
    
    def drag_and_drop(self, source_drag, target_drop):
        drag_and_drop(self.driver, source_drag, target_drop)