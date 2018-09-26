

def is_delimeter(delimeter_array, char):
    for idx, val in enumerate(delimeter_array):
        if val == char:
            return 1
    return 0
