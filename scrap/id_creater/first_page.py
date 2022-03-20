from sre_constants import SUCCESS
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrap.subscriber.add_subscriber import subscribe #Chrome need
from utils.random_mail_pass_generator import *
from scrap.id_creater.verification import *
from scrap.id_creater.welcome import welcomePage
from record.recorder import getRecordObject


def putUserNamePassword(driver,recordObject):
    username = randomMail()
    password = randomPassword()
    print("username :-",username+"@gmail.com"," password :-",password)

    recordObject.write(username+"\n")
    recordObject.write(password+"\n")

    driver.find_element_by_xpath('//*[@id="username"]').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)

    driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').click()
    driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(password)

    driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').click()
    driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(password)

def putName(driver):
    first = "ram"
    last = "insan"

    driver.find_element_by_xpath('//*[@id="firstName"]').click()
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(first)

    driver.find_element_by_xpath('//*[@id="lastName"]').click()
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(last)

def firstPage(driver,recordObject):

    putName(driver)
    justClick(driver,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[3]/div/div/button/span') #create gmail instead

    putUserNamePassword(driver,recordObject)
    driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span').click() # for next button

    time.sleep(4)

def gmailCreate():
    success = False
    chrome_option = Options()
    recordObject = getRecordObject()

    #chrome_option.add_argument("--headless") #Chrome

    url = "https://accounts.google.com/signup/v2/webcreateaccount?service=youtube&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&dsh=S855897290%3A1647745622040820&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true"

    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url)

    try:
        firstPage(driver,recordObject)
        verification(driver)
        welcomePage(driver)
        subscribe(driver)
        success = True
    except Exception as e:
        print("Error In Id creation :-",e)

    if success:
        print("ID created and subscribe process done !")
        time.sleep(10)

    driver.close()
    driver.quit()
