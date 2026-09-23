from CUSTOMER_REGISTRATION import customer_registration, current_customer
from ROOM_MANAGEMENT import room_management
from SERVICE_MANAGEMENT import *
from BILL_MANAGEMENT import bill_management
import sqlite3 as sql
import time
import random

def main():
    print("HELLO WELCOME TO 7* HOTEL")
    c_details=customer_registration()
    c_room = None
    cr_bill = 0
    c_r_type = None
    while True:
        print("1.TO CHECK-IN\n2.TO EXIT")
        m_input=input("ENTER YOUR CHOICE: ")
        if m_input == "1":
            c_r_type,cust_room,cr_bill = room_management()
            print("HOPE YOU ENJOY YOUR STAY")
            c_room = cust_room
            break
        elif m_input == "2":
            break
        else:
            print("Invalid input")
    s_bill = service_management(c_details[1],c_details[2],c_room)

    bill_management(c_room,c_r_type,cr_bill,s_bill,c_details[1],c_details[2])
    conn = sql.connect('./Database/rooms.db')
    c = conn.cursor()

    c.execute(f'UPDATE {c_r_type} SET availability = True WHERE room_no = {c_room}')
    print("THANK YOU, VISIT AGAIN")
    conn.commit()
    conn.close()


main()