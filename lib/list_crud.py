""" import ipdb """

def create_an_empty_list():
    empty_list = []
    return empty_list

def create_a_list():
    new_list = ["apple", "banana", "cucumber", "dragonfruit"]
    return new_list

def add_element_to_end_of_list(list, element):
    list.append(element)
    return list

def add_element_to_start_of_list(list, element):
    list.insert(0, element)
    return list

def remove_element_from_end_of_list(list):
    list.pop()
    return list

def remove_element_from_start_of_list(list):
    del(list[0])
    return list

def retrieve_first_element_from_list(list):
    return list[0]

def retrieve_element_from_index(list, index):
    return list[index]

def retrieve_last_element_from_list(list):
    return list[-1]

""" ipdb.set_trace() """
