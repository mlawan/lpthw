# creates a mapping to state to abbreviation
states ={
'Oregon': 'OR',
'Florida' : 'FL',
'CAlifornia' : 'CA',
'Konduga' : 'KDG',
'Maiduguri': 'Mag'
}
#creats a babsic set of states and some cities in them
cities = {
'CA': 'SanfranCisco',
'KDG': 'Sandiya',
'FL': 'Florida',
'Mag': 'MMC'
}

#ADD SOME MORE cities
cities['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out some cities
print('*'* 20)
print("NY State has:", cities ['NY'])
print("OR State has:", cities['OR'])
print("Borno state has:", cities['KDG'])
#print("Borno State has:", states)

#print some states
print('*' * 20)
print("Maiduguri's abbreviation is:" , states['Maiduguri'])
print("Florida's abbreviation is:" , states['Florida'])

#do it by using the state then cities dict
print('-' * 20)
print("Maiduguiri has:", cities [states['Maiduguri']])
print ("Florida has:" , cities[states['Florida']])

#print every state abbreviation
print('*' *20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print("+" *20)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('=' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} state abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('~'*20)
# safely get a abbreviatedby state that might not be There
state = states.get("Texas")

if not state:
    print("Sorry , no Texas")

#get a city with a defalut value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX'is {city}")
