from players_signup import time
from filespaths import file_for_Admin_exit,file_for_Admin_award,file_for_Admin_random,rules
score_list=[]

import random
def number_game(file_for_user, name, file_for_score):
    current_time_value = time()
    curr_name = name
    global min_score
    x = "***"
    print("Welcome To Number Guessing Game!!")
    print()
    with open(file_for_Admin_exit) as close:
        end_val=close.read()
       
    with open(file_for_Admin_award) as award:
        award_val=award.read()
     
    with open(file_for_Admin_random) as here:
        reversed_random=here.read()
    
    # Check if score_list is empty
    if not score_list:
        with open(file_for_score) as score:
            score.seek(0)
            for line in score:
                data = line.strip().split(f"{x}")
                user_score = {"name": data[0], "score": int(data[1])}
                score_list.append(user_score)
    champion_names = []
    min_score = min(check["score"] for check in score_list)
    for check in score_list:
        if check["score"] == min_score and check["name"] not in champion_names:
         champion_names.append(check["name"])
         print(f"Least Attempts To Win: {min_score}")
         print(f"Names Of Champions: {', '.join(champion_names)}")

    # Proceed with the game logic
   

    random_numbers = []  # Renamed variable to avoid conflict with the 'random' module
    with open(file_for_Admin_random) as random_file:
            for line in random_file:
                new_rand = line.strip().split(",")
                random_numbers.append(new_rand)
                reversed_random = random_numbers[::-1]            
    with open(rules,"w+") as writting:
        writting.write(f"3.The Number Is In Range {reversed_random}\n")
        writting.write(f"4.The Number For Game Over Is  {end_val}\n")
        writting.write(f"5.The Number For Award Winning Is  {award_val}\n")
    guess_number = random.randint(int(reversed_random[0][0]), int(reversed_random[0][1]))
    user_try = 0
    award = 0
    while True:
        try:
            num_Ask = int(input(f"Enter Guess Number Between {reversed_random[0][0]}-{reversed_random[0][1]} (enter 0 to exit from game) :"))
            if num_Ask == 0:
                print("Thanks for playing Guess The Number! The game is wrapping up now. We hope you had a blast in Raza's Gaming Arena!  See you again soon for more excitement and challenges!")
                print()
                return
            if num_Ask > guess_number:
                print("Your Guess Number Is High!!")
                print()
                user_try += 1
                with open(file_for_Admin_exit) as ending:
                    for line in ending:
                        end_no = line.strip().split(",")
                        end_no.sort(reverse=True)
                        end_val = int(end_no[0])
                if user_try == end_val:
                    print()
                    print(f"OOPS {name} You Lose The Game!!")
                    print()
                    print(" Thanks for playing Guess The Number! The game is wrapping up now.")
                    print("TRY AGAIN")
                    print()
                    exit()
            elif num_Ask < guess_number:
                print("Your Guess Number Is  low")
                print()
                user_try += 1
                with open(file_for_Admin_exit) as ending:
                    for line in ending:
                        end_no = line.strip().split(",")
                        end_no.sort(reverse=True)
                        end_val = int(end_no[0])
                if user_try == end_val:
                    print()
                    print(f"OOPS {name} You Lose The Game!!")
                    print()
                    print("TRY AGAIN")
                    print(" Thanks for playing Guess The Number! The game is wrapping up now.")
                    exit()
            elif num_Ask == guess_number:
                print(f"Congratulations {name} You win the game!!")
                print()
                user_try += 1
                print(f"You Total take {user_try} attempts to win the Game")
                print()

                print()
                print()
                with open(file_for_Admin_award) as new:
                    for line in new:
                        new_num = line.strip().split(",")
                        new_num.sort(reverse=True)
                        award_val = int(new_num[0])
                if user_try <= award_val:
                    print(f"OHH!!! {name} You Won THe Award As You Guess In {user_try} attempts")
                    print()
                    award += 1
                if user_try < min_score:
                    print(f"CONGRATULATIONS {name} you Are A New Champion !!")
                    print("You Break The Previous Record And Set New One")
                    print()
                elif user_try <= min_score:
                    print(f"CONGRATULATIONS {name} you Are Now IN A List Of Champions !!")
                    print("You Level The Previous Record And Get Name In List")

                    print()
                with open(file_for_score, "a+") as score:
                    score.write(f"{name}{x}{user_try}\n")
                with open(file_for_user, "a+") as file:
                    file.write(f"{current_time_value}{x}{curr_name}{x}{user_try}{x}{award}\n")
             
                exit()
        except ValueError:
            print("Please Enter a valid Number")