from generate_encoder_decoder_defination import generate_encoder_decoder_defination


def process_asn_string(input_string, delimeter, asnc_mapping_object, struct_name):
    input_string = input_string.strip()
    word_array = input_string.split(" ")
    #print(len(word_array))
    #print(word_array)
    word_array_len = len(word_array)
    if word_array_len<2:
        return None

    #print(asnc_mapping_object[word_array[1]])
    current_keyword_mapping_object = asnc_mapping_object[word_array[1]]
    if word_array_len < current_keyword_mapping_object["min_len"]:
        return None

    #print(current_keyword_mapping_object["equivalent"])
    i=1
    output_list = []
    while i< current_keyword_mapping_object["min_len"]:
        output_list.append( asnc_mapping_object[word_array[i]]["equivalent"])
        i += 1
    output_list.append(word_array[0])
    print(output_list)
    if delimeter == '{':
        output_list.append(delimeter)
        struct_name.append(word_array[0])
    elif delimeter == ',':
        output_list.append(";")
    elif delimeter == '}':
        output_list.append(";")
        output_list.append("\n")
        output_list.append(delimeter)
        struct_type = struct_name.pop()
        output_list.append(struct_type + "_t")
        output_list.append(";\n\n")
        output_list.append(generate_encoder_decoder_defination(struct_type))

    output_string = " ".join(output_list)
    print(output_string)
    return output_string

