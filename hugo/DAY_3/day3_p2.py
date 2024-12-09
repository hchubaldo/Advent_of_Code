import regex as re

def pattern_found(line):
    ans = 0
    pattern_remove = r"don't\(\).*?do\(\)"
    line = re.sub(pattern_remove, '', line)
    pattern_mul = r"mul\((\d+),(\d+)\)"
    for nums in re.findall(pattern_mul, line):
        print(nums)
        num1, num2 = int(nums[0]), int(nums[1])
        mult_ans = num1 * num2
        ans += mult_ans

    return ans

def main():
    total = 0
    with open('/Users/hchubaldo/Documents/Advent_of_Coding/hugo/DAY_3/day3_input.txt', 'r') as f:
        long_line = ' '.join([line.rstrip('\n') for line in f])
        total += pattern_found(long_line)
    
    print(total)

if __name__ == '__main__':
    main()