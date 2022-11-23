import math
def is_palindrome(text):

    text = text.lower()
    text = text.split(" ")
    text = "".join(text)

    for i in range(1, math.floor((len(text) + 1)/2)):

        if text[i-1] != text[-i]:
            return False
            break

    return True
