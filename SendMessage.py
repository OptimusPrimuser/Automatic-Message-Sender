from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#message_enter="//*[@id='main']/footer/div[1]/div[3]/button"
#search_bar="//*[@id='side']/div[1]/div/label/div/div[2]"
#cancle_search='//*[@id="side"]/div[1]/div/span/button/span'
class SendMessage:
    def send_message_unknown(self,driver,no,message):
        url="https://web.whatsapp.com/send?phone="+no+"&text="+message+"&source=&data="
        driver.get(url)
        message_enter='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        while True:
            try:
                time.sleep(0.3)
                message_enter=driver.find_element_by_xpath(message_enter)   
                break
            except :
                pass
        message_enter.send_keys(Keys.ENTER)
        while True:
            try:
                driver.find_element_by_xpath('//span[@aria-label=" Pending "]')
                time.sleep(0.3)
            except:
                break

    def __init__(self,nos,message):
        search_bar="//*[@id='side']/div[1]/div/label/div/div[2]"
        path="chromedriver.exe"
        driver=webdriver.Chrome(executable_path=path)
        driver.get("https://web.whatsapp.com")

        while True:
            try: 
                search_bar=driver.find_element_by_xpath(search_bar)
                break
            except :
                pass
        
        for i in nos:
            self.send_message_unknown(driver,i,message)

        driver.quit()
