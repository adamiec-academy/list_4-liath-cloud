def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(poziom, pion):

    answer = []

    for i in range(poziom):

        part_answer = []

        if i == 0 or i == poziom - 1:
            for k in range(pion):
                part_answer.append("X")

        else:
            part_answer.append("X")
            for k in range(pion - 2):
                part_answer.append(".")

            part_answer.append("X")

        answer.append(part_answer)
    return answer
