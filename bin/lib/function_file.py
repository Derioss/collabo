#!/user/bin/env python3
import re
def check_if_one_file_in_dir(dir):
    if len(dir) == 2:
        message='ok'
    elif len(dir) < 2:
        message="This dir is empty, you need to put csv file as described on readme."
    else:
        message="you need to put online ONE csv file as described on readme."
    return message

def read_data_and_for_each_event_write_file(source_file,dest_dir):
    with open(f'{source_file}', 'r',encoding="utf8") as data_file:
        i = 0
        lines = data_file.readlines()
        temp_var= ''
        for line in lines:
            i+=1
            temp_var = temp_var + line
            if re.search('-- end --',line):
                with open(f'{dest_dir}/{i}.csv', 'w',encoding="utf8")as file:
                    file.write(temp_var)
                temp_var=""
