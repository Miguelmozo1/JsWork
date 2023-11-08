# function that gives added values, max, and min of any given list respectively

def stats(list):
    sum = 0
    max = list[0]
    min = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
        sum += list[i]
        if list[i] < min:
            min = list[i]
    return sum, max, min


x = stats([901,98,23,99,45,902])
print(x)