people = 30
cars = 40
trucks = 40

if cars > people or trucks < cars:
    print("We should take the cars")
elif cars< people:
    print("We should not take the cars")

else:
    print(" We cant decide.")
if trucks > cars and cars == trucks:
    print("Thats too much of trucks")

elif trucks <cars:
    print("Maybe we could take the trucks")

else:
    print(" We still can't decide")
if cars == trucks and  cars > people:
    print("Alrifht, lets jsut take the trucks")
else:
    print("fine, lets stay home then.")
