import sqlite3 as sql

conn = sql.connect("./Database/rooms.db")
c = conn.cursor()

def room_management():
    print(" ")
    while True:
        print(" ")
        print("PLEASE CHOOSE YOU ROOM TYPE")
        print("1.SUIT ROOMS-Rs.6000/night\n2.TWO SEATER ROOMS-Rs.2000/nightRs\n3.FAMILY ROOMS-Rs.4000/night")
        print(" ")
        choice = input("ENTER YOUR CHOICE: ")
        if choice == "1":
            print(" ")
            print("AVAILABLE SUITE-ROOMS")
            c.execute("SELECT room_no,floor_no FROM suite_rooms WHERE availability = True")
            print(c.fetchall())
            for i in c.fetchall():
                print(i)
            print(" ")

            print("1.TO SELECT YOUR ROOM\n2.GO BACK TO CHOOSING ROOM TYPE")
            r_c = input("ENTER YOUR CHOICE: ")
            if r_c == "1":
                print(" ")
                c_suc = False
                r_b = int(input("ENTER THE ROOM NO TO BOOK: "))
                print(f'ROOM SELECTED:{r_b}(Suite_Room)')
                c.execute("SELECT room_no FROM suite_rooms WHERE availability = True")
                r_a = False
                for i in c.fetchall():
                    if r_b == i[0]:
                        print("Available", r_b)
                        r_c = input("TYPE BOOK (to give details) TO CHECK-IN: ")
                        if r_c == "BOOK":
                            print("CHECK-IN SUCCESSFUL")
                            c_suc = True
                            r_a = True
                            c.execute("UPDATE suite_rooms SET availability = False WHERE room_no = ?",(r_b,))
                            return r_b
                            break
                        else:
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            break
                    else:
                        pass
                if not r_a:
                    print("CHOSEN ROOM NOT AVAILABLE")

                elif c_suc:
                    break


            elif r_c == "2":
                pass

        elif choice == "2":
            print(" ")
            print("AVAILABLE TWO-SEATER ROOMS")
            c.execute("SELECT room_no,floor_no FROM two_seater WHERE availability = True")
            print(c.fetchall())
            for i in c.fetchall():
                print(i)
            print(" ")

            print("1.TO SELECT YOUR ROOM\n2.GO BACK TO CHOOSING ROOM TYPE")
            r_c = input("ENTER YOUR CHOICE: ")
            if r_c == "1":
                print(" ")
                c_suc = False
                r_b = int(input("ENTER THE ROOM NO TO BOOK: "))
                print(f'ROOM SELECTED:{r_b}(Two-Seater Room)')
                c.execute("SELECT room_no FROM two_seater WHERE availability = True")
                r_a = False
                for i in c.fetchall():
                    if r_b == i[0]:
                        print("Available", r_b)
                        r_c = input("TYPE BOOK (to give details) TO CHECK-IN: ")
                        if r_c == "BOOK":
                            print("CHECK-IN SUCCESSFUL")
                            c_suc = True
                            r_a = True
                            c.execute("UPDATE two_seater SET availability = False WHERE room_no = ?", (r_b,))
                            return r_b
                            break
                        else:
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            break
                    else:
                        pass
                if not r_a:
                    print("CHOSEN ROOM NOT AVAILABLE")

                elif c_suc:
                    break

            elif r_c == "2":
                pass
        elif choice == "3":
            print(" ")
            print("AVAILABLE FAMILY ROOMS")
            c.execute("SELECT room_no,floor_no FROM family_room WHERE availability = True")
            print(c.fetchall())
            for i in c.fetchall():
                print(i)
            print(" ")

            print("1.TO SELECT YOUR ROOM\n2.GO BACK TO CHOOSING ROOM TYPE")
            r_c = input("ENTER YOUR CHOICE: ")
            if r_c == "1":
                print(" ")
                c_suc = False
                r_b = int(input("ENTER THE ROOM NO TO BOOK: "))
                print(f'ROOM SELECTED:{r_b}(Two-Seater Room)')
                c.execute("SELECT room_no FROM family_room WHERE availability = True")
                r_a = False
                for i in c.fetchall():
                    if r_b == i[0]:
                        print("Available", r_b)
                        r_c = input("TYPE BOOK (to give details) TO CHECK-IN: ")
                        if r_c == "BOOK":
                            print("CHECK-IN SUCCESSFUL")
                            c_suc = True
                            r_a = True
                            c.execute("UPDATE family_room SET availability = False WHERE room_no = ?", (r_b,))
                            return r_b
                            break
                        else:
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            print("CHECK-IN FAILED")
                            break
                    else:
                        pass
                if not r_a:
                    print("CHOSEN ROOM NOT AVAILABLE")

                elif c_suc:
                    break

            elif r_c == "2":
                pass
        else:
            print("INVALID CHOICE")
            print(" ")




room_management()

conn.commit()
c.close()
