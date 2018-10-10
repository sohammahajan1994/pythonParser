from process_struct import process_struct


def process_data(data):
    data  = data.strip(' ')
    if data.startswith('typedef struct'):
        return process_struct(data)
