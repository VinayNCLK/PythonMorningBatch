from tests.login import Test_Login
import unittest

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Login.test_validlogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_Login.test_invalidlogin)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Login.test_invalidlogin_multipledata)

smokeTest = unittest.TestSuite([tc1])
regression = unittest.TestSuite([tc1,tc2,tc3])

#unittest.TextTestRunner.run(smokeTest)
unittest.TextTestRunner.run(regression)