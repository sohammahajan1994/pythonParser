import json


def read_json_file(filename):
    with open(filename) as f:
        data = json.load(f)

    return data

def add_headers_to_file(f_output_file, header_file, custom_header_file):
    header_json_object = read_json_file(header_file)
    preprocessor_directive = "#include"
    for header in header_json_object["system_header_files"]:
        f_output_file.write(preprocessor_directive + " <" + header + ">" + "\n")
    f_output_file.write("\n")
    for header in header_json_object["custom_header_files"]:
        f_output_file.write(preprocessor_directive + " \"" + header + "\"" + "\n")
    f_output_file.write(preprocessor_directive + " \"" + custom_header_file + "\"" + "\n\n")

