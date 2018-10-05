from add_headers_to_file import add_headers_to_file

print("encode decode generator")
path = "asnc/output/src/"
output_directory = "asnc/output/src/"
output_file = "rectangle.c"

f_output_file = open(path + output_file, "w+")
# # generate c code for encode_integer ===>  added there in output folder
add_headers_to_file(f_output_file)
# # include header for encode and decode

    # f_output_file = open(, "w+")

    # # read .h


    # en # get struct name as param with buff as output argument to encoder_function( S s, char* buff)

    # en # parse struct members and call encode integer/ char /struct accordingly

    # en # append returned string to buf i.e. outout argument

    # de # get binary char * and struct as a output argument to decoder function

    # de # parse struct members and call decode integer / char/ struct respectively

    # de # add decoded value to the struct


f_output_file.close()
