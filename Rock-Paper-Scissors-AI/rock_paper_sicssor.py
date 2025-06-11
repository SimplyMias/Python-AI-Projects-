import random

options = ['rock','paper','scissors']

user_score = 0
ai_score = 0
tie_score = 0

while True:
    user_input = input("-----Hey I am Jarvis. let's play Rock-Paper-Scissor----- \n Type rock, paper, scissor (or q to quite): ").lower()

    if user_input=='q':
        print("\nGame Over!")
        print("🎯 Final Score:")
        print("You: ", user_score)
        print("Jarvis: ", ai_score)
        print("Ties: ",tie_score)

        break
    
    if user_input not in options:
        print("Invalid input! Please choose rock, paper or scissors")
        continue


    ai_choice = random.choice(options)

    print("\nyour choice: ",user_input)
    print("Jarvis choice: ",ai_choice)

    if user_input==ai_choice:
       print("\nIt's a tie\n")
       tie_score +=1
    elif user_input == "rock":
       if ai_choice == "scissors":
           print("\nYou win\n")
           user_score +=1
       else:
           print("\nJarvis Wins\n")
           ai_score +=1
    elif user_input == "paper":
        if ai_choice == "rock":
           print("\nYou win\n")
           user_score +=1
        else:
           print("\nJarvis Wins\n")
           ai_score+=1
    elif user_input == "\nscissors\n":
        if ai_choice == "paper":
           print("\nYou win\n")
           user_score+=1
        else:
           print("\nJarvis Wins\n")
           ai_score +=1
print(f"score => You: {user_score}, Jarvis: {ai_score}, Ties: {tie_score}\n")
if user_score>ai_score:
    print("--------You are FInal Winner--------")
elif user_score<ai_score:
    print("--------Jarvis is FInal Winner--------")
else:
    print("----Ties----")