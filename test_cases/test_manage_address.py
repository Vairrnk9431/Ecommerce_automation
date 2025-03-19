import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Manage_address import Manage_address_page
from base_pages.Login_admin_page import Login_admin_page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker

class Test_03_Manage_address:

    
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password =Read_config.get_password()
    First_Name=Read_config.get_First_Name()
    Last_name=Read_config.get_last_Name()
    comp_id=Read_config.get_comp()
    address=Read_config.get_address()
    city=Read_config.get_city()
    country=Read_config.get_country()
    region=Read_config.get_region()
    zip=Read_config.get_zip()
    logger=Log_Maker.log_gen()

    @pytest.mark.regression
    def test_manage_addrs(self,setup):
         
         self.logger.info("*******Test03 Addrs************")
         
         self.driver = setup
         self.driver.implicitly_wait(10)
         self.driver.get(self.admin_page_url)
         
         self.logger.info("*******Login start************")
         self.admin_lp=Login_admin_page(self.driver)
         self.admin_lp.enter_username(self.username)
         self.admin_lp.enter_password(self.password)
         self.admin_lp.click_login()
         self.driver.find_element(By.XPATH,"//ul[@class='nav-dash']/li[3]").click()
         self.driver.find_element(By.XPATH,"//a[@title='New Address']").click()
         

         self.logger.info("*******Addrs fields test start************")
         self.addrs_field=Manage_address_page(self.driver)
         self.addrs_field.enter_first_name(self.First_Name)
         self.addrs_field.enter_last_name(self.Last_name)
         self.addrs_field.enter_company_id(self.comp_id)
         self.addrs_field.enter_address_id(self.address)
         self.addrs_field.enter_city_id(self.city)
         self.addrs_field.enter_country_id(self.country)
         self.addrs_field.enter_region_State_id(self.region)
         self.addrs_field.enter_zip_code_id(self.zip)
         self.addrs_field.enter_default_addrs()
         self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

         title_after_continue=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success']").text
         if "Your address has been successfully inserted" in title_after_continue:
              self.logger.info("********Title matched**********")
              assert True
         else:
              self.logger.error("******** Address insertion failed **********")
              self.driver.close()
              assert False     



         
         

         
         

         




