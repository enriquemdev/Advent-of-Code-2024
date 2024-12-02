list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        line_locations = line.strip().split("   ")
        list1.append(int(line_locations[0]))
        list2.append(int(line_locations[1]))

list1.sort()
list2.sort()

total_distance = 0
for i in range(1000): # from 0 to 999
    total_distance = total_distance + abs(list1[i] - list2[i])
    
print(total_distance)