def problem_1(tuple_a):
    list_a = []

    for i in tuple_a:
        list_a.append(i[0] - i[1])

    list_a = [abs(x) for x in list_a]
    sum_of_diff = sum(list_a)

    return sum_of_diff

def main():
    col_1 = []
    col_2 = []

    with open('/Users/hchubaldo/Documents/Advent_of_Coding/day_p1_input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n').split('   ')
            col_1.append(int(line[0]))
            col_2.append(int(line[1]))

    col_1.sort()
    col_2.sort()
    tuple_a = tuple(zip(col_1, col_2))

    ans = problem_1(tuple_a)

    print(ans)

if __name__ == '__main__':
    main()