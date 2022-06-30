from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# 2. Mở URL của post
browser.get("http://10.255.58.201:9000")
sleep(5)
# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("username")
txtUser.send_keys("sonnb2")
txtPass = browser.find_element_by_name("password")
txtPass.send_keys("Kimm@123")
txtPass.send_keys(Keys.ENTER)
sleep(10)
browser.get("http://10.255.58.201:9000/#/cr/crManagement")
sleep(10)

# chọn mục cab
txtSelect = browser.find_element_by_id("custom-input-searchGroup")
txtSelect.send_keys("Đang CAB")
txtSelect.send_keys(Keys.ENTER)
# 3. Lấy link hiện comment
#showmore_link = browser.find_element_by_xpath ("/html/body/div/div/div/div[3]/main/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[1]")
#showmore_link.click()
sleep(10)
# 6. Đóng browser
browser.close()
