import time

import pytest
#from Settings import driver,url
from PagesObject.Paaage_obj_practise import NOP
from PagesObject.LoginPaage_nop import Login_Paage

path=r"C:\\Users\\Manasa\\PycharmProjects\\pythonProject\\Screenshots"

class Test_NOP1():

    def test_homepage(self,setup,url):
        self.driver=setup
        self.driver.get(url)
        self.driver.maximize_window()
        nop_obj = NOP(setup)
        nop_obj.getUsername(' admin@yourstore.com')
        nop_obj.getPassword('admin')
        actual_title = self.driver.title
        print(actual_title)
        nop_obj.click_Login()
        nop_obj.click_Logout()
        self.driver.close()



    def test_activities(self,setup,url):
        self.driver=setup
        self.driver.get(url)
        self.driver.maximize_window()
        nop_obj = NOP(setup)
        nop_obj.getUsername(' admin@yourstore.com')
        nop_obj.getPassword('admin')
        nop_obj.click_Login()
        time.sleep(10)
        page_title=self.driver.title
        print(page_title)
        nop_obj.click_Logout()
        self.driver.close()

    def test_Homepage_activities(self,setup,url):
        self.driver=setup
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        nop_obj = NOP(setup)
        nop_obj.getUsername(' admin@yourstore.com')
        nop_obj.getPassword('admin')
        nop_obj.click_Login()
        time.sleep(10)
        lop_obj=Login_Paage(setup)
        lop_obj.homepage_activities()
        hmepage_title=self.driver.title
        print(hmepage_title)
        if hmepage_title == "Dashboard / nopCommerce administration":
            assert True

        else:
            self.driver.save_screenshot(path + "test_login2.png")
            print("incorrect page")
            self.driver.close()











