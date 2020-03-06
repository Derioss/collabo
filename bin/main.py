#!/user/bin/env python3
import sys
import argparse
import os
import socket
from pathlib import Path
from lib.function_file import check_if_one_file_in_dir,read_data_and_for_each_event_write_file
from lib.function_load import load_config
from lib.function_log import my_log

###VAR##############
project_root = Path(__file__).absolute().parent.parent
list_data_dir = os.listdir(f'{project_root}\data')
###CONF####
load_config(project_root)
####################MAIN#############################
def main(loglevel,my_log,dryrun,project_root):
    #logging 
    my_log = my_log('script.py',loglevel,project_root)
    my_log.info('START PROGRAM')
    if dryrun is True:
        my_log.info('DRYRUN ACTIVE')

    value = check_if_one_file_in_dir(list_data_dir)
    if value is not 'ok':
        my_log.warning(value)

    read_data_and_for_each_event_write_file(f'{project_root}/data/'+ list_data_dir[1],f'{project_root}/temp')

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
