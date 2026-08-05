class Mobile_Security_System:

    def __init__(self, name, password):

        self.name = name                
        self.__password = password      
        self.__status = "Locked"    

    def unlock_mobile(self):

        enter_password = int(input("Enter Password : "))

        if enter_password == self.__password:
            self.__status = "Unlocked"
            print("\nYour Mobile is Unlocked Successfully.")
        else:
            print("\nWrong Password!")


    def lock_mobile(self):

        self.__status = "Locked"
        print("\nYour Mobile has been Locked.")


    def change_password(self):

        old_password = int(input("Enter Old Password : "))

        if old_password == self.__password:

            new_password = int(input("Enter New Password : "))

            self.__password = new_password

            print("\nPassword Changed Successfully.")

        else:
            print("\nOld Password is Incorrect.")


    def mobile_display(self):

        print("\n========== MOBILE DETAILS ==========")
        print("Owner  :", self.name)
        print("Status :", self.__status)
        print("====================================")


print("=" * 30)
print("   MOBILE SECURITY SYSTEM")
print("=" * 30)

name = input("Enter Mobile Owner Name : ")

password = int(input("Create Password : "))

user1 = Mobile_Security_System(name, password)


while True:

    print("\n========== MENU ==========")
    print("1. Unlock Mobile")
    print("2. Lock Mobile")
    print("3. Change Password")
    print("4. Mobile Status")
    print("5. Exit")

    choice = int(input("Enter Your Choice : "))

    match choice:

        case 1:
            user1.unlock_mobile()

        case 2:
            user1.lock_mobile()

        case 3:
            user1.change_password()

        case 4:
            user1.mobile_display()

        case 5:
            print("\nExiting Program...")
            print("Thank You for Visiting.")
            break

        case _:
            print("\nInvalid Choice! Enter between 1 to 5.")
