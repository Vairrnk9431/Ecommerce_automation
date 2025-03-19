import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_admin_page import Login_admin_page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password =Read_config.get_password()
    invalid_username =Read_config.get_invalid_username()
    logger=Log_Maker.log_gen()

   
    
    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("*******Test01 login************")
        self.logger.info("*******Verification of login page title************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Account Login"
        if act_title == exp_title:
            self.logger.info("*******Page title matched************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******Page title not matched************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
         self.logger.info("******* login started************")
         self.driver= setup
         self.driver.implicitly_wait(10)
         self.driver.get(self.admin_page_url)
         self.admin_lp=Login_admin_page(self.driver)
         self.admin_lp.enter_username(self.username)
         self.admin_lp.enter_password(self.password)
         self.admin_lp.click_login()

         
         act_dasboard_text=self.driver.find_element(By.XPATH,"//span[@class='subtext']").text
         if act_dasboard_text=="Kumar":
             self.logger.info("*******Title matched************")
             assert True
             self.driver.close()
         else:
            self.logger.info("*******Title not matched************")
            self.driver.save_screenshot(r".\screenshots\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
         self.logger.info("*******Valid login started************")
         self.driver= setup
         self.driver.implicitly_wait(10)
         self.driver.get(self.admin_page_url)
         self.admin_lp=Login_admin_page(self.driver)
         self.admin_lp.enter_username(self.invalid_username)
         self.admin_lp.enter_password(self.password)
         self.admin_lp.click_login()
         error_message=self.driver.find_element(By.XPATH,"//div[@class='alert alert-error alert-danger']").text
         print("error...",error_message)
         if error_message.__contains__("Error: Incorrect login or password provided."):
             self.logger.info("*******Title not matched************")
             assert True
             self.driver.close()
         else:
             self.driver.close()
             assert False
                 
