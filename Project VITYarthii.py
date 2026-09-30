import random

name=input("Enter your Name:")
print("Hi",name)

wins=0
losses=0
draws=0

options=["Rock","Paper", "Scissors"]
for i in range (1,4):
    print("\nRound", i)

    choice=input("Choose - Rock, Paper or Scissors :").capitalize()
    

    while choice not in options:
        print("Invalid choice! Try again.")
        choice = input("Choose Rock, Paper or Scissors: ").capitalize()
    print("You Choose:",choice)

    computer=random.choice(options)
    print("Computer choose:",computer)

    if(choice==computer):
        print("It's a Draw")
        draws += 1
    elif(choice=="Rock" and computer=="Paper"):
        print("You Lost")
        losses += 1

    elif(choice=="Rock" and computer=="Scissors"):
        print("You win")
        wins += 1

    elif(choice=="Paper" and computer=="Rock"):
        print("You Win")
        wins += 1

    elif(choice=="Paper" and computer=="Scissors"):
        print("You Lost")
        losses += 1

    elif(choice=="Scissors" and computer=="Rock"):
        print("You Lost")
        losses += 1

    elif(choice=="Scissors" and computer=="Paper"):
        print("You Win")    
        wins += 1


print("\n====== FINAL SCORE ======")
print("Player:", name)
print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)