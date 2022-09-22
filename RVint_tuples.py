# Ryan Vint 08/25/2022 Module 4 Assignment: Tuples
# This program is a tuple showing the functions that can be used such as displaying the contents, iterating through the collection both ways, and displaying a nice output

football_teams = ('panthers','patriots','browns','jets','titans','cardinals','bengals','giants','packers','cheifs','raiders','commanders','dolphins','bengals','saints','cowboys','texans','chargers','falcons','buccaneers')
print(f'\n{football_teams}\n')

for x in football_teams:
    print(x)

print()

for i in range(len(football_teams)):
    print(football_teams[-(i+1)])