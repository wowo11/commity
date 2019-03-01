import sys
sys.path.append("E:\discuz_project")
import unittest
import os
# from test.test_discuz_one import Test_one
# from test.test_two import Test_two
# from test.test_three import Test_three
# from test.test_four import Test_four
test_dir='./'

import HTMLTestRunner

current_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(current_path,'report')
if not os.path.exists(report_path):os.mkdir(report_path)
#批量执行测试用例
suite=unittest.TestLoader().discover(test_dir,pattern='test*.py')
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Test_one))
# suite.addTest(unittest.makeSuite(Test_two))
# suite.addTest(unittest.makeSuite(Test_three))
# suite.addTest(unittest.makeSuite(Test_four))
if __name__=="__main__":
    html_report=report_path+r'/result.html'
    # print(html_report,"dhtghgj")
    file=open(html_report,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title='测试报告',description='测试用例')
    runner.run(suite)





