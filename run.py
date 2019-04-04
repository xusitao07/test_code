import TestCase.test_weather
import HTMLTestReportCN
import getcwd
import os
import Common.my_email

import unittest
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase.test_weather.weather('test_weather'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path,'report/xxx接口自动化测试报告.html')
    fp = open(file_path,'wb')
    runner = HTMLTestReportCN.HTMLTestReportCN(
        stream = fp,
        title = 'xxx接口自动化测试报告',
        description = '报告中描述部分',
        tester = '测试者'
    )
    runner.run(suite)
    fp.close()
    Common.my_email.mail()


#       testDir = 'D:\\TjsApi\\TestCase\\'  # 定义测试用例目录
#       discover = unittest.defaultTestLoader.discover(testDir, pattern="test_appUI*.py")
#       reportDir = "D:\\TjsApi\\Android_report\\"  # 定义报告存放路
#       runner = HTMLTestRunner(stream=fp, title=u"同金社Android流程测试报告", description=u"测试用例执行情况：")
#       runner.run(discover)  # 运行用例生成报告