#constructing stone paper scissors......
#import random for random outcomes from the computer
import random
points_count = 0
#creating a definition
def mainpoints(cg : str, yg : str, lwd: str):
    print(F"The computers guess was {guess_emojised[cg]}, you your guess was {yg}, you {lwd} as point")
def subpoints(points: int):
    print(F"The current points you scored is {points}")
#creating a infinite loops to make the user play as much as he wants to and end the game whenever required
while True:
    #assigning the value to choose between randomly by the computer
    low = 1
    max = 3
    computer_guess = random.randint(low, max)
    #test version of computers guess 
    guess_available = {1: "scissors",
                        2: "paper",
                        3: "stone"}
    #emoji version of computers guess
    guess_emojised = {"scissors": "scissors",
                        "paper": "paper",
                        "stone": "stone"}   
    #available answers
    available_answers = ["scissors", "paper", "stone"]
    #to check the points and produce them as a output alsoknown as prestatement for while loops
    while True:
        try:
            manual_answer = str(input("please input a guess between stone, paper or scissors and 'end' to quit game : ")).casefold()
            break
        except (EOFError, KeyboardInterrupt):
            print()
            print("please give a valid input")
    if manual_answer == "end": 
        print(F"the total points you scored was {points_count}")
        break
    elif manual_answer in available_answers: 
        #for scissors
        if manual_answer == "scissors":
            if guess_available[computer_guess] == "scissors":
                mainpoints("scissors", "scissors", "drew")
                points_count += 0#drawn
                subpoints(points_count)
            elif guess_available[computer_guess] == "stone":
                mainpoints("stone", "scissors", "lost")
                points_count -= 1#lost
                subpoints(points_count)
            elif guess_available[computer_guess] == "paper":
                mainpoints("paper", "scissors", "won")
                points_count += 1#won
                subpoints(points_count)
            else:
                print("Oops!!, something went wrong")
        #for stone
        elif manual_answer == "stone":
            if guess_available[computer_guess] == "scissors":
                mainpoints("scissors", "stone", "won")
                points_count += 1#won
                subpoints(points_count)
            elif guess_available[computer_guess] == "stone":
                mainpoints("stone", "stone", "drew")
                points_count += 0#drawn
                subpoints(points_count)
            elif guess_available[computer_guess] == "paper":
                mainpoints("paper", "stone", "lost")
                points_count -= 1#lost
                subpoints(points_count)
            else:
                print("Oops!!, something went wrong")
        #for paper
        if manual_answer == "paper":
            if guess_available[computer_guess] == "scissors":
                mainpoints("scissors", "paper", "lost")
                points_count -= 1#lost
                subpoints(points_count)            
            elif guess_available[computer_guess] == "stone":
                mainpoints("stone", "paper", "won")
                points_count += 1#won
                subpoints(points_count)            
            elif guess_available[computer_guess] == "paper":
                mainpoints("paper", "paper", "drew")
                points_count += 0#drawn
                subpoints(points_count)          
            else:
                print("Oops!!, something went wrong")
    else:
        print("please give a valid input")
#The End!!! Thankyou#
