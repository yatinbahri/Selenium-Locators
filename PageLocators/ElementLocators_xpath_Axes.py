from selenium import webdriver


class Locators:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def xpath_axes(self):
        self.driver.get("https://money.rediff.com/gainers/bse/daily")

        # Self
        a = self.driver.find_element_by_xpath("//a[contains(text(),'Lotus Chocolate')]/self::a").text
        print(a)

        # Access Parent node

        a = self.driver.find_element_by_xpath("//a[contains(text(),'Lotus Chocolate')]/parent::td").text
        print ("\n" + a)

        # Child elements

        length = len(
            self.driver.find_elements_by_xpath("//a[contains(text(),'Lotus Chocolate')]/ancestor::tr//child::td"))
        print ("\nNumber of Child elements = {}".format(length))

        # Access Ancestor

        text = self.driver.find_element_by_xpath("//a[contains(text(),'Lotus Chocolate')]/ancestor::tr").text
        print(text)


    def teardown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    obj = Locators()
    obj.xpath_axes()
    obj.teardown()
