import pytest
from pages.loginpage import LoginPO
from pages.dashboardpage import DashboardPO
from pages.adduserspage import AdduserPO

@pytest.mark.usefixtures("onetimesetup")
class Test_users():
    @pytest.fixture(autouse=True)
    def classlevelsetup(self):
        self.lp = LoginPO(self.driver)
        self.dp = DashboardPO(self.driver)
        self.au = AdduserPO(self.driver)

    def createuser(self):
        self.lp.validlogin("admin","manager")
        self.dp.userstab()
        self.dp.newuserbtn()
        self.au.firstname("abc")
        


