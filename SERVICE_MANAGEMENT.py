import time
import random
from random import randint


def service_management(c_name,c_phno,c_room):
    current_cust_scharges = 0
    print(" ")
    print("WELCOME TO SERVICE MANAGEMENT")
    print(" ")
    while True:
        print("OUR SERVICES DURING YOUR STAY INCLUDE:")
        print("1.BUFFET(breakfast(Rs.300/person)/lunch(Rs.500/person)/dinner(Rs.500/person)/snacks(Rs.150/person)\n2.ROOM CLEANING\n3.CHECK OUT")
        choice = input("ENTER YOUR CHOICE:")
        if choice == "1":
            print(" ")
            print("BOOK YOUR BUFFET")
            print("1.Book your breakfast\n2.Book your lunch\n3.Book your dinner\n4.Book your evening snacks")
            f_c = input("ENTER YOUR CHOICE:")
            print(" ")
            if f_c == "1":
                f_b = input("TYPE BOOK TO BOOK YOUR BREAKFAST: ")
                if f_b == "BOOK":
                    current_cust_scharges += 300
                    print("YOUR BOOKING IS SUCCESSFUL")
                    print("BREAKFAST TIMINGS: 7:00 AM - 10:00 AM")
                    print("BREAKFAST VENUE: GARDEN-1(Ground floor)")
                    print("YOUR QR CODE: ")
                    print(f'Customer Details:\nName: {c_name}\nPhone Number: {c_phno}\nRoom No: {c_room}')
                    print('''----------------------------
                    ---          ****                  --
                    ------  -------     --    ** --------
                    -------  &&&  -----------***---------
                    -------     ###### ------------------
                    -------------------------------------
                    ''')
                else:
                    print("YOUR BOOKING IS NOT SUCCESSFUL")
                    print(" ")

            elif f_c == "2":
                f_b = input("TYPE BOOK TO BOOK YOUR LUNCH: ")
                if f_b == "BOOK":
                    current_cust_scharges += 500
                    print("YOUR BOOKING IS SUCCESSFUL")
                    print("LUNCH TIMINGS: 12:00 PM - 2:00 PM")
                    print("LUNCH VENUE: GARDEN-1(Ground floor)")
                    print("YOUR QR CODE: ")
                    print(f'Customer Details:\nName: {c_name}\nPhone Number: {c_phno}\nRoom No: {c_room}')
                    print('''----------------------------
                    ---          ****                  --
                    ------  -------     --    ** --------
                    -------  &&&  -----------***---------
                    -------     ###### ------------------
                    -------------------------------------
                    ''')
                else:
                    print("YOUR BOOKING IS NOT SUCCESSFUL")
                    print(" ")

            elif f_c == "3":
                f_b = input("TYPE BOOK TO BOOK YOUR DINNER: ")
                if f_b == "BOOK":
                    current_cust_scharges += 500
                    print("YOUR BOOKING IS SUCCESSFUL")
                    print("DINNER TIMINGS: 7:30 PM - 10:00 PM")
                    print("DINNER VENUE: GARDEN-1(Ground floor)")
                    print("YOUR QR CODE: ")
                    print(f'Customer Details:\nName: {c_name}\nPhone Number: {c_phno}\nRoom No: {c_room}')
                    print('''----------------------------
                    ---          ****                  --
                    ------  -------     --    ** --------
                    -------  &&&  -----------***---------
                    -------     ###### ------------------
                    -------------------------------------
                    ''')
                else:
                    print("YOUR BOOKING IS NOT SUCCESSFUL")
                    print(" ")

            elif f_c == "4":
                f_b = input("TYPE BOOK TO BOOK YOUR SNACKS: ")
                if f_b == "BOOK":
                    current_cust_scharges += 150
                    print("YOUR BOOKING IS SUCCESSFUL")
                    print("SNACKS TIMINGS: 7:30 PM - 10:00 PM")
                    print("SNACKS VENUE: GARDEN-1(Ground floor)")
                    print("YOUR QR CODE: ")
                    print(f'Customer Details:\nName: {c_name}\nPhone Number: {c_phno}\nRoom No: {c_room}')
                    print('''----------------------------
                    ---          ****                  --
                    ------  -------     --    ** --------
                    -------  &&&  -----------***---------
                    -------     ###### ------------------
                    -------------------------------------
                    ''')
                else:
                    print("YOUR BOOKING IS NOT SUCCESSFUL")
                    print(" ")

            else:
                print("INVALID CHOICE")
                print(" ")

        elif choice == "2":
            print("")
            print("ROOM CLEANING ORDERED")
            print("CLEANER WILL BE AT YOUR DOORSTEP VERY SOON")
            a = random.randint(10,15)
            for i in range(a):
                print("..",end=' ')
                time.sleep(1)
            print("\n")
            print("CLEANER IS HERE")
            b = random.randint(4, 7)
            for i in range(b):
                print(".",end=" ")
                time.sleep(1)
            print("\n")
            print("CLEANING IS BEING DONE")
            c = random.randint(12, 17)
            for i in range(c):
                print(".",end=" ")
                time.sleep(1)
            print("\n")
            print("ROOM CLEANING IS DONE")
            print(" ")

        elif choice == "3":
            s_bill = current_cust_scharges
            return s_bill
        else:
            print("INVALID CHOICE")
            print(" ")







