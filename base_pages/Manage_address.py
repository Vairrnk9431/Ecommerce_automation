
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Manage_address_page:
    First_name_id="AddressFrm_firstname"
    Last_Name_id="AddressFrm_lastname"
    Company_id="AddressFrm_company"
    Address_1_id="AddressFrm_address_1"
    City_id="AddressFrm_city"
    Country_id="AddressFrm_country_id"
    Region_State_id="AddressFrm_zone_id"
    zip_Code_id="AddressFrm_postcode"


    def __init__(self,driver):
        self.driver=driver

    def enter_first_name(self,First_Name):
        self.driver.find_element(By.ID,self.First_name_id).send_keys(First_Name)

    def enter_last_name(self,Last_name):
        self.driver.find_element(By.ID,self.Last_Name_id).send_keys(Last_name)

    def enter_company_id(self,comp_id):
        self.driver.find_element(By.ID,self.Company_id).send_keys(comp_id)   

    def enter_address_id(self,address):
        self.driver.find_element(By.ID,self.Address_1_id).send_keys(address)

    def enter_city_id(self,city):
        self.driver.find_element(By.ID,self.City_id).send_keys(city)    

    def enter_country_id(self,country):
        select_country=self.driver.find_element(By.ID,self.Country_id)
        select_country=Select(select_country)
        select_country.select_by_visible_text(country)   

    def enter_region_State_id(self,region):
        Select_region=self.driver.find_element(By.ID,self.Region_State_id)
        Select_region=Select(Select_region)
        Select_region.select_by_visible_text(region)


    def enter_zip_code_id(self,zip):
        self.driver.find_element(By.ID,self.zip_Code_id).send_keys(zip)

    def enter_default_addrs(self):
        self.driver.find_element(By.XPATH,'//label[@for="AddressFrm_default1"]').click()         
    
        


