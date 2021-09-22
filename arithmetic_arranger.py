def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error:Too many problems."

    arranged_problems = []

    for index, value in enumerate(problems):
        # ["32" + "8"]
        operation = value.split(" ")

        if operation[1] not in "-+":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            val1 = int(operation[0])
            val2 = int(operation[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        # len of each line with spaces
        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2

        # output = f"{operation[0]:>{width}}\n{f'{operation[1]} {operation[2]}':>{width}\n{'-'*width}}"

        line_1 = f"{operation[0]:>{width}}"
        line_2 = operation[1] + f"{operation[2]:>{width - 1}}"
        dash = '-' * width

        try:
            arranged_problems[0] += (' ' * 4) + line_1
        except IndexError:
            arranged_problems.append(line_1)

        try:
            arranged_problems[1] += (' ' * 4) + line_2
        except IndexError:
            arranged_problems.append(line_2)

        try:
            arranged_problems[2] = (' ' * 4) + dash
        except IndexError:
            arranged_problems.append(dash)

        if args:
            if operation[1] == '+':
                ans = str(int(operation[0]) + int(operation[2]))
            else:
                ans = str(int(operation[0]) - int(operation[2]))

            answer = f"{str(ans):>{width}}"

            try:
                arranged_problems[3] += (' ' * 4) + answer
            except IndexError:
                arranged_problems.append(answer)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    output = output + f"{arranged_problems[3]}" if args else output

    return output