from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.get("https://www.apengdai.com/user/login")
dr.maximize_window()
dr.find_element_by_id("userName").send_keys("用户名")
dr.find_element_by_id("loginPass").send_keys("用户密码")
time.sleep(8)
dr.find_element_by_tag_name("button").click()
time.sleep(4)
dr.get("https://www.apengdai.com/licai/31981")
dr.find_element_by_id("amount").send_keys("投资金额")
#dr.find_element_by_id("alltou").click()
dr.find_element_by_css_selector("input[type='submit']").click()
#dr.find_element_by_class_name("ft16.ztac-btn").click()

k=1
while k<2:
    now_time=time.strftime("%H:%M")
    now_time1=time.strftime("%H:%M:%S")

    if now_time == '时间点：12:00':
        print ("====================")
        dr.find_element_by_id("okcp").click()
        time.sleep(3)
        js="document.getElementsByClassName('affirm_qr_bt')[0].click()"
        dr.execute_script(js)
        time.sleep(3)
        dr.find_element_by_id("pass").send_keys("交易密码")
        dr.find_element_by_id("sub").click()
    else:
        time.sleep(2)
        print (now_time1)
