#!/user/bin/env python3
import os,re

def listToString(s):
    str1 = " " 
    return (str1.join(s))

def retrieve_date_event(project_root):
    list_temp_dir = os.listdir(f'{project_root}/temp')
    date = []
    for file in list_temp_dir[1:]:
        with open(f'{project_root}\\temp\\{file}', 'r',encoding="utf8") as data_file:
            lines = data_file.readlines()
            date_temp = lines[1].split(',')[1]
            date.append(date_temp)
    return date

def retrieve_player_by_event(project_root,num0,num1):
    list_temp_dir = os.listdir(f'{project_root}/temp')
    all_raid = []
    player = []
    for file in list_temp_dir[1:]:
        player_temp0 = []
        with open(f'{project_root}\\temp\\{file}', 'r',encoding="utf8") as data_file:
            lines = data_file.readlines()
            if num1 is 0:
                player_temp = listToString(lines[num0]).split('--')
            else:
                player_temp = listToString(lines[num0:num1]).split('--')
            for entry in player_temp:
                new_line = entry.rstrip()
                if re.search(r"\*\*", new_line):
                    player_temp0.append(new_line.split('**')[1])
            player.append(player_temp0)
    return player

def retrieve_present_by_event(project_root):
    return retrieve_player_by_event(project_root,3,10)
