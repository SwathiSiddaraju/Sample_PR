# from selenium import webdriver
# import pytest
#
# class Test_fixture:
#
#     @pytest.fixture()
#     def method1(self):
#         global driver
#         driver = webdriver.Chrome(executable_path="C:\\Users\\Swathi S\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
#         driver.get("http://google.com")
#
#     def test_method2(self,method1):
#         driver.find_element_by_xpath("//div[@id='tophf']/following-sibling::div/div/div[3]//input[@value='Google Search']").click()
#         # driver.find_element_by_xpath("// div[ @ id = 'tophf'] / following - sibling::div / div / div[3] // input[ @ value = 'I'm Feeling Lucky']").click()
#         # driver.close()



print("hello world")

def tyield():
    a=1
    print(a,"before operation")
    a+=1
    print(a,"after optn")
    yield a
    print(a)
tyield()