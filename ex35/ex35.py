from sys import exit

def gold_room():
    print("This is full of gold, How much willl u take?")

    choice = input("Enter Number>")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Bro learn to insert number")

        if how_much < 50:
            print("NIce you ain't greedy")
            exit(0)
        else:
            dead("You are greedy!")

def bear_room():
    print("There's a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in form=nt of a another door.")
    print("How are you going to move out of the door?")
    bear_moved = False

    while True:
        choice = input(">")
        if choice == "take honey":
            dead(" The bear looks at you the dead guy")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear get pissed and eats u")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means!")
            exit(0)
def cthlhu_room():
        print("Here you see the great eveil Cthulhu.")
        print("He, it, whatever startes at you you and you go insane")
        print("Do you flee for your life or eat ur head")

        choice = input(">")
        if "flee" in choice:
            start()
        elif "head" in choice:
            dead("well that was tasty")
        else:
            cthlhu_room()
def dead(why):
        print(why, "Good job")
        exit(0)

def start():
        print(" You are in a dark room")
        print("There is a door to your right and left")
        print("Which one do u take")

        choice = input(">")
        if choice == "left":
            bear_room()
        elif choice == "right":
            cthlhu_room()
        else:
            dead(" You stumble around the room ")
start()
