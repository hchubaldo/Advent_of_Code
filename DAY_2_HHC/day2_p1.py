def problem_1(reports):
    count_safe = 0
    for report in reports:
        for num in report:
            val_1 = num
            val_2 = (num.index() + 1)
            


    return count_safe

def main():
    reports = []

    with open('/Users/hchubaldo/Documents/Advent_of_Coding/DAY_2_HHC/day2_input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')
            reports.append(line)

    ans = problem_1(reports)

    #print(ans)

if __name__ == '__main__':
    main()