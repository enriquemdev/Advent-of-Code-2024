# 265 low - 636 high
counter = 1
def main():
    global counter
    safe_reports_count = 0
    with open('input.txt', 'r') as file:
        
        for line in file:
            report_list = line.strip().split(' ')
            report_list = [int(item) for item in report_list]
            
            

            if (check_consistency(report_list, True) and check_graduality(report_list, True)):
                safe_reports_count = safe_reports_count + 1
                # if counter == 678:
                #     print('raro 1 ')
                # if counter == 754:
                #     print('raro 2')
            counter = counter + 1
    print(safe_reports_count)


def check_consistency(report_list, is_first_run):
    global counter
    defined_mode = None
    dampener_saved = False
    for i in range(len(report_list) - 1):
        
        if report_list[i] < report_list[i + 1]:
            
            current_mode = 'increasing'
        elif report_list[i] == report_list[i + 1]:
        
            if not is_first_run:
                return False
            
            # print('hmmm')

            if is_first_run and not dampener_saved:
                if does_problem_dampener_saves(report_list, i):
                    dampener_saved = True

                    # edge case: first 2 items are equal so mode is not defined.
                    if len(report_list) >= i + 3: # 3 for one more of the i+2
                        if report_list[i + 1] < report_list[i + 2]:
                            current_mode = 'increasing'
                            # print("line: " + str(counter))
                        elif report_list[i] == report_list[i + 1]:
                            return False # Cannot save from two equal values more than once
                            # print("line: " + str(counter))
                        else:
                            current_mode = 'decreasing'
                else:
                    return False
            else:
                return False   
            

        else:
            current_mode = 'decreasing'
        
        if i == 0:
            defined_mode = current_mode
            # if counter== 678:
            #     print(i, report_list[i], report_list[i + 1], defined_mode, current_mode)
        else:
            # if counter== 678:
            #     print(i, report_list[i], report_list[i + 1], defined_mode, current_mode)
            if defined_mode != current_mode:
                if is_first_run and not dampener_saved:
                    if does_problem_dampener_saves(report_list, i):
                        dampener_saved = True
                    else:
                        return False
                else:
                    return False
    return True

def check_graduality(report_list, is_first_run):
    dampener_saved = False
    for i in range(len(report_list) - 1):
        diff_adjacent = abs(report_list[i] - report_list[i + 1])
        if not(diff_adjacent >= 1 and diff_adjacent <= 3):
        
            if is_first_run and not dampener_saved:
                if does_problem_dampener_saves(report_list, i):
                    dampener_saved = True
                else:
                    return False
            else:
                return False           
    return True

# removes one level of the report (element of the list) to check if then the report is safe
def does_problem_dampener_saves (report_list, index):
    report_list_copy = report_list.copy()
    report_list_copy.pop(index)

    # if counter == 678:
    #     print(report_list_copy)

    if (check_consistency(report_list_copy, False) and check_graduality(report_list_copy, False)):
        return True
    else:
        return False

main()