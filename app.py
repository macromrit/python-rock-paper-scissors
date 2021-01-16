#constructing stone paper scissors......
#emojis pasted from https://getemoji.com/

#import random for random outcomes from the computer
import random

#creating a infinite loops to make the user play as much as he wants to and end the game whenever required
while True:
    #assigning the value to choose between randomly by the computer
    low = 1
    max = 3
    
    #making computer guess a number within the given number /\ notice randint is not a range fixture i.e it does use the syntax of range/\
    #computer_guess is under while loop cause it helps in togling the number change as the user could experience a real gaming ambience
    computer_guess = random.randint(low, max)
    #test version of computers guess 
    guess_available = {1: "scissors",
                        2: "paper",
                        3: "stone"}

    #emoji version of computers guess
    guess_emojised = {"scissors": "✌",
                        "paper": "🖐",
                        "stone": "✊"}
                        
    #available answers
    available_answers = ["scissors", "paper", "stone"]
                        


    points_count = 0#to check the points and produce them as a output alsoknown as prestatement for while loops

    while True:
        try:
            manual_answer = str(input("please input a guess between stone, paper or scissors : ")).casefold()
            break
        except (EOFError, KeyboardInterrupt):
            print()
            print("please give a valid input")
            print()

    if manual_answer == "end": 
        print(F"the total points you scored was {points_count}")
        break
    
    elif manual_answer in available_answers:
        #for scissors
        if manual_answer == "scissors":
            if guess_available[computer_guess] == "scissors":
                print(F"""
computers guess was {guess_emojised["scissors"]}
your guess was "scissors" so you drew a point
                """)
                points_count += 0#drawn
            
            elif guess_available[computer_guess] == "stone":
                print(F"""
computers guess was {guess_emojised["stone"]} 
your guess was "scissors" so you lost a point        
                """)
                points_count -= 1#lost
            
            elif guess_available[computer_guess] == "paper":
                print(F"""
computers guess was {guess_emojised["paper"]}
your guess was "scissors" so you won a point        
                """)
                points_count += 1#won
            
            else:
                print("Oops!!, something went wrong")
        
        #for stone
        elif manual_answer == "stone":
            if guess_available[computer_guess] == "scissors":
                print(F"""
computers guess was {guess_emojised["scissors"]}
your guess was "stone" so you won a point        
                """)
                points_count += 1#won
            
            elif guess_available[computer_guess] == "stone":
                print(F"""
computers guess was {guess_emojised["stone"]}         
your guess was "stone" so you drew a point        
                """)
                points_count =+ 0#drawn
            
            elif guess_available[computer_guess] == "paper":
                print(F"""
computers guess was {guess_emojised["paper"]}
your guess was "stone" so you lost a point        
                """)
                points_count -= 1#lost
            
            else:
                print("Oops!!, something went wrong")
        
        #for paper
        if manual_answer == "paper":
            if guess_available[computer_guess] == "scissors":
                print(F"""
computers guess was {guess_emojised["scissors"]}
your guess was "paper" so you lost a point        
                """)
                points_count -= 1#lost
            
            elif guess_available[computer_guess] == "stone":
                print(F"""
computers guess was {guess_emojised["stone"]}     
your guess was "paper" so you won a point            
                """)
                points_count += 1#won
            
            elif guess_available[computer_guess] == "paper":
                print(F"""
computers guess was {guess_emojised["paper"]}
your guess was "paper" so you drew a point        
                """)
                points_count += 0#drawn
            
            else:
                print("Oops!!, something went wrong")

    else:
        print("please give a valid input")

