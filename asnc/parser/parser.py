from read_json_file import read_json_file
from read_and_process_asn_file import read_and_process_asn_file
from pprint import pprint

mapping_json_obj = read_json_file("asnc_to_c_equivalent.json")
pprint(mapping_json_obj)

read_and_process_asn_file("rectangle.asn1", "rectangle.h", mapping_json_obj)

