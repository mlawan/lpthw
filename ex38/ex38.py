ten_things = " Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("Wait there are not 10 things in that list. Lets fix it.")

stuff = ten_things.split(' ')
more_stuff = [ "Day", "NIght", "SOng", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = pop(more_stuff)
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go : ", (stuff))
print("Lets do some things with stuff")

print("first stuff", stuff[1])
print("second stuff", stuff[-2])
print("show me stuff.pop()", stuff.pop())
print(' '. join(stuff), "join command")
print('#'.join(stuff[3:5]))
