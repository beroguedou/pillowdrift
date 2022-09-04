import os
import sys
import requests
from pathlib import Path
from logging import config, getLogger
from pillowdrift.utils.logging_config import logging_config

config.dictConfig(logging_config)
logger = getLogger('root')

absolute_path_app = os.path.join(Path(__file__).parent.parent, 'app.py')


def startapp(configpath, datapath_ref, datapath_cur, datapath_service, host, port):
    # Execute the app.py file with argparse arguments
    os.system('python {} --configpath {} --reference-datapath {} --current-datapath {} --service-datapath {} --host {} --port {} '.format(absolute_path_app, configpath, datapath_ref,
                                                                                                                                          datapath_cur, datapath_service, host, port))


def stopapp(url):
    r = requests.get(url)
    if r.status_code:
        print('The server is off !')


def pillowdrift(options=sys.argv[1:]):

    if 'start' in options:
        options_dict = {}
        for element_value in options:
            if element_value != 'start':
                element, value = element_value.split('=')
                element, value = element.strip(), value.strip()
                options_dict[element] = value
        options_count = 0
        if '--configpath' not in options_dict.keys():
            logger.critical('Enter the config path !')
            sys.exit(1)
        else:
            options_count += 1
        if '--datapath-ref' not in options_dict.keys():
            logger.critical('Enter the reference data path !')
            sys.exit(1)
        else:
            options_count += 1

        if '--datapath-cur' not in options_dict.keys():
            logger.critical('Enter the current data path !')
            sys.exit(1)
        else:
            options_count += 1

        if '--datapath-service' not in options_dict.keys():
            logger.critical('Enter the service data path !')
            sys.exit(1)
        else:
            options_count += 1
        if '--host' not in options_dict.keys():
            host = '127.0.0.1'
        else:
            host = options_dict['--host']
        if '--port' not in options_dict.keys():
            port = '5000'
        else:
            port = options_dict['--port']

        if options_count == 4:
            configpath = options_dict['--configpath']
            datapath_ref = options_dict['--datapath-ref']
            datapath_cur = options_dict['--datapath-cur']
            datapath_service = options_dict['--datapath-service']
            host = options_dict['--host']
            port = options_dict['--port']

            # Start flask server
            logger.info('Launching the application ...')
            startapp(configpath,
                     datapath_ref,
                     datapath_cur,
                     datapath_service,
                     host, port)

    elif 'stop' in options:
        options_dict = {}
        for element_value in options:
            if element_value != 'stop':
                element, value = element_value.split('=')
                element, value = element.strip(), value.strip()
                options_dict[element] = value

        if '--host' not in options_dict.keys():
            host = '127.0.0.1'
        else:
            host = options_dict['--host']
        if '--port' not in options_dict.keys():
            host = '5000'
        else:
            port = int(options_dict['--port'])

        # Stop flask server
        logger.info('Shutting down the application ...')
        url = 'http://{}:{}/shutdown'.format(host, port)
        stopapp(url)
    else:
        logger.info('Provide one action: start or stop !')
        sys.exit(1)
