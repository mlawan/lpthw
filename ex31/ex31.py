print(""" You enter a dark room with two doors
Do you go though door #1 or door #2? """)

door = input("enter number>")

if door == "1":
    print("There's a giant bear here eating cheese")
    print("What will u do?")
    print("1. Take the cheese")
    print("2. Sceeam for help")

    bear = input("Enter number>")
    if bear == "1":
        print("The beat eats your face off, Good job!")
    elif bear == "2":
        print("The bear eats your legs off")
    else:
        print(f"well, doint {bear} is probably the best")
        print("bear runs away")
elif door == "2":
        print("You stare into the endless abyss, choice option below")
        print("1. Blueberries")
        print("2. Yellow jacket clothespins.")
        print("3. understanding revolvers yelling")
        insanity = input(">")
        if insanity == "1" or insanity =="2":
            print ("your body survic=ves powered by a mind of jetto")
            print("Good job!")
        else:
            print("The insanity rots your eyes with love")
            print("Good job!")

else:
    print("You stumble around and fall on a cliff")
