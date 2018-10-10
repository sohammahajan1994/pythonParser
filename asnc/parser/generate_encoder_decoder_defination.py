def generate_encoder_decoder_defination(struct_type):
    output_string = ""

    e_return_type = "void"
    e_function_name = "encoder"
    e_input_param_type = struct_type.strip(" ") + "_t"
    e_input_param_name = struct_type.strip(" ") + "_struct"
    e_input_param_name = e_input_param_name.lower()
    e_output_param_type = "char **"
    e_output_param_name = "binary_view_of_struct"

    output_string += e_return_type + " " + e_function_name + "(" + e_input_param_type + "* " + e_input_param_name + ", " + e_output_param_type + e_output_param_name + ");\n\n"

    d_return_type = "void"
    d_function_name = "decoder"
    d_output_param_type = struct_type.strip(" ") + "_t"
    d_output_param_name = struct_type.strip(" ") + "_struct"
    d_output_param_name = d_output_param_name.lower()
    d_input_param_type = "char **"
    d_input_param_name = "binary_view_of_struct"

    output_string += d_return_type + " " + d_function_name + "(" + d_input_param_type + " " + d_input_param_name + ", " + d_output_param_type + "* "+ d_output_param_name + ");\n\n"

    return output_string

