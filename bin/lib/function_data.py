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

def retrieve_date_event(temp_dir,file):
    with open(f'{temp_dir}/{file}', 'r',encoding="utf8") as data_file:
        lines = data_file.readlines()
        date = lines[1].split(',')[1]
    return date

def build_player_list(temp_dir,file,num0,num1):
    player = []
    with open(f'{temp_dir}/{file}', 'r',encoding="utf8") as data_file:
        lines = data_file.readlines()
        if num1 is False:
            player_temp = listToString(lines[num0]).split('--')
        else:
            player_temp = listToString(lines[num0:num1]).split('--')
        for entry in player_temp:
            new_line = entry.rstrip()
            if re.search(r"\*\*", entry):
                player.append(new_line.split('**')[1])
        return player

def build_player_list_format2(temp_dir,file,num0,num1):
    player = []
    with open(f'{temp_dir}/{file}', 'r',encoding="utf8") as data_file:
        lines = data_file.readlines()
        if num1 is False:
            player_temp = listToString(lines[num0]).split('--')
        else:
            player_temp = listToString(lines[num0:num1]).split('--')
        for entry in player_temp:
            new_line = entry.rstrip()
            if re.search(r"\-\-", new_line):
                player.append(new_line.split('--')[1])
        return player
class dict_player_by_event:
    def __init__(self,project_root):
        self.project_root = project_root
        self.temp_dir = f'{project_root}/temp'
        self.present0 = 3
        self.present1 = 10
        self.late = 11
        self.bench = 12
        self.abs = 13
        self.final_dict = {}

    def build_player_dict_list_by_date_event(self):

        list_temp_dir = os.listdir(self.temp_dir)
        for file in list_temp_dir[1:]:
            temp_dict = {}
            player_dict = {}
            date = retrieve_date_event(self.temp_dir,file)
            player_dict['present'] = build_player_list(self.temp_dir,file, self.present0,self.present1)
            player_dict['late'] = build_player_list_format2(self.temp_dir,file, self.late,False)
            player_dict['bench'] = build_player_list_format2(self.temp_dir,file, self.bench, False)
            player_dict['abs'] = build_player_list_format2(self.temp_dir,file, self.abs, False)
            temp_dict[date] = player_dict
            self.final_dict.update(temp_dict)

        return self.final_dict




