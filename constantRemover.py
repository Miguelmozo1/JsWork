# function removes a constant from all values in a list without altering original list
def remover(list, const):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(list[i] - const)
    print(f"Original list: {list}")
    return f"Altered List: {new_list}"

x = remover([3,5,6,12,76], 12)
print(x)