DAY_1_INPUT_FILE = "/workspaces/Advent_of_Coding/judge/data/day_1_input.txt"
list_1 = []
list_2 = []

with open(DAY_1_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:

        tmp_input = line.split("\n")[0].split("  ")
        list_1.append(int(tmp_input[0].strip()))
        list_2.append(int(tmp_input[1].strip()))

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

## Calculate the distance between the two lists
distance = 0
for idx in range(len(sorted_list_1)):
    distance += abs(sorted_list_1[idx] - sorted_list_2[idx])

print(f"Distance: {distance}")

## Calculate the similarity between the two lists
similarity = 0

for number in sorted_list_1:
    similarity += number*sorted_list_2.count(number)

print(f"Similarity: {similarity}")