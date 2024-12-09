DAY_2_INPUT_FILE = "/Users/bm/repos/Advent_of_Code/judge/data/day_2_input.txt"

count = 0
tmp_count=0



with open(DAY_2_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:

        str_tmp_input = line.split("\n")[0].split(" ")
        tmp_input = [int(x) for x in str_tmp_input]
        length =  len(tmp_input)

        # Figure out if increasing or decreasing
        origin_input = [int(x) for x in str_tmp_input]
        for i in range(length):
            if  not (sorted(tmp_input) == tmp_input or sorted(tmp_input, reverse=True) == tmp_input):
                continue

            # Check the level if valid
            for idx in range(1, length):
                valid = False
                if 1 <= abs(tmp_input[idx-1] - tmp_input[idx]) <= 3:
                    valid = True
                else:
                    valid = False
                    break

            if valid:
                count += 1
            break

print(f"Part 1 Count: {count}")

count = 0
tmp_count=0


with open(DAY_2_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:

        str_tmp_input = line.split("\n")[0].split(" ")
        tmp_input = [int(x) for x in str_tmp_input]
        length =  len(tmp_input)

        # Figure out if increasing or decreasing
        origin_input = [int(x) for x in str_tmp_input]

        for i in range(length+1):
            if  not (sorted(tmp_input) == tmp_input or sorted(tmp_input, reverse=True) == tmp_input):
                tmp_input = origin_input.copy()
                if i <length:
                    tmp_input.pop(i)
                    continue

                else:
                    break
            
            # Check the level if valid
            for idx in range(1, len(tmp_input)):
                valid = False
                if 1 <= abs(tmp_input[idx-1] - tmp_input[idx]) <= 3:
                    valid = True
                else:
                    valid = False
                    break

            if valid:
                count += 1
                break
            else:
                if i <length:
                    tmp_input = origin_input.copy()
                    tmp_input.pop(i)
                else:
                    break

print(f"Part 2 Count: {count}")


