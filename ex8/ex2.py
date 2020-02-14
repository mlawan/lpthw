from sys import argv

script, input_file = argv

def print_all(script, f):
    print(script, f.read())

def rewind(f):
    f.seek(0) #command to forwand (seeking)

def print_a_line (line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First lets print the whole file:\n")

print_all(script, current_file)

print("print rewind file, tape yeah")
rewind(current_file)

print("lets print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
