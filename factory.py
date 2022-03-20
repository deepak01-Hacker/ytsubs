from scrap.id_creater.first_page import *

if __name__ == "__main__":

    while(1):
        print("Operations :- \n1.For New ID & Subscriber\n2.Stop")
        operation = input()
        if operation == "2":
            break
        try:
            gmailCreate()
        except Exception as e:
            print("Error in selenium :- ",str(e))