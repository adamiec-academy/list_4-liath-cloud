def my_split(text):

    answer=[]
    flag = 0
    string = ""

    for i in range(len(text)):

        if text[i] != " ":
            string += text[i]
            flag = 1

        elif text[i] == " " and string != "":
            answer.append(string)
            string = ""
            flag = 0

    if flag == 1:
        answer.append(string)

    return answer
