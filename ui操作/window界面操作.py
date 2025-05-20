import uiautomation,time
'''
自动化控制window的计算机实现1+9=10，首先指定控制窗口，使用name属性
然后用按钮id属性，控制点击计算机按钮
'''
time.sleep(2)
calc=uiautomation.WindowControl(name="计算器")
calc.ButtonControl(AutomationId="num1Button").Click()
calc.ButtonControl(AutomationId="plusButton").Click()
calc.ButtonControl(AutomationId="num9Button").Click()
calc.ButtonControl(AutomationId="equalButton").Click()