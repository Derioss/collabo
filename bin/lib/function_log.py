#!/user/bin/env python3
import logging
import logging.handlers
import datetime
def my_log(my_log, loglevel, project_root):
    datetime_now=datetime.datetime.now()
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
