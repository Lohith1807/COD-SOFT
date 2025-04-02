import random
choice=["rock","paper","scissor"]
user=input("enter your choice")
computer=random.choice(choice)
if user==computer:
    print("Its a tie")
elif user=="rock":
    if computer=="scissor":
        print("you win")
    else:
        print("you lose")
elif user=="paper":
    if computer=="rock":
        print("you win")
    else:
        print("you lose")
elif user=="scissor":
    if computer=="paper":
        print("you win")
    else:
        print("you lose")
else:
    print("invalid input")