def min_max(data):
    min = data[0]
    max = data[0]

    for i in data:

        if i > max:
            max = i

        if i < min:
            min = i

    return min, max
