set = [ [11, "string", 77], [12, 14, "boar"] ]

clients = [
    {'f_name': 'Jerry', 'l_name': 'Ole'},
    {'f_name': 'Bertha', 'l_name': 'Jenn'}
]

hobby_descr = {
    'skateboard': ['griptape', 'trucks', 'wheels'],
    'snowboard': ['bindings', 'boots', 'googles']
}



coordinates = [ {'x': 5, 'y': 10} ]

# coordinates[0]['x'] = 9
# print (coordinates)

# clients[1]['l_name'] = "Jennings"
# print(clients)

# hobby_descr['snowboard'][2] = "goggles"
# print(hobby_descr)

# set[1][1] = 24
# print(set)

# def go_through_dict(dict):
#     for value in dict:
#         print(f"{value}\n")
# go_through_dict(clients)
# go_through_dict(hobby_descr)


def list_hunter(key_name, list):
    for i in range(len(list)):
        for key, val in list[i].items():                # method used particularly in dictionairies. Formatted so "key" and "val" can be anything, it knows its reading a dict
            if key ==  key_name:
                print(val)
# list_hunter('f_name', clients)



def dict_hunter(dict):
    for i in dict.items():
        print(len(dict))
        print(i)
dict_hunter(hobby_descr)

