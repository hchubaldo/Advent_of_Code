import re

DAY_3_INPUT_FILE  = "/Users/bm/repos/Advent_of_Code/judge/data/day_3_input.txt"
REGEX_PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'
              
input_string = ''
count = 0

with open(DAY_3_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:
        input_string += line

pairs = re.findall(REGEX_PATTERN, input_string)

for pair in pairs:
    count += int(pair[0]) * int(pair[1])

print(f"Part 1 Count: {count}")

matches = []

# Find mul expressions with number pairs
mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
for match in re.finditer(mul_pattern, input_string):
    matches.append((match.start(), (int(match.group(1)), int(match.group(2)))))

# Find don't() and do() expressions
command_pattern = r"don't\(\)|do\(\)"
for match in re.finditer(command_pattern, input_string):
    # Remove the () from the match
    command = match.group()[:-2]
    matches.append((match.start(), command))

pairs = [m[1] for m in sorted(matches, key=lambda x: x[0])]

#print(pairs)

# 1 = True and 0 = False
do = 1
count =0
for pair in pairs:

    if pair == "don't":
        do = 0
    elif pair == "do":
        do = 1

    if do == 1 and isinstance(pair, tuple):
        count += pair[0] * pair[1]

print(f"Part 2 Count: {count}")
