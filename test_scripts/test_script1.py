# from generic.base_setup import BaseSetup
#
# class TestScript1(BaseSetup):
#     def test_script1(self):
#         print("This is test script 1")
#         print(self.driver.title)

print("--------------------------")  
from generic.base_setup import BaseSetup
from generic.excel import Excel

class TestScript1(BaseSetup):
    def test_script1(self):
        print("This is test script 1")
        print(self.driver.title)
        Excel.get_data(self.xl_path,'login',2,2)
        print("Hello World")