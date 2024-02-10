#making this function for reading contents from files if player wants to see rules settup by admin
def read_file(rules, file_for_Admin_random, file_for_Admin_exit, file_for_Admin_award):
    with open(rules) as reading:
        content = reading.read()
    # opening adminsettup files for getting variables to write in files
    with open(file_for_Admin_random) as random_file:
        reversed_random = random_file.read()
    
    with open(file_for_Admin_exit) as exit_file:
        end_val = exit_file.read()
    
    with open(file_for_Admin_award) as award_file:
        award_val = award_file.read()
    # after all printing all rules to users   
    print("\t\tRules Of Raza's Gaming Arena")
    print()
    print("Important Instructions")
    print()
    print("1.If You Won Any Award You Will Be Notified")
    print("2.If You Meet Certain Condition You Will Lose")
    print(f"3.The Number Is In Range {reversed_random}")
    print(f"4.The Number For Game Over Is {end_val}")
    print(f"5.The Number For Award Winning Is  {award_val}")


# Making this funtion To provide player choices about history options he have 
def history_option():
    print("\tThere are three options For You In History Section")
    print("\t1.Enter 1 To See Entire History Of Play")
    print("\t2.Enter 2 To See  History Of specific date ")
    print("\t3.Enter 3 To Exit")

# making this function for players to see thier histories of gaming
def see_history(file_for_user):
    x="***"
    while True:
     history_option()
     ask_by_user=input("Enter Your Option: ").lower()
     if ask_by_user=="1":   # if player wants to see complete history
      with open(file_for_user) as file:
        contents=file.readlines()
        if contents:
         for line in contents:
            data=line.strip().split(f"{x}")
            print()
            # printing overall historty
            print(f"Recored Time : {data[0]}")
            print(f"Name : {data[1]}")
            print(f"Total Attempts : {data[2]}")
            print(f"Total Awards You Got : {data[3]}")
            print()
         print()
         # if no history then prompting the message
        else:
            print("No History To show")
            print()
     elif ask_by_user == "2":      # if he wants to see specif history
            history = []
            ask_mon = input("Enter Month Name To See History:").upper().strip()
            ask_data = input("Enter Specific Date In Number:")
            take = ask_mon[0:3] + ask_data  # Updated: Combine month and date directly

            with open(file_for_user) as file:
                for line in file:
                    data = line.strip().split(f"{x}")
                    data[0] = data[0].split()
                    comp = data[0][1].upper() + data[0][2]  
                    user_dic = {comp: [data[0], data[1], data[2],data[3]]}
                    history.append(user_dic)
            check_by_user = False
            for check in history:
                if take in check.keys():  # Updated: Check for key existence directly
                    ans = check[take]  # Access using the generated `take` key
                    check_by_user = True
                    if check_by_user:
                        print()
                        # print the specific date history
                        print(f"Recorded Time Of Play :{ans[0]}")
                        print(f"Player Name :{ans[1]}")
                        print(f"Total Attempts To Win :{ans[2]}")
                        print(f"Total Awards You Achieve  :{ans[3]}")
                        print()
                        print()
            # if no record found of that specific date history
            if not check_by_user:
                print()
                print(f"No Record Found On That Date Of Month {ask_mon} {ask_data}")
                print()
     elif ask_by_user=="3": # if he wants to come out of this section
             print("Alright Return Back From This Section")
             print()
             return
     else: # invalid choice
        print("Invalid Choice Please Enter Correct Choice")
        print()
                  

# function for mainpage for users       
def choice_main_page():
    print("\t\tWELCOME TO RAZA'S GAMING ARENA")
    print("\tOnce You Login You Are Able To Play The Game")
    print()
    print("\t1.Create Account")
    print("\t2.Login As Player")
    print("\t3.Login As Admin")
    print("\t4.To Exit ")
# Making this functtion for admin to see complete data
def admin_see_data(file_for_accounts):
    x="***&^"   # our own sepertor
    all_data=[]
    with open (file_for_accounts) as file:
            contents=file.readlines()
            if contents:
             for line in contents:    # unpacking the data from file
                data=line.strip().split(f"{x}")
                user_data={"name":data[0],"userId":data[1],"useremail":data[2]}
                all_data.append(user_data)
             # printing all playwrs details
             print("\tALL PLAYERS DETAILS!!")
             print()
             for dictionaries in all_data:
                for key,value in dictionaries.items():
                    print(f"{key} : {value}")
                print()
            # if no players data has found
            else:
                print()
                print("No player data available at the moment.")
                print()
def admin_delete_player(user_Account, file_for_accounts):
    # Check if there are any accounts in the user_Account list
    if not user_Account:
        # Attempt to populate user_Account from file if it's empty
        x = "***&^"
        with open(file_for_accounts) as file:
            for line in file:
                data = line.strip().split(f"{x}")
                user_data = {"userid": data[1]}  # Assuming the user ID is at index 1 in your data
                user_Account.append(user_data)

        if not user_Account:
            print("No player data available at the moment.")
            return

    # Check if there are any accounts in the file
    with open(file_for_accounts) as file:
        file_contents = file.read().strip()
        if not file_contents:
            print("No player data available at the moment.")
            return

    user_name_to_delete = input("Enter User Name To Delete Record:").strip()

    with open(file_for_accounts, "r") as file:
        lines = file.readlines()

    new_lines = []  # Store modified lines here
    deleted = False  # Flag to track deletion
    for line in lines:
        data = line.strip().split(f"{x}")
        if data[1] != user_name_to_delete:
            new_lines.append(line)  # Keep lines for other usernames
        else:
            deleted = True
            print(f"Account for {user_name_to_delete} deleted successfully.")
    if not deleted:
        print("No Username Of That Name")
    with open(file_for_accounts, "w") as file:
        file.writelines(new_lines)  # Write back the modified lines

    # Update final list only if deletion occurred
    if deleted:
        user_Account = [user for user in user_Account if user["userid"] != user_name_to_delete]



# making this functuon for admin if he want to search for any specific player
def player_search(file_for_accounts):
    name_serach = False
    x = "***&^"
    all_data = []
    with open(file_for_accounts) as file:
        for line in file:
                data = line.strip().split(f"{x}")
                user_data = {"name": data[0], "userId": data[1], "useremail": data[2]}
                all_data.append(user_data)
        if all_data:
            name_to_search = input("Enter User Id To Search Record:")
            for check in all_data:
                if name_to_search == check["userId"]:
                    name_serach = True   # if name is sound that admin wants to see details of
                    if name_serach:
                        # printing the data of specific player
                        print(f"Player Name : {check['name']}")
                        print(f"Player User-Id : {check['userId']}")
                        print(f"Player Email : {check['useremail']}")
                        print()
                        print()
            # if wrong username enter by admin
            if not name_serach:
                print()
                print(f"No Record Found of that userid {name_to_search}")
                print()
        else:   # if no player has created account yet
            print()
            print("No player data available at the moment.")
            print()
       
                
# function to see complee scores along with names of all players
def view_Score(file_for_score,score_list): 
    x="***"
    print("Welcome To Number Guessing Game!!")
    print()
    with open(file_for_score) as score:
        score.seek(0) # seek to move cursor zero
        for line in score:
            data=line.strip().split(f"{x}")
            user_score={"name":data[0],"score":int(data[1])}
            score_list.append(user_score)
        if not score_list: # if no player has played the game
            print("OHHO!! No Player Is Arrived Yet!!")
            print()
        else:
         # printing all players scores
         print("NAMES : SCORES")
         for every in score_list:
            for key,value in every.items():
                print(f"{key}:{value}")
            print()
# making the function for random number generetae and set by admin
def game_settings_random(file_for_Admin_random):
    while True:
        with open(file_for_Admin_random, "w") as file:
            ask_start_num = input("Enter Starting Number: ").strip()
            ask_end_num = input("Enter Ending Number: ").strip()
            # apply condition for appropiate input by admin
            if all(char.isdigit() for char in ask_start_num) and all(char.isdigit() for char in ask_end_num):
                file.write(f"{ask_start_num},{ask_end_num}")  # Write only the numerical range
                file.seek(0)
                break # break on certain condition
            else:
                print("Please Enter In Digits")


      
def game_settings_Award(file_for_Admin_award):
    while True:
        with open(file_for_Admin_award,"w") as award: # open the file to write back in file
          award_num=input("Enter New Conditional Number For Award Winning:")
          if all(char.isdigit() for char in award_num) :
            award.write(f"{award_num}")
            award.seek(0)    # after that seek to zero
            break
          else:
              print("Invalid Input Write In NUmber Must Be Greater Than Zero")
              print()
            
def game_settings_end(file_for_Admin_exit):
    while True:  # apply loop to stuk admin here
        with open(file_for_Admin_exit,"w") as end:

           num_to_exit=input("Enter New Conditional Number For Exit:")
           if all(char.isdigit() for char in num_to_exit):
                end.write(f"{num_to_exit}")
                end.seek(0) # seek to move cursor to start
                break
           else: # printing for only digits allowed
               print("Invalid Input Must BE In Digits")