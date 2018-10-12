import re


def function_writer(f_output_file , line):
    f_output_file.write("\t" + line +"\n")

def process_encode_int(f_output_file, struct_name, data_member_name, main_output_var, bits_req_to_encode, size_of_char):
    e_int_function_name = "encode_integer"
    main_output_var = "*" + main_output_var
    function_writer(f_output_file, bits_req_to_encode + " += "+ e_int_function_name + "(" + struct_name + "->" + data_member_name + ", temp_int);")
    function_writer(f_output_file, main_output_var + " = realloc( "+ main_output_var +", " + bits_req_to_encode + "*" + size_of_char + ");" )
    function_writer(f_output_file, "strcat("+ main_output_var + ", temp_int);")

def generate_encoder_function(f_output_file, struct_data_dictionary):
    return_type = "void"
    function_name = "encoder"
    input_params_type = struct_data_dictionary["struct_type"].strip(" ")
    input_params_name = struct_data_dictionary["struct_type"].strip(" ") + "_struct"
    input_params_name = input_params_name.lower()
    output_param_type = "char **"
    output_param_name = "output_binary_view"
    bits_req_to_encode  = "bits_req_to_encode"
    size_of_char = " sizeof(char)"

    f_output_file.write(return_type + " " + function_name + "(" + input_params_type + " *" + input_params_name + ", " + output_param_type + output_param_name + "){ \n")
    function_writer(f_output_file, "int " +bits_req_to_encode + "= 8;" )
    function_writer(f_output_file, "char temp_int[72];")

    for key, val in struct_data_dictionary.items():
        if key.startswith('varname_'):
            actual_key = re.search("varname_(.*)", key).group(1)
            actual_value = val
            if actual_value == "int":
                process_encode_int(f_output_file, input_params_name, actual_key, output_param_name, bits_req_to_encode, size_of_char)


    f_output_file.write("}\n\n")