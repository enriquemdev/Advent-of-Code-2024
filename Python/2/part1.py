def main():
    safe_reports_count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            report_list = line.strip().split(' ')
            report_list = [int(item) for item in report_list]

            if (check_consistency(report_list) and check_graduality(report_list)):
                safe_reports_count = safe_reports_count + 1

    print(safe_reports_count)


def check_consistency(report_list):
    defined_mode = None
    for i in range(len(report_list) - 1):
        if report_list[i] < report_list[i + 1]:
            current_mode = 'increasing'
        elif report_list[i] == report_list[i + 1]:
            return False # If it isnt increasing nor decrasing, it is unsafe
        else:
            current_mode = 'decreasing'
        
        if i == 0:
            defined_mode = current_mode
        else:
            if defined_mode != current_mode:
                return False
    return True

def check_graduality(report_list):
    for i in range(len(report_list) - 1):
        diff_adjacent = abs(report_list[i] - report_list[i + 1])
        if not(diff_adjacent >= 1 and diff_adjacent <= 3):
            return False
    return True

main()