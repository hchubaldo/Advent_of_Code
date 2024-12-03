DAY_2_INPUT_FILE = "/Users/bm/repos/advent/data/day_2_input.txt"

count = 0
tmp_count=0
with open(DAY_2_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:

        str_tmp_input = line.split("\n")[0].split(" ")
        tmp_input = [int(x) for x in str_tmp_input]
        length =  len(tmp_input)

        valid = False

        if (tmp_input == sorted(tmp_input, reverse=False)) or (tmp_input == sorted(tmp_input, reverse=True)):
             # Check the level is valid for min max difference
             
            tmp_count += 1 #Ignore this is for debugging only

            for idx in range(1, length):
                if 1 <= abs(tmp_input[idx-1] - tmp_input[idx]) <= 3:
                    valid = True
                else:
                    valid = False
                    break
        if valid:
            count += 1

print(tmp_count)
print(count)