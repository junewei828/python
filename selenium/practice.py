from selenium import webdriver
import unittest

# # driver = webdriver.Chrome()
# # driver.get("http://wwww.google.com")

# # elem = driver.find_element_by_name("q")
# # elem.send_keys("Hello WebDriver")
# # elem.submit()

# # print(driver.title)

# class FooBarTestCase(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     def setUp(self):
#         self.driver.get("http://travel.agileway.net")

#     def tearDown(self):
#         self.driver.find_element_by_link_text("Sign off").click()

#     def test_first_case(self):
#         self.assertEqual("Agile Travel", self.driver.title)
#         self.driver.find_element_by_name("username").send_keys("agileway")

#     def test_second_case(self):
#         self.driver.find_element_by_id("register_link").click()
#         self.assertIn("Register", self.driver.find_element_by_tag_name("body").text)


import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
