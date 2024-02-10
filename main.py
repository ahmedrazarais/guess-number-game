#Importing differnt files and functions from other files
from adminfunctions import choice_main_page
from players_signup import user_signup,get_name,time
from filespaths import file_for_user,file_for_accounts
from playerslogin import login
from adminlogin import admin_login

user_Account=[]  # list for appending users details 
score_list=[]    # list for taking users scores for award and other process
min_score=""  # initial minimum score to zero

# this function for printing user details about gaming zone
def options_gaming_zone():
    print("\t\tWELCOME IN RAZA'S GAMING ARENA!!")
    print()
    print("\tWe are Here To Entertain You!!")
    print("\t1.Press 1 To Start The Game")
    print("\t2.Press 2 To See Your History Of Gaming")
    print("\t3.Press 3 To See The RUles Of Games")
    print("\t4.Press 4 To Exit")
    print()
# applying loop on certain conditions for players
#calling different function on certain conditions
while True:
  choice_main_page()
  choice=input("Enter Your Choice:")

  if choice=="1":
   print("Create Your Account..")
   print()
   name=get_name()
   user_signup(user_Account,file_for_user,file_for_accounts,name)
   time() 
  elif choice=="2":
    print("Login With Your User Id..")
    print()
    name=get_name()
    login(name,file_for_user,user_Account,file_for_accounts)
  elif choice=="3":
      admin_login()

  elif choice=="4":
      print("🎮 We noticed you've stepped out of the game arena! We miss your presence in the action-packed world of Guess The Number. Come back and join the fun! 🚀")
      print()
      print()
      break # if user wants to exit so come out of loop
  else:
      print("Invalid Choice")
      print("Please Select Correct Choice")
      print()