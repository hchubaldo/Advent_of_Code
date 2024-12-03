def asc_desc(report, key = lambda x: x):
    asc = all(key(report[i]) <= key(report[i + 1]) for i in range(len(report) - 1))
    desc = all(key(report[i]) >= key(report[i + 1]) for i in range(len(report) - 1))
    if asc or desc:
        return True
    else:
        return False

def problem_1(reports):
    count_safe = 0
    for report in reports:
        list_count = 1
        report_diffs = []
        if asc_desc(report, key = int):
            for num in report:
                if list_count < len(report):
                    val_1 = num
                    val_2 = report[report.index(num) + 1]
                    list_count += 1
                    diff = abs(int(val_1) - int(val_2))
                    report_diffs.append(diff)
                else:
                    continue
        if len(report_diffs) >= 1:
            if min(report_diffs) > 0 and max(report_diffs) < 4:
                print(report)
                count_safe += 1

    return count_safe

def main():
    reports = []

    with open('/Users/hchubaldo/Documents/Advent_of_Coding/hugo/DAY_2/day2_input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')
            reports.append(line)

    ans = problem_1(reports)

    print(ans)

if __name__ == '__main__':
    main()