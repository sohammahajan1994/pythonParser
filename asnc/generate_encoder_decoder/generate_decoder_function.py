import re

def function_writer(f_output_file , line):
    f_output_file.write("\t" + line +"\n")

def process_decode_int(f_output_file, input_param_name,  struct_name, data_memeber_name, start_bit):
    d_int_function_name = "decode_integer"
    function_writer(f_output_file, start_bit + " = " + d_int_function_name + "(" + input_param_name + ", &" + struct_name + "->" + data_memeber_name + ", " + start_bit + ");")

def generate_decoder_function(f_output_file, struct_data_dictionary):
    return_type = "void"
    function_name = "decoder"
    output_params_type = struct_data_dictionary["struct_type"].strip(" ")
    output_params_name = struct_data_dictionary["struct_type"].strip(" ") + "_struct"
    output_params_name = output_params_name.lower()
    input_param_type = "char *"
    input_param_name = "input_binary_view"
    start_bit = "start_bit"
    function_defination = return_type + " " + function_name + "(" + input_param_type + input_param_name + ", " + output_params_type + " *" + output_params_name + "){\n"
    f_output_file.write(function_defination)
    function_writer(f_output_file, "int " + start_bit + "=0;")


    for key, val in struct_data_dictionary.items():
        if key.startswith('varname_'):
            actual_key = re.search("varname_(.*)", key).group(1)
            if val == "int":
                process_decode_int(f_output_file, input_param_name, output_params_name, actual_key, start_bit)



    f_output_file.write("}\n")
