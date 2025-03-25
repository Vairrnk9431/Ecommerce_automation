
from selenium.webdriver.common.by import By


class Login_admin_page:
    textbox_username_id="loginFrm_loginname"
    textbox_password_id="loginFrm_password"
    btn_login_xpath="//button[@title='Login']"
    loggoff_xpath="//ul[@class='side_account_list']/li[10]"
    # after_logout_continue_xpath="//a[@title='Continue']"
    # login_link_text="Login or register"


    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def logg_off(self):
          self.driver.find_element(By.XPATH,self.logg_off).click()
        #   self.driver.find_element(By.XPATH,self.after_logout_continue_xpath).click()
        #   self.driver.find_element(By.LINK_TEXT,self.login_link_text).click()

       










