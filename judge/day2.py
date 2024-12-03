DAY_2_INPUT_FILE = "/Users/bm/repos/advent/data/day_2_input.txt"

count = 0
with open(DAY_2_INPUT_FILE, "r") as f:
    
    text = f.readlines()
    for line in text:

        str_tmp_input = line.split("\n")[0].split(" ")
        tmp_input = [int(x) for x in str_tmp_input]
        length =  len(tmp_input)
        print("start")

        # Figure out if increasing or decreasing
        if tmp_input[0] < tmp_input[1]:
            increasing = True
        elif tmp_input[0] > tmp_input[1]:
            increasing = False
        else:
            # Should handle case when equal and skip this skip
            print("equal found")
            continue
            
        
        # Check the level if valid
        for idx in range(1, length):
            valid = False
            if (increasing and tmp_input[idx-1] < tmp_input[idx]) or (not increasing and tmp_input[idx-1] > tmp_input[idx]):
                if 1 <= abs(tmp_input[idx-1] - tmp_input[idx]) <= 3:
                    valid = True
                else:
                    valid = False
                    break
            else:
                valid = False
                break
        if valid:
            count += 1
            print(tmp_input[idx])
        print("done")
print(count)