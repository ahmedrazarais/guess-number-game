
def get_name():
    while True:
     name=input("Enter Your Name:").strip()
     if not name:
          print("It is mandatory To Fill This Field")     
     elif not all(char.isalpha() or char.isspace() for char in name ):     
            print("Only Alphabets Allowed In Name")
     else:
         return name
        #  break
def time():
    import time
    current_time=time.ctime()
    return current_time
    # print(current_time)              
    
def user_signup(user_Account, file_for_user, file_for_accounts,name):
    x = "***&^"
    with open(file_for_accounts) as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(f"{x}")
            if data[1]:  # Only append if data[0] is not empty
                user_Accounts = {"user_id": data[1]}
                user_Account.append(user_Accounts)

    while True:
        user_id = input("Enter Your User Id (Enter 0 to return):")
        if user_id=="0":
            return
        for check in user_Account:
           if "user_id" in check and user_id == check["user_id"] and len(user_id) > 1:
                print("This UserName Is Already Taken Please Select another")
                print("If You already Have an account so please Login")
                print()
                break  # Break out of the outer while loop
        else:
             while True:
                gmail_=input('Enter your gmail:')
                s='!#$%^&*()_+|}{":<?/,\';\\][=-]}'
                if gmail_=='':
                    print('Required field cannot be left blank')
                elif gmail_.startswith(' '):
                    print('The entered gmail is not valid')
                elif not(6<len(gmail_)<30):
                    print('Length must be between 6 and 30 characters long')
                elif not(gmail_.endswith('@gmail.com')):
                    print('Make sure @gmail.com must be at last')    
                elif (gmail_.startswith('@gmail.com')):
                    print('Enter valid Gmail')
                elif (gmail_.endswith('.@gmail.com')):
                    print('Sorry the last character before @gmail.com must be a letter or number')
                elif any(char in s for char in gmail_):
                        print('Only letters and numbers are allowed')
                else:
                    break
             with open(file_for_accounts, "a") as file:
                file.write(f"{name}{x}{user_id}{x}{gmail_}\n")  # Add newline after username
             print("Your Account Has Been Successfully Created")
             break