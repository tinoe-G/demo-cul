from random import randint


choices=["rock","paper","scissers"]

computer=choices[randint(0,2)]

print("lets play rock paper scissers ")

player=input("enter your choice :")

print("computer ",computer)

if player==computer:
    print("draw")
elif player=="rock" and computer=="paper":
    print("computer wins")
elif player=="rock" and computer=="scissers":
    print("player wins")
elif player=="paper" and computer=="rock":
    print("player wins")

elif player=="paper" and computer=="scissers":
    print("computer wins")

elif player=="scissers" and computer=="rock":
    print("computer wins")

elif player=="scissers" and computer=="paper":
    print("player wins")