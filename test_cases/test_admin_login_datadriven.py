import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_admin_page import Login_admin_page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from utilities import excl_utils

class Test_02_Admin_Login_datadriven:
    admin_page_url = Read_config.get_admin_page_url()
    logger=Log_Maker.log_gen()
    path=".\\test_data\\admin_login_data.xlsx"
    status_list=[]


    
    def test_valid_admin_login_datadriven(self,setup):
         self.logger.info("******* login started************")
         self.driver= setup
         self.driver.implicitly_wait(10)
         self.driver.get(self.admin_page_url)
         self.admin_lp=Login_admin_page(self.driver)

         self.rows=excl_utils.get_row_count(self.path,"Sheet1")
         print("No of rows",self.rows)

         for r in range(2,self.rows+1):
             self.username=excl_utils.read_data(self.path,"Sheet1",r,1)
             self.password=excl_utils.read_data(self.path,"Sheet1",r,2)
             self.Exp_login=excl_utils.read_data(self.path,"Sheet1",r,3)
             self.admin_lp.enter_username(self.username)
             self.admin_lp.enter_password(self.password)
             self.admin_lp.click_login()
             time.sleep(5)
             act_title=self.driver.title
             org_title="My Account"

             if act_title==org_title:    #here if Title matches Test case pass
                 if self.Exp_login=="Yes": #login happend sucessfully
                     self.logger.info("Test data is passed") #Test data is passed
                     self.status_list.append("Pass")
                     self.admin_lp.logg_off()
                     self.driver.get(self.admin_page_url)
                 elif self.Exp_login=="No": #here if in data its 'NO' its doesn't logged inthe test is failed
                     self.logger.info("Test data is Failed")
                     self.status_list.append("Fail")
                     self.admin_lp.logg_off()
                     self.driver.get(self.admin_page_url)    
             elif act_title!=org_title:  #here if title doesn't matched staraight away the test data is faild
                if self.Exp_login=="Yes": #login happend  then also test is failed because title is not matched
                    self.logger.info("Test data failed")
                    self.status_list.append("Fail")
                elif self.Exp_login=="No":
                    self.logger.info("Test data is Passed")
                    self.status_list.append("Pass")
     
         print("Status list is",self.status_list) 
         if "Fail" in self.status_list:
             self.logger.info("The test data driven is Failed")
             assert False
         else:
             self.logger.info("The test data driven is Passed")
             assert True
                            






    

                    



         

         
      


  
                 
