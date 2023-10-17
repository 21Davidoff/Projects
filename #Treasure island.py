#Treasure island, choose your own adventure!

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You are at a crossroads, do you want to go Left or Right?\n")

c1 = choice1.lower()

if c1 == "right" :
    print("The crossroads demon found you. Game over. :( ")
elif c1 == "left" :
    choice2 = input("You find a lake, do you swim or wait for a boat?\n")
    c2 = choice2.lower()
    if c2 == "swim" :
        print("You try to swim, but the crocodiles catch you. Game over. :( ")
    elif c2 == "wait" :
        print("You have waited and a boat came, it takes you to the other side and you find an abandoned pirate fortress.")
        choice3 = input("There are 3 doors. Red, Blue, Yellow. Which will you open?\n")
        c3 = choice3.lower()
        if c3 == "red" :
            print("You open the red door and...")
            print("You get engulfed in flames... it was a fire trap... Game over. :( ")
        elif c3 == "blue" :
            print("You open the blue door and...")
            print("You get pierced by arrows! It was a trap... Game over. :( ")
        elif c3 == "yellow" :
            print("You open the yellow door and...")
            print("There it is! The treasure! Congratulations adventurer, you have found a chest filled with gold coins! :) ")
        else:
            print("Misinput.")
    else:
        print("Misinput.")
else:
    print("Misinput.")