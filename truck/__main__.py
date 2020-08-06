#! /usr/bin/env python3

import os
import re
import csv
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


def load_cargo() -> dict:
    logging.debug('Load cargo table')

    cargo = []
    with open(os.path.join(cfg.data_dir, cfg.cargo_csv)) as file:
        data = csv.DictReader(file)
        for row in data:
            cargo.append(row)

    logging.debug('Cargo table loaded')
    return cargo

def match_cargo(cargo, truck) -> str:
    '''
    Print cargo and optimal available truck. 
    If a truck is loaded with a previous (in list) cargo, 
    print the next possible truck: "each truck can only make up to one trip"
    '''
    logging.info('Matching a truck for each cargo')

    res = ""
    truck_in_use = []
    for row in cargo:
        res += f'{row["product"]:<15} from {row["origin_state"]}'

        t = truck.locate(float(row['origin_lat']), float(row['origin_lng']))
        for option in t["options"]:
            if not option['truck'] in truck_in_use:
                truck_in_use.append(option['truck'])
                break

        res += f'transported by {option["truck"][:34]:<35} from {option["state"]}\n'

    return res


if __name__ == '__main__':
    logging.debug('Running from truck.main')

    cargo = {}
    truck = Truck()
    matches = None

    print('# Inform values to get a truck.')
    print('# Submit "limit" to know range of trucks.')
    print('# Submit "all" to list all cargo and most optimal (and available) truck.')
    print('# Submit "quit" to exit.')
    logging.debug('Menu displayed')

    while True:
        t = input('\nInform cargos latitude and longitude as "36.876 -89.587": ')

        if 'quit' in t.lower():
            logging.info('Exit application requested')
            print('# Tchau! :-)')
            break

        elif 'all' in t.lower():
            logging.debug('All cargo matches requested')
            if not cargo:
                cargo = load_cargo()
                matches = match_cargo(cargo, truck)

            count = len(matches.splitlines())
            logging.info(f'Printing trucks for each one of {count} cargos')
            print(matches)

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


