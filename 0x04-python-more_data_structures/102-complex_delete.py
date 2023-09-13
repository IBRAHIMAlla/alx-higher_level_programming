#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_list = sorted(a_dictionary.keys())

    for val_dic in k_list:
        if value == a_dictionary.get(val_dic):
            del a_dictionary[val_dic]

    return (a_dictionary)
