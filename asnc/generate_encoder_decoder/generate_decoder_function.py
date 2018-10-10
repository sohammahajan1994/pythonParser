def generate_decoder_function(f_output_file, struct_data_dictionary):
    return_type = "void"
    function_name = "decoder"
    output_params_type = struct_data_dictionary["struct_type"]
    output_params_name = struct_data_dictionary["struct_type"].strip(" ") + "_struct"
    output_params_name = output_params_name.lower()
    output_param_type = "char **"
    output_param_name = "output_binary_view"
    bits_req_to_encode = "bits_req_to_encode"
