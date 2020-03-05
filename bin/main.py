#!/user/bin/env python3
import logging
import logging.handlers
import sys
import argparse
import os
import socket
from pathlib import Path
import datetime
import yaml
from function import *

###VAR##########
project_root = Path(__file__).absolute().parent.parent
datetime_now=datetime.datetime.now()
list_data_dir = os.listdir(f'{project_root}\data')

###CONF####
with open(f'{project_root}/conf/main.yaml') as ymlfile:
    conf = yaml.load(ymlfile, Loader=yaml.FullLoader)

############LOGGING#################################
def my_log(my_log, loglevel):

    LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

    my_log = logging.getLogger(my_log)
    my_log.setLevel(LEVELS[loglevel])
    logFormatter = logging.Formatter(f'{datetime_now} - %(levelname)s - %(message)s')
    sysloghandler = logging.FileHandler(f'{project_root}\log\collabo.log')
    sysloghandler.setFormatter(logFormatter)
    my_log.addHandler(sysloghandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    my_log.addHandler(consoleHandler)
    return my_log

####################MAIN#############################
def main(loglevel,my_log,dryrun):
    #logging 
    my_log = my_log('script.py',loglevel)
    my_log.info('START PROGRAM')
    if dryrun is True:
        my_log.info('DRYRUN ACTIVE')

    print(conf['path']['log_path'])
#    with open(f'{project_root}/data/'):
#        for line in 
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
    main(loglevel,my_log,dryrun)
