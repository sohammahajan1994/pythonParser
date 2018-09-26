from is_delimeter import is_delimeter


def read_and_process_asn_file(input_file):
    delimeter_array = [",", "{", "}"]
    str_to_be_processed = ""
    with open(input_file) as f:
        while True:
            c = f.read(1)
            if not c:
                print("process ending")
                break
            elif is_delimeter(delimeter_array, c):
                print("process sub part with sub string")
                print("write output to the file")
                str_to_be_processed = ""
            else:
                str_to_be_processed += c
