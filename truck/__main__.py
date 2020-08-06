#! /usr/bin/env python3

import os
import re
import json
import logging
from . import Truck
import config as cfg


# logging hack in case of windows
_datefmt = '%Y%m%dT%H%M%S' if os.name == 'nt' else '%s'

# Set log level and path in config
_logs_file = os.path.join(cfg.logs_dir, cfg.logs_file)
logging.basicConfig(level=cfg.logs_level, filename=_logs_file, datefmt=_datefmt,
                    format='%(asctime)s:%(levelname)s:%(message)s')


if __name__ == '__main__':
    logging.debug('Running from truck.main')

    truck = Truck()
    logging.info('Truck object instantiated')

    print('# Inform values to get a truck.')
    print('# Submit "limit" to know range of trucks.')
    print('# Submit "quit" to exit.')
    logging.debug('Menu displayed')

    while True:
        t = input('\nInform cargos latitude and longitude as "36.876719 -89.5878579": ')

        if 'quit' in t.lower():
            logging.info('Exit application requested')
            print('# Tchau! :-)')
            break
        elif 'limit' in t.lower():
            logging.debug('Coords limit requested')
            print(f'# Limits as ((North, South), (West, East)) are: {truck.range()}')
            continue
        else:
            t = re.sub('[^0-9-\. ]', '', t)
            try:
                lat, lng = t.split(' ')
                lat = float(lat)
                lng = float(lng)

                d = truck.locate(lat, lng)
                logging.info(f'Trucks near {lat} and {lng}: {len(d["options"])}')
                logging.debug(f'Closest truck: {d["options"][0]["truck"]}')

                print('\n# Available trucks:')
                print(json.dumps(d, indent=2))

                logging.debug('Trucks JSON printed')
            except e:
                logging.warning(f'Data input error: {e}')
                print('# Must inform two float coords separated by space, as [36.87 -89.58].')

