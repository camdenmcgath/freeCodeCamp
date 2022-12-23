def arithmetic_arranger(problems, answers=False):
    eqval = True
    worklist = []
    # Checking if list contains valid equations
    if len(problems) > 5:
        return "Error: Too many problems."
    worklist = [x.split() for x in problems]
    for x in worklist:
        if x[1] != '+' and x[1] != '-':
            eqval = False
            return "Error: Operator must be '+' or '-'."
        if len(x[0]) > 4 or len(x[2]) > 4:
            eqval = False
            return "Error: Numbers cannot be more than four digits."
        if x[0].isdigit() is False or x[2].isdigit() is False:
            eqval = False
            return "Error: Numbers must only contain digits."
    # Formatting equations
    line1 = ""
    line2 = ""
    bar = ""
    solutions = ""
    if eqval:
        width = 0
        for x in worklist:
            if len(x[0]) > len(x[2]):
                width = len(x[0]) + 2
            else:
                width = len(x[2]) + 2
            for i in range(width):
                bar += '-'
            if x != worklist[-1]:
                bar += "    "
                line1 += x[0].rjust(width) + "    "
                line2 += x[1] + x[2].rjust(width - 1) + "    "
                if x[1] == "+":
                    solutions += str(int(x[0]) +
                                     int(x[2])).rjust(width) + "    "
                else:
                    solutions += str(int(x[0]) -
                                     int(x[2])).rjust(width) + "    "
            else:
                line1 += x[0].rjust(width)
                line2 += x[1] + x[2].rjust(width - 1)
                if x[1] == "+":
                    solutions += str(int(x[0]) + int(x[2])).rjust(width)
                else:
                    solutions += str(int(x[0]) - int(x[2])).rjust(width)
    #Output
    if answers:
        arrangedproblems = line1 + "\n" + line2 + "\n" + bar + "\n" + solutions
    else:
        arrangedproblems = line1 + "\n" + line2 + "\n" + bar
    return arrangedproblems
