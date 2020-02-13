def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("we got enough for the party")
    print("HurraY!")

print("we can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("Or, we can use variables form our script")
amount_of_cheese = 33
amount_of_crackers = 35
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do maths inside too")
cheese_and_crackers(20 + 30, 15 + 20)

print("furthermore, we can combine the two variables and math")
cheese_and_crackers(amount_of_crackers +50, amount_of_cheese + 20)
