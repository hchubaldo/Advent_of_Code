import regex as re

def pattern_found(line):
    ans = 0
    pattern = r"mul\((\d+,\d+)\)"
    for nums in re.findall(pattern, line):
        num1, num2 = map(int, nums.split(','))
        mult_ans = num1 * num2
        ans += mult_ans

    return ans

def main():
    total = 0
    with open('/Users/hchubaldo/Documents/Advent_of_Coding/hugo/DAY_3/day3_input.txt', 'r') as f:
        for line in f.readlines():
            total += pattern_found(line)
    
    print(total)
            


if __name__ == '__main__':
    main()