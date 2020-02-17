print("Lets practice everything we have learn")
print('You\'d need to know \bout excapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely wife and car
with good food and family
cannot escape the pleasure of Allah \n
nor compare to heaven
\n\t hwere he pray.
"""
print("------------------------------")
print(poem)


five = 10 - 2 + 3 - 6
print(f"This should be answer: {five}")

def secret_formula(started):
    jelly_beans = started * 100
    jars = jelly_beans / 200
    crates = jars /10
    print(f"jelly_beans:{jelly_beans}\n jars:{jars}\n crates:{crates}")
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With this starting point of : {}".format(start_point))
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point / 10
