import time


def verification(driver):

    driver.find_element_by_xpath('//*[@id="phoneNumberId"]').click()
    mobileNumber = input("Please Input Your Phone Number without country code :- ")
    driver.find_element_by_xpath('//*[@id="phoneNumberId"]').send_keys(mobileNumber)

    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() #for next button
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="code"]').click()
    verificationCode = input("Verification Code :- ")

    driver.find_element_by_xpath('//*[@id="code"]').send_keys(verificationCode)
    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span').click()

    time.sleep(5)

