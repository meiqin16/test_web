import time, HTMLTestRunnerPlugins, unittest

# 添加case文件路径
case_dir = "./case"
# 添加测试报告文件路径
report_dir = "./report"
# 制作时间格式
now = time.strftime("%Y-%m-%d %H-%M-%S")
# 命名测试报告文件名
report_file = open(report_dir + '\\' + now + 'HTMLReport.html', 'wb')
# 创建套件
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py")
# 创建runner
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
                                                title="unittest 自动化测试",
                                                description="unittest演示",
                                                stream=report_file,
                                                verbosity=2
                                              )
# 执行
runner.run(discover)
report_file.close()
