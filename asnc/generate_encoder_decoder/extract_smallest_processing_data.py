

def extract_smallest_processing_data(data):
    smallest_processing_data =""
    next_char = ';'
    for c in data:
        if c == next_char:
            if next_char == ';':
                return  smallest_processing_data + c
            elif c == '}':
                smallest_processing_data += c
                next_char = ';'
        elif c == '{':
            smallest_processing_data += c
            next_char = '}'
        else:
            smallest_processing_data +=c







