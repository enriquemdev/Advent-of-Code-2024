def main ():
    safe_reports_qty = 0

    with open('input.txt', 'r') as file:
        for line in file:
            report = line.strip().split(' ')
            report = list(map(int, report))

            if check_safety(report):
                safe_reports_qty = safe_reports_qty + 1

def check_safety(report):
    for i in range(len(report) - 1):
        a, b = report[i], report[i + 1]
        diff = abs(a - b)

        if 1 > diff > 3:
            return False



main()