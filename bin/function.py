#!/user/bin/env python3

def check_if_one_file_in_dir(dir):
    if len(dir) == 2:
        message='ok'
    elif len(dir) < 2:
        message="This dir is empty, you need to put csv file as described on readme."
    else:
        message="you need to put online ONE csv file as described on readme."
    return message