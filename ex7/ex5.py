def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(x, y):
    print(f"state: {x}, capital: {y}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("Alh Bundi")

print_two("Mijin", "Hajiya")
print_two_again("Borno", "Biu")
print_one("Bundi")
print_none()
