from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_001(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_001, self).__init__(driver)

    def set_search(self, email):
        wait = WebDriverWait(self.driver, 60)
        setSearch = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
        setSearch.send_keys(email)
