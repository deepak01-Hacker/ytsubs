from selenium.webdriver.support.ui import Select
from utils.random_mail_pass_generator import *
import time



def welcomePage(driver):

    monthSelector = Select(driver.find_element_by_xpath("""//*[@id="month"]""")) 
    monthSelector.select_by_index(1) 

    putValueInPage(driver,'//*[@id="day"]','01')
    putValueInPage(driver,'//*[@id="year"]','2001')

    monthSelector = Select(driver.find_element_by_xpath("""//*[@id="gender"]""")) 
    monthSelector.select_by_index(1) 

    justClick(driver,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]')
    time.sleep(3)

    justClick(driver,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/span')
    time.sleep(2)

    justClick(driver,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    time.sleep(6)




