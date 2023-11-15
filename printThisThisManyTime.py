# function that will print a given value x amount of times

def print_this(value, x):
    list = []
    for i in range(x):
        list.append(value)
    return list

x = print_this(3, 9)
print(x)