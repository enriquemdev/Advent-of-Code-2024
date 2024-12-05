# 265 low - 271 right answer to another person - 636 high
def main():
    safe_reports_count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            report_list = line.strip().split(' ')
            report_list = [int(item) for item in report_list]

            total_problems_list = check_consistency(report_list).union(check_graduality(report_list)) 
            
            if len(total_problems_list) == 0:
                safe_reports_count = safe_reports_count + 1
            elif len(total_problems_list) == 1:
                if problem_dampener_saves(report_list):
                    safe_reports_count = safe_reports_count + 1
                # elif problem_dampener_saves(report_list, next(iter(total_problems_list)) + 1):
                #     safe_reports_count = safe_reports_count + 1
            
    print(safe_reports_count)


def check_consistency(report_list):
    problem_ids = set()
    defined_mode = None
    first_valid_iteration = 0
    
    for i in range(len(report_list) - 1):
        if report_list[i] < report_list[i + 1]:
            current_mode = 'increasing'
        elif report_list[i] == report_list[i + 1]:
            problem_ids.add(i) # If it isnt increasing nor decrasing, it is unsafe
            if defined_mode == None:
                first_valid_iteration = first_valid_iteration + 1
        else:
            current_mode = 'decreasing'
        
        if i == first_valid_iteration:
            defined_mode = current_mode
        else:
            if defined_mode == None or defined_mode != current_mode:
                problem_ids.add(i)
    return problem_ids

def check_graduality(report_list):
    problem_ids = set()
    for i in range(len(report_list) - 1):
        diff_adjacent = abs(report_list[i] - report_list[i + 1])
        if not(diff_adjacent >= 1 and diff_adjacent <= 3):
            problem_ids.add(i)
    return problem_ids


def problem_dampener_saves (report_list):
    for i in range(len(report_list)):
        report_list_copy = report_list.copy()
        report_list_copy.pop(i)
        
        if check_consistency_og(report_list_copy) and check_graduality_og(report_list_copy):
            return True
        
    return False


def check_consistency_og(report_list):
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

def check_graduality_og(report_list):
    for i in range(len(report_list) - 1):
        diff_adjacent = abs(report_list[i] - report_list[i + 1])
        if not(diff_adjacent >= 1 and diff_adjacent <= 3):
            return False
    return True

main()