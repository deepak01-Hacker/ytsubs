import random
import string
import array



def randomChar(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def randomMail():
    return randomChar(8)

def randomPassword():


    MAX_LEN = 12


    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)


    password = ""
    for x in temp_pass_list:
            password = password + x
            

    return password

def putValueInPage(driver,xpathh,value):

    driver.find_element_by_xpath(xpathh).click()
    driver.find_element_by_xpath(xpathh).send_keys(value)

def justClick(driver,xpathh):
    driver.find_element_by_xpath(xpathh).click()


if __name__ == "__main__":
    print(randomMail())
    print(randomPassword())