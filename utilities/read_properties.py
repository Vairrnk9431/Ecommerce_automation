import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Read_config():
    @staticmethod
    def get_admin_page_url():
        url=config.get('admin login info','admin_page_url')
        return url
    
    @staticmethod
    def get_username():
        username=config.get('admin login info','username')
        return username
    
    @staticmethod
    def get_password():
        password=config.get('admin login info','password')
        return password
    
    @staticmethod
    def get_invalid_username():
        invalid_username=config.get('admin login info','invalid_username')
        return invalid_username
    
    @staticmethod
    def get_First_Name():
        First_Name=config.get('admin login info','First_Name')
        return First_Name

    @staticmethod
    def get_last_Name():
        Last_name=config.get('admin login info','Last_name')
        return Last_name
    
    @staticmethod
    def get_comp():
        comp_id=config.get('admin login info','comp_id')
        return comp_id
    
    @staticmethod
    def get_address():
        address=config.get('admin login info','address')
        return address
    
    @staticmethod
    def get_city():
        city=config.get('admin login info','city')
        return city
    @staticmethod
    def get_country():
        country=config.get('admin login info','country')
        return country
    
    @staticmethod
    def get_region():
        region=config.get('admin login info','region')
        return region
    
    @staticmethod
    def get_zip():
        zip=config.get('admin login info','zip')
        return zip



