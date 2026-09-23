import CUSTOMER_REGISTRATION
import ROOM_MANAGEMENT

from CUSTOMER_REGISTRATION import customer_registration, current_customer
from ROOM_MANAGEMENT import room_management


def Main():
    print("HELLO WELCOME TO 7* HOTEL")
    cr=customer_registration()
    while True:
        print("1.TO CHECK-IN\n2.TO EXIT")
        m_input=input("ENTER YOUR CHOICE: ")
        if m_input == "1":
            cust_room = room_management()
        elif m_input == "2":
            break
        else:
            print("Invalid input")




Main()