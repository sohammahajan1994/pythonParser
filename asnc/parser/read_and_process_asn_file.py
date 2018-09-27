from is_delimeter import is_delimeter
from process_asn_string import process_asn_string

def read_and_process_asn_file(input_file, output_file, asnc_mapping_object):
    delimeter_array = [",", "{", "}"]
    str_to_be_processed = ""
    struct_name = []
    f_output_file = open(output_file, "w+")
    with open(input_file) as f:
        while True:
            c = f.read(1)
            if not c:
                print("process ending")
                break
            elif is_delimeter(delimeter_array, c):
                print("process sub part with sub string")
                str_equivalent = process_asn_string(str_to_be_processed, c, asnc_mapping_object, struct_name)
                print("write output to the file")
                if str_equivalent:
                    f_output_file.write(str_equivalent + "\n")
                str_to_be_processed = ""
            else:
                str_to_be_processed += c

    f_output_file.close()
