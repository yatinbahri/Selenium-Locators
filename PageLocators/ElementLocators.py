from selenium import webdriver
import time


class Locators:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def locators_test(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(5)

        # id
        self.driver.find_element_by_id("search_query_top").send_keys("Hello")

        # name
        self.driver.find_element_by_name("search_query").clear()
        self.driver.find_element_by_name("search_query").send_keys("How are you")

        # link_text
        if self.driver.find_element_by_link_text("Faded Short Sleeve T-shirts"):
            print("\nElement is present")
        else:
            assert False

        # class_name
        element_count = len(self.driver.find_elements_by_class_name("homeslider-container"))
        print("\nTotal Slider Elements = {}".format(element_count))

        # tag_name
        element_count = len(self.driver.find_elements_by_tag_name("a"))
        print("\nTotal Links in the page = {}".format(element_count))

        # css_selector

        self.driver.get("http://www.facebook.com")

        # ID = css_selector("#id")
        self.driver.find_element_by_css_selector("#email").send_keys("username_id")

        # Class = css_selector(".class")
        self.driver.find_element_by_css_selector(".inputtext").clear()
        self.driver.find_element_by_css_selector(".inputtext").send_keys("username_class")
        time.sleep(2)

        # Attribute = css_selector("[Attribute=value]")
        self.driver.find_element_by_css_selector("[name=email]").clear()
        self.driver.find_element_by_css_selector("[name=email]").send_keys("username_attribute")
        time.sleep(2)

        # Combination 1 - Tag and Id = "Tag#ID"
        self.driver.find_element_by_css_selector("input#email").clear()
        self.driver.find_element_by_css_selector("input#email").send_keys("username_comb_tag_id")
        time.sleep(2)

        # Combination 2 - Tag and Class = "Tag.class"
        self.driver.find_element_by_css_selector("input.inputtext").clear()
        self.driver.find_element_by_css_selector("input.inputtext").send_keys("username_comb_tag_class")
        time.sleep(2)

        # Combination 3 - Tag and Attribute = "Tag[attribute= value]"
        self.driver.find_element_by_css_selector("input[name=email]").clear()
        self.driver.find_element_by_css_selector("input[name=email]").send_keys("username_comb_tag_attribute")
        time.sleep(2)

        # Combination 4 - Tag, Class and Attribute

        self.driver.find_element_by_css_selector("input.inputtext[data-testid=royal_email").clear()
        self.driver.find_element_by_css_selector("input.inputtext[data-testid=royal_email").send_keys(
            "username_comb_tag_class_attribute")
        time.sleep(2)
        self.driver.find_element_by_css_selector("input.inputtext[data-testid=royal_pass").send_keys(
            "password_comb_tag_class_attribute")
        time.sleep(2)

        # xpath
        # Relative xpath = //tagname[@attribute='value']

        if self.driver.find_element_by_xpath("//input[@data-testid='royal_email']"):
            assert True
        else:
            assert False

        if self.driver.find_element_by_xpath("//*[@data-testid='royal_email']"):
            assert True
        else:
            assert False

        # Options can be used with xpath

        # Xpath with "or" operator

        self.driver.find_element_by_xpath("//input[@id='email' or @data-testid='royal_email']").clear()
        self.driver.find_element_by_xpath("//input[@id='email' or @data-testid='royal_email']").send_keys("Using Or")

        # Xpath with "and" operator

        self.driver.find_element_by_xpath("//input[@id='email' and @data-testid='royal_email']").clear()
        self.driver.find_element_by_xpath("//input[@id='email' and @data-testid='royal_email']").send_keys("Using And")

        # Xpath with "contains()" operator # //tagname[contains(@attribute,'value')]

        self.driver.find_element_by_xpath("//input[contains(@id,'email')]").clear()
        self.driver.find_element_by_xpath("//input[contains(@id,'email')]").send_keys("Using Contains method")

        # Xpath with "starts-with()" operator # //tagname[contains(@attribute,'value')]

        self.driver.find_element_by_xpath("//input[starts-with(@id,'ema')]").clear()
        self.driver.find_element_by_xpath("//input[starts-with(@id,'ema')]").send_keys("Using starts-with method")

        # Xpath with "text()" operator # //tagname[@text='text')]

        if self.driver.find_element_by_xpath("//a[text()='Create New Account']"):
            assert True
        else:
            assert False

        # Xpath with "chained xpath" operator # //tagname[@attribute='value')]//[@attribute='value']

        self.driver.find_element_by_xpath("//div[@class='_6ltg']//button[text()='Log In']").click()



    def teardown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    obj = Locators()
    obj.locators_test()
    obj.teardown()
