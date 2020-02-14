def add(a,b):
    print(f"Adding {a} +{b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f" Mulitiplcatio {a} * {b}")
    return  a * b

def divide(a, b):
    print(f"Diving {a} / {b}")
    return a / b

print(" Lets play with mahts")

age = add(30 , 20)
height = subtract(74, 4)
weight = multiply (20, 5)
iq = divide(100, 2)

print(f"age {age}\n height {height}\n, weight{weight}\n iq {iq}")

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))
print("thats becomes:", what, "can you do it by hand?")
