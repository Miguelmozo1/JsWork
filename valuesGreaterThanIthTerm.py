# function that makes new list of values greater than chosen index from given list

def greater_than(list, value):
    new_list = []
    greater_than = value
    for i in range(len(list)):
        if list[i] > greater_than:
            new_list.append(list[i])
    return f'New list {new_list}'

x = greater_than([22,1,34,52,89,10], 33)
print(x)