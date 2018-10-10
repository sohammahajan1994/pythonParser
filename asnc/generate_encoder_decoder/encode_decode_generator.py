from add_headers_to_file import add_headers_to_file
from extract_smallest_processing_data import extract_smallest_processing_data
from process_data import process_data
from generate_encoder_function import generate_encoder_function

print("encode decode generator")
header_file = "headers.json"
output_directory = "asnc/output/src/"
output_file = "rectangle.c"
input_header_directory = "asnc/output/src/include/"
input_header_file = "rectangle.h"

# open output file in write mode
f_output_file = open(output_directory + output_file, "w+")
# # generate c code for encode_integer ===>  added there in output folder
# # include header for encode and decode
add_headers_to_file(f_output_file, header_file, input_header_file)

with open(input_header_directory + input_header_file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
print("header file " + data)

# currently working for only one struct in file
data_to_be_processed = extract_smallest_processing_data(data)
print(data_to_be_processed)
struct_data_dictionary = process_data(data_to_be_processed)
print(struct_data_dictionary.keys())
print("========================================================================")
generate_encoder_function(f_output_file, struct_data_dictionary)

# # read .h




    # en # get struct name as param with buff as output argument to encoder_function( S s, char* buff)

    # en # parse struct members and call encode integer/ char /struct accordingly

    # en # append returned string to buf i.e. outout argument

    # de # get binary char * and struct as a output argument to decoder function

    # de # parse struct members and call decode integer / char/ struct respectively

    # de # add decoded value to the struct


f_output_file.close()
