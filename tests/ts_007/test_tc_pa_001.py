import allure

from BasePage.BasePage import BasePage
from Pages.tc_pa_001 import tc_pa_001


class AIAnalyzer(BasePage):
    @allure.step("FNO Login into bpusa website")
    def test_tc_pa_001(self):
        tc_pa = tc_pa_001(self.driver)
        tc_pa.set_search("Zdaly Inc")
