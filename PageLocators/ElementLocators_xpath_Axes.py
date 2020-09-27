from selenium import webdriver
import time


class Locators:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def xpath_axes(self):
        self.driver.get("https://money.rediff.com/gainers/bse/daily")

        # Self - Selects the current node
        a = self.driver.find_element_by_xpath("//a[contains(text(),'Ashok Leyland')]/self::a").text
        print(a)

        # Access Parent node - Selects parent of the current node

        a = self.driver.find_element_by_xpath("//a[contains(text(),'Ashok Leyland')]/parent::td").text
        print ("\n" + a)

        # Child elements - Selects children of the current node

        length = len(
            self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr//child::td"))
        print ("\nNumber of Child elements = {}".format(length))

        # Access Ancestor - Selects all ancestors of the current node (Parent and grand parent)

        text = self.driver.find_element_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr").text
        print(text)

        # Descendants of Ancestor - # Selects all descendants (children and grand children)

        descendants = []
        descendants = self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr/descendant::*")

        print(descendants)

        # for only child elements
        self.driver.find_elements_by_xpath(
            "//a[contains(text(),'Ashok Leyland')]/ancestor::tr/descendant::td")  # Includes only child element (5)

        # Following Node - Selects all the following node from current node

        number = len(self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr/following::tr"))
        print ("\nNumber of following node = {} ".format(number))

        # Following Sibling - Selects only the following siblings from current node

        number = len(self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr/following-sibling::tr"))

        print ("\n Number of following Sibling nodes = {}".format(number))
        # Preceding nodes

        number = len(self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr/preceding::tr"))
        print ("\n Number of Preceding nodes = {}".format(number))

        number = len(self.driver.find_elements_by_xpath("//a[contains(text(),'Ashok Leyland')]/ancestor::tr/preceding-sibling::tr"))
        print ("\n Number of Preceding Siblings nodes = {}".format(number))


        # Find sign-up button from Facebook registration form using Child

        self.driver.get("https://www.facebook.com/")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'English (UK)')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='u_0_2']").click()
        time.sleep(2)

        if self.driver.find_element_by_xpath("//div[@id='reg_form_box']/child::div[10]/button"):
            assert True
        else:
            assert False

        # Find FirstName field using signup button on FB registration form (Parent)

        self.driver.find_element_by_xpath(
            "//button[@id='u_7_s']/parent::*/parent::*/child::div[1]/div/div[1]").send_keys("FirstBame")

        # Identify the password from mobile number field (Following)

        self.driver.find_element_by_xpath("//input[@id='u_7_g']/following::input[2]").send_keys("Password")

        # Identify the mobile number from password field (preceding)

        self.driver.find_element_by_xpath("//input[@id='password_step_input']/preceding::input[10]").send_keys("01234567897")

        # Locate Surname from female radio button using Ancestor

        self.driver.find_element_by_xpath("//input[@id='u_7_2']/ancestor::div[2]/div[1]/div/div[2]").send_keys("SurName")

        # or use below as identifier

        self.driver.find_element_by_xpath("//input[@id='u_7_2']/ancestor::div[2]//input[@id='u_7_d']").clear()








    def teardown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    obj = Locators()
    obj.xpath_axes()
    obj.teardown()
