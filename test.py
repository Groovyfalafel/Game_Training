# Anything i wanna test goes here

map_data = open("map.txt", "r")
map = []

for i in map_data:
    i = i.strip()
    if i != "":
        row = [int(x) for x in i.split()]
        map.append(row)
        
print(map)