class NOP():

    def __init__(self,driver):
        self.driver=driver

    username = '//input[@name="Email"]'
    password = '//input[@name="Password"]'
    loginbutton = '//input[@value="Log in"]'
    logoutbutton = '//a[text()="Logout"]'


    # def launch_url(self):
    #     self.driver.get(url[0])
    #     self.driver.maximize_window()
    def getUsername(self,username):
        self.driver.find_element_by_xpath(self.username).clear()
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def getPassword(self,password):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_Login(self):
        self.driver.find_element_by_xpath(self.loginbutton).click()

    def click_Logout(self):
        self.driver.find_element_by_xpath(self.logoutbutton).click()

    # def all_activites(self):
    #     self.getUsername()
    #     self.getPassword()
    #     self.click_Login()
    #     self.click_Logout()

# nop_obj=NOP(driver)
# nop_obj.all_activites()

