"""
this file is for building complex interactions
it can be used as building blocks in the front_end_automation
,and it consists of multiple single interactions

"""
from interactions_single import SingleInteractions


class CompoundInteractions:

    @staticmethod
    def login(driver, url, username, password):
        driver.get(url)
        SingleInteractions.insert_login_username(driver, username)
        SingleInteractions.insert_login_password(driver, password)
        SingleInteractions.click_login(driver)
        SingleInteractions.wait_for_active_workspace_name_to_be_displayed(driver)

