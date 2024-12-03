def problem_2(col_1, col_2):
    list_a = []
    
    for num_1 in col_1:
        repeat_count = 0
        for num_2 in col_2:
            if num_1 == num_2:
                repeat_count += 1
        
        score = num_1 * repeat_count
        list_a.append(score)
    
    sim_score = sum(list_a)
        
    return sim_score

def main():
    col_1 = []
    col_2 = []

    with open('/Users/hchubaldo/Documents/Advent_of_Coding/DAY_1_HHC/day_p1_input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n').split('   ')
            col_1.append(int(line[0]))
            col_2.append(int(line[1]))

    ans = problem_2(col_1, col_2)

    print(ans)

if __name__ == '__main__':
    main()