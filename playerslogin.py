from filespaths import file_for_score,rules,file_for_Admin_random,file_for_Admin_award,file_for_Admin_exit
from adminfunctions import read_file,see_history
from Numbergame import number_game



def options_gaming_zone():
    print("\t\tWELCOME IN RAZA'S GAMING ARENA!!")
    print()
    print("\tWe are Here To Entertain You!!")
    print("\t1.Press 1 To Start The Game")
    print("\t2.Press 2 To See Your History Of Gaming")
    print("\t3.Press 3 To See The RUles Of Games")
    print("\t4.Press 4 To Exit")
    print()
def login(name, file_for_user, user_Account, file_for_accounts):
    x = "***&^"
    with open(file_for_accounts) as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(f"{x}")
            if data[1]:  # Only append if data[0] is not empty
                user_Accounts = {"user_id": data[1]}
                user_Account.append(user_Accounts)
        while True:
            user_name = False
            user_id = input("Enter Your User Id:")
            for check in user_Account:
                if "user_id" in check and user_id == check["user_id"]:
                    user_name = True
                    print("Login Successfully")
                    file_for_user = file_for_user + user_id + ".txt"
                    print()
                    with open(file_for_user, 'a+'):
                        pass
                    while True:
                        options_gaming_zone()
                        choice = input("Enter Your Choice:")
                        if choice == "1":
                            number_game(file_for_user, name, file_for_score)
                        elif choice == "2":
                            see_history(file_for_user)
                        elif choice == "3":
                            read_file(rules, file_for_Admin_random, file_for_Admin_exit, file_for_Admin_award)
                        elif choice == "4":
                            print("Our gaming community is waiting for a champion like you! 🏆 Thanks for being a part of Guess The Number. See you back in the arena soon! 👋")
                            print()
                            return
                        else:
                            print("Invalid Choice")
                            print()
            if not user_name:
                print("No Record Found Of That Id")
                print()
                while True:
                    ask_for_try = input("Did You Want Another Try (Y/N):").lower()
                    if ask_for_try == "n":
                        print("Back To Our Main Page...")
                        print()
                        return
                    elif ask_for_try == "y":
                        print("Alright TRY AGAIN!")
                        print()
                        break
                    else:
                        print("Please Enter Correct Option (Y/N)")