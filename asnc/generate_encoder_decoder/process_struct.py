import re

def process_data_member(data_member, data_dictionary):
    data_member = data_member.strip(' ')
    data_member_list = data_member.split(" ")
    if len(data_member_list) < 2:
        return
    data_dictionary["varname_" +data_member_list[1]] = data_member_list[0]
    data_member_list.clear()

def get_struct_member(data):
    return re.search("{(.*)}", data).group(1)

def get_struct_name(data):
    return re.search("}(.*);", data).group(1)

def process_struct(data):
    data_dictionary = {}
    struct_name = get_struct_name(data)
    data_dictionary["struct_type"] = struct_name
    struct_member_string = get_struct_member(data)
    struct_member_list = struct_member_string.split(";")
    for data_member in struct_member_list:
        process_data_member(data_member, data_dictionary)
    return data_dictionary
