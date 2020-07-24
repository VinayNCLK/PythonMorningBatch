import pytest
from pages.loginpage import LoginPO
from pages.dashboardpage import DashboardPO
from utilities.excel_testdata import *
import sys

@pytest.mark.usefixtures("onetimesetup")
class Test_Login():
    @pytest.fixture(autouse=True)
    def classlevelsetup(self):
        self.lp = LoginPO(self.driver)
        self.dp = DashboardPO(self.driver)

    def test_validlogin(self):
        self.lp.enterusername("admin")
        self.lp.enterpassword("manager")
        self.lp.clickkeepmeloggedin()
        self.lp.clickloginbtn()
        self.lp.waitfordashboardpage()
        self.dp.logout()

    def test_invalidlogin(self):
        try:
            self.lp.enterusername("admin1")
            self.lp.enterpassword("passwored1")
            self.lp.clickloginbtn()
            self.lp.validateinvalidloginerrormsg()
        except Exception as e:
            self.lp.screenshot("test_invalidlogin")

    def test_invalidlogin_multipledata(self):
        try:
            sheetname = "test_invalidlogin_multipledata"
            exceldata_path = sys.path[0] + "\\test_data.xlsx"
            numberofrows = getnoofrows(exceldata_path, sheetname)
            for i in range(2,numberofrows+1):
                self.lp.enterusername(getcellvalue(exceldata_path,sheetname,rowno=i,colmunno=2))
                self.lp.enterpassword(getcellvalue(exceldata_path,sheetname,rowno=i,colmunno=3))
                self.lp.clickloginbtn()
                self.lp.validateinvalidloginerrormsg()
                writecellvalue(exceldata_path,sheetname,rowno=i,colmunno=4,value="PASS")
        except Exception as e:
            self.lp.screenshot("test_invalidlogin_mulitpledata")
