list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        line_locations = line.strip().split("   ")
        list1.append(int(line_locations[0]))
        list2.append(int(line_locations[1]))

list2.sort()

similarity_score = 0
for i in list1:
    multiplied_value = i * list2.count(i)
    similarity_score = similarity_score + multiplied_value
    
print(similarity_score)