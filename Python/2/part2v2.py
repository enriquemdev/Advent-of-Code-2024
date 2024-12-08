def main ():
    safe_reports_qty = 0

    with open('input.txt', 'r') as file:
        for line in file:
            report = line.strip().split(' ')
            report = list(map(int, report))

            if check_safety(report):
                safe_reports_qty = safe_reports_qty + 1
            else: #If the report itself isnt valid, try deleting one item one at a time to check if then it is valid
                for i in range(len(report)):
                    reports_copy = report.copy()
                    reports_copy.pop(i)
                    if (check_safety(reports_copy)):
                       safe_reports_qty = safe_reports_qty + 1 # if exists the case when deleting an item it becomes valid, then sum 1
                       break # No need to keep searching as the report is now considered valid no matter what
                        
        
        print(safe_reports_qty)

def check_safety(report):
    for i in range(len(report) - 1): # Ends in the penultimate item
        a, b = report[i], report[i + 1]
        diff = abs(a - b)

        if not 3 >= diff >= 1: # If diff isnt less or equal than three nor more or equal than one
            return False
        
        if i != len(report) - 2:
            c = report[i + 2]
            
            if not a < b < c and not a > b > c: # If there isnt a segment of the list wich the 3 items have the same direction(up or down)
                return False
    return True


main()