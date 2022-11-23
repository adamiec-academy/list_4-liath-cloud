def my_split(text):

    answer=[]
    string = ""

    for i in range(len(text)):

        if text[i] != " ":
            string += text[i]

        elif text[i] == " " and string != "":
            answer.append(string)
            string = ""

    return answer
