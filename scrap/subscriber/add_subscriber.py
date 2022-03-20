import time

def subscribe(driver):

    driver.get('https://www.youtube.com/c/DeraSachaSaudaOfficial')
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button').click()


   
