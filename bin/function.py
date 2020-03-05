#!/user/bin/env python3

def check_if_one_file_in_dir(dir):
    if len(dir) == 1:
        value='ok'
    else:
        value='ko'
    return value