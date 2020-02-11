from sys import argv
script, filename = argv

print(f" we are going to erase {filename}")
print("press control CTRL + C to abort")
print("press enter to continue")

input('=>')

print ("opening file.........")
file = open(filename, 'a+')

print("truncating the file .... Goodbye!!!")
file.truncate()

print("Now lets write some note to the text")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("lets write those note to the file")
file.write(line1)
file.write('\n')
file.write(line2)
file.write('\n')
file.write(line3)

print("lets close the file")
file.close()
