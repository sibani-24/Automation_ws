# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# class BaseSetup:
#     @pytest.fixture(autouse=True)
#     def precondition(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://www.google.com")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         self.wait=WebDriverWait(self.driver,10)
#
#     @pytest.fixture(autouse=True)
#     def postcondition(self):
#         yield
#         self.driver.quit()
        
print("--------------------------")        
        
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from pyjavaproperties import Properties
#
# class BaseSetup:
#     @pytest.fixture(autouse=True)
#     def precondition(self):
#         pptobj=Properties()
#         pptobj.load(open('../config.properties'))
#
#         browser=pptobj['BROWSER'].lower()
#         appurl=pptobj['APPURL']
#
#         ito=pptobj['IMPLICIT_TIME_OUT']
#
#         eto=pptobj['EXPLICIT_TIME_OUT']
#
#         if browser=='chrome':
#             self.driver=webdriver.Chrome()
#
#         elif browser=='firefox':
#             self.driver=webdriver.Firefox()
#
#         else:
#             self.driver=webdriver.Edge()
#
#         self.driver.get(appurl)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(ito)
#         self.wait=WebDriverWait(self.driver,eto)
#
#     @pytest.fixture(autouse=True)
#     def postcondition(self):
#         yield
#         self.driver.quit()
        
print("--------------------------")          
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from pyjavaproperties import Properties
#
# class BaseSetup:
#     @pytest.fixture(autouse=True)
#     def precondition(self):
#         pptobj=Properties()
#         pptobj.load(open('../config.properties'))
#
#         browser=pptobj['BROWSER'].lower()
#         print("Browser",browser)
#         appurl=pptobj['APPURL']
#         print("AppURL",appurl)
#         ito=pptobj['IMPLICIT_TIME_OUT']
#         print("ITO",ito)
#         eto=pptobj['EXPLICIT_TIME_OUT']
#         print("ETO",eto)
#         print("Executing in local system")
#         if browser=='chrome':
#             print("Open chrome browser")
#             self.driver=webdriver.Chrome()
#
#         elif browser=='firefox':
#             print("Open firefox browser")
#             self.driver=webdriver.Firefox()
#
#         else:
#             print("Open edge browser")
#             self.driver=webdriver.Edge()
#         print("Enter the URL",appurl)    
#         self.driver.get(appurl)
#         print("Maximize the browser")
#         self.driver.maximize_window()
#         print("Set ito",ito,'seconds')
#         self.driver.implicitly_wait(ito)
#         print("Set eto",eto,'seconds')
#         self.wait=WebDriverWait(self.driver,eto)
#
#     @pytest.fixture(autouse=True)
#     def postcondition(self):
#         yield
#         print("Close the browser")
#         self.driver.quit()
        
print("--------------------------")          
from pyjavaproperties import Properties
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        pptobj=Properties()
        pptobj.load(open('config.properties'))
        
        self.xl_path=pptobj['XL_PATH']
        print("XL Path",self.xl_path)
        gridurl=pptobj['GRIDURL']
        print("Grid URL",gridurl)
        
        usegrid=pptobj['USERGRID'].lower()
        print("Use Grid",usegrid)
        browser=pptobj['BROWSER'].lower()
        print("Browser",browser)
        appurl=pptobj['APPURL']
        print("AppURL",appurl)
        ito=pptobj['IMPLICIT_TIME_OUT']
        print("ITO",ito)
        eto=pptobj['EXPLICIT_TIME_OUT']
        print("ETO",eto)
        if usegrid=='yes':
            print("Executing in remote system")
            if browser=='chrome':
                print("Open chrome browser")
                self.driver = webdriver.Remote(command_executor=gridurl,options=webdriver.ChromeOptions())
                
            elif browser=='firefox':
                print("Open firefox browser")
                self.driver = webdriver.Remote(command_executor=gridurl,options=webdriver.FirefoxOptions())
                
            else:
                print("Open edge browser")
                self.driver = webdriver.Remote(command_executor=gridurl,options=webdriver.EdgeOptions())
                
        else:
            print("Executing in local system")
            if browser=='chrome':
                print("Open chrome browser")
                self.driver=webdriver.Chrome()
            
            elif browser=='firefox':
                print("Open firefox browser")
                self.driver=webdriver.Firefox()
                
            else:
                print("Open edge browser")
                self.driver=webdriver.Edge()
        print("Enter the URL",appurl)    
        self.driver.get(appurl)
        print("Maximize the browser")
        self.driver.maximize_window()
        print("Set ito",ito,'seconds')
        self.driver.implicitly_wait(ito)
        print("Set eto",eto,'seconds')
        self.wait=WebDriverWait(self.driver,eto)
        
    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.quit()
        
    
        
    
        
    