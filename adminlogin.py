from filespaths import file_for_accounts,file_for_Admin_random,file_for_Admin_award,file_for_score,file_for_Admin_exit,file_for_user
user_Account=[]
score_list=[]
from adminfunctions import admin_see_data,admin_delete_player,player_search,view_Score,game_settings_Award,game_settings_end,game_settings_random
from players_signup import get_name,time,user_signup



def admin_choices():
    print("\t|THERE ARE TWO CHOICES FOR YOU!!")     
    print("\t1.Manage Players Accounts Details")
    print("\t2.Manage Players Gaming Area")
    print("\t3.Exit From Admin Section")
    print()
    
def admin_choices_Accounts():
    print()
    print("\tWeLCOME IN THIS AREA") 
    print("\t1.See All Players Accounts Data")
    print("\t2.Add Any Players Accounts Data")
    print("\t3.Delete Any Players Accounts Data")
    print("\t4.Search Any Players Accounts Data")
    print("\t5.Exit From Account Area ")
    print()
    print()
def admin_choices_Gaming():
    print("WELCOME TO THIS AREA!!")
    print("\t1.View Overall Scores Of All Players")
    print("\t2.Set The Random Values For The Game")
    print("\t3.Set The Number For Award Winning Condition")
    print("\t4.Set The Number For Game Over")
    print("\t5.Exit From This Section")

# number_game(file_for_user,time,get_name)     # calling the function
def admin_login():
    user_name="raza"
    psd="1234"
    while True:
     user_name_input=input("Enter Admin User name enter 0 to go back :").lower()
     if user_name_input=="0":
         return
     if user_name_input==user_name:
         psd_input=input("Enter admin Password enter 0 to go back:")
         if psd_input=="0":
             return
         if psd_input==psd:
             print("Login SuccessFully!!")
             while True:
                 admin_choices()
                 choice=input("Enter Your Option :")
                 if choice=="1":
                     while True:
                         admin_choices_Accounts()  
                         option=input("Enter Your Desired Option")
                         if option=="1":
                               admin_see_data(file_for_accounts)
                         elif option=="2":
                              print("Create Your Account..")
                              print()
                              name=get_name()
                              user_signup(user_Account,file_for_user,file_for_accounts,name)
                              time()
                         elif option=="3":
                              admin_delete_player(user_Account,file_for_accounts)
                         elif option=="4":
                             player_search(file_for_accounts)
                         elif option=="5":
                             print("Alright Return From This Section")
                             print()
                             break
                 elif choice=="2":
                     while True:
                         admin_choices_Gaming()
                         option=input("Enter Your Desired Option")
                         if option=="1":
                             view_Score(file_for_score,score_list)
                         elif option=="2":
                             game_settings_random(file_for_Admin_random)
                         elif option=="3":
                             game_settings_Award(file_for_Admin_award)
                         elif option=="4":
                              game_settings_end(file_for_Admin_exit)
                         elif option=="5":
                              print("Alright Return From This Section")
                              print()
                              break
                 elif choice=="3":
                     print("Hope You Enjoying Using Admin Services")
                     print()
                     print("Back To Main Page..")
                     print()
                     return
                 else:
                     print("Invalid Choice Please Select Correct Choice")
                     print()
        
         else:
             print("Invalid Password")
             print()
     else:
         print("Invalid User Name")
         print()
         while True:
             ask_for_more=input("Did You Want Another Chance (Y/N):").lower()
             if ask_for_more=="y":
                 print("Alright Try Again!!")
                 print()
                 break
             elif ask_for_more=="n":
                 print("Alright Back To Main Page..")
                 print()
                 return
             else:
                 print("Please Select Correct Choice (Y/N)")
                 print()