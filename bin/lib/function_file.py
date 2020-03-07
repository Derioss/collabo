#!/user/bin/env python3
import re, os
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

def format_temp_file(project_root):
    list_temp_dir = os.listdir(f'{project_root}/temp')
    for file in list_temp_dir[1:]:
        with open(f'{project_root}\\temp\\{file}', 'r',encoding="utf8") as f:
            flag = False
            text = []
            for line in f:
                new_line = line.rstrip()
                if re.search('Number of raids', new_line):
                    flag = False
                elif re.search('Time of creation', new_line):
                    flag = False
                elif re.search('-- start --',new_line):
                    flag = False
                elif re.search('-- end --',new_line):
                    flag = False
                elif re.match(r'^\s*$', line):
                    flag = False
                else:
                    flag = True
                if flag is True:
                    text.append(line)
        with open(f'{project_root}\\temp\\{file}', 'w', encoding="utf8") as f:
            f.writelines(text)