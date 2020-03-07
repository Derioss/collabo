#!/user/bin/env python3
import sys, os
import argparse
import socket
from pathlib import Path
import lib.function_file as file
from lib.function_load import load_config
from lib.function_log import my_log
import lib.function_data as data
import pandas as pd
import numpy as np
import openpyxl
###VAR##############
project_root = Path(__file__).absolute().parent.parent
list_data_dir = os.listdir(f'{project_root}\data')
###CONF####
conf = load_config(project_root)
####################MAIN#############################
def main(loglevel,my_log,dryrun,project_root):
    #logging 
    my_log = my_log('script.py',loglevel,project_root)
    my_log.info('START PROGRAM')
    if dryrun is True:
        my_log.info('DRYRUN ACTIVE')

    value = file.check_if_one_file_in_dir(list_data_dir)
    if value is not 'ok':
        my_log.warning(value)

    file.read_data_and_for_each_event_write_file(f'{project_root}/data/'+ list_data_dir[1],f'{project_root}/temp')
    file.format_temp_file(project_root)
    '''
    player_class = data.dict_player_by_event(project_root)
    final_dict = player_class.build_player_dict_list_by_date_event()
    print(final_dict['06-01-2020'])
    '''
 


    '''
    present = data.retrieve_present_by_event(project_root)
    player_list_temp = []


    for list in present:
        player_list_temp = player_list_temp + list

    player_list = set(player_list_temp)
    index_raid = data.retrieve_date_event(project_root)
    df = pd.DataFrame(columns=index_raid, index=player_list)
    print(df)
    df.to_excel('myDataFrame.xlsx', encoding='utf-8')
    '''
    my_log.info('STOP PROGRAM')
##########################################################

if __name__ == "__main__":
    ## args options for log level
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--loglevel", action="store",dest="verbosity",default='info',
    help="options: debug info warning error critical, default=info")
    parser.add_argument("-d","--dryrun", action="store_true",help="active this option to performed dryrun")
    args = parser.parse_args()
    loglevel=args.verbosity
    if args.dryrun:
        dryrun=args.dryrun
    else:
        dryrun=False
    #main
    main(loglevel,my_log,dryrun,project_root)
