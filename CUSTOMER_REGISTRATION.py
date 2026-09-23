
current_customer = []

def customer_registration():
    while True:
        cust_v = input("ARE YOU OUR REGISTERED USER: ")
        found = False
        if cust_v == "YES":
            print('''1.SIGN IN BY NAME\n2.SIGN IN BY PH-NO: ''')

            while True:

                s_choice = input("ENTER YOUR CHOICE(1.NAME/2.PH-NO): ")
                with open("./Database/CUSTOMER_HISTORY.txt", "r") as file:
                    if s_choice == "1":
                        u_name = input("ENTER YOUR NAME: ")
                        for line in file:
                            l_d = line.split()
                            if l_d[1] == u_name:
                                found = True
                                print(l_d)
                                current_customer = l_d
                                print("YOU ARE OUR REGISTERED USER")
                                break
                        if found:
                            break
                        elif not found:
                            break


                    elif s_choice == "2":
                        u_phno = input("ENTER YOUR PH-NO: ")
                        for line in file:
                            l_d = line.split()
                            if l_d[2] == u_phno:
                                found = True
                                print(l_d)
                                print("YOU ARE OUR REGISTERED USER")
                                break
                        if not found:
                            break
                        elif found:
                            break
                    else:
                        print("INVALID CHOICE")
            if not found:
                print("CUSTOMER NOT FOUND")
            elif found:
                break


        elif cust_v == "NO":
            print(" ")
            print("TO REGISTER")
            cust_n = input("ENTER YOUR NAME: ")
            cust_phno = input("ENTER YOUR PH-NO: ")
            cnt = 0
            with open("./Database/CUSTOMER_HISTORY.txt", "r") as file:
                for line in file:
                    cnt += 1
            with open("./Database/CUSTOMER_HISTORY.txt", "a") as file:
                file.write("\n")
                file.write(f'{cnt+1} {cust_n} {cust_phno}')
                print("REGISTERED SUCCESSFULLY")
                print("YOUR CUSTOMER ID: ", cnt+1)

            nm_c = 0
            with open("./Database/CUSTOMER_HISTORY.txt", "r") as file:
                for line in file:
                    nm_c += 1
                    if nm_c == cnt+1:
                        current_customer = line.split()
            break
        else:
            print("Invalid input")

    return current_customer

