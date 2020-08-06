#! /usr/bin/env python3
'''
Truck package

Note: truck csv file is checked with module load.
'''

import os
import math
import pandas as pd
import config as cfg


trucks_file = os.path.join(cfg.data_dir, cfg.trucks_csv)
if not os.path.isfile(trucks_file): raise FileNotFoundError

class Truck:
    def __init__(self) -> None:
        '''Load truck csv into a pandas dataframe'''
        self.data = pd.read_csv(trucks_file)

    def count(self) -> int:
        '''Count trucks loaded from csv'''
        return len(self.data.index)

    def range(self) -> tuple:
        '''Return (northern, southern) and (western, eastern limits), based on available trucks'''
        return ( (round(self.data['lat'].max()), round(self.data['lat'].min())), 
                 (round(self.data['lng'].min()), round(self.data['lng'].max())) )

    def locate(self, lat, lng, range_limit=5, results_limit=3) -> dict:
        '''
        Return trucks as near as possible to the informed coords.

        Arguments:
            lat (float): latitude, as in 34.79981
            lng (float): longitude, as in -87.677251
            range_limit (int): search limit (optional, defaults to 5 degrees or 500+ km)

        Return:
            dict: up to three closest trucks (ordered by proximity)
        '''

        lat_limits = [ int(lat*10) ] * 2
        lng_limits = [ int(lng*10) ] * 2

        for degree in range(1, range_limit*10, 3): # increases range in 0.3 degrees
            lat_limits = [ lat_limits[0]-degree, lat_limits[1]+degree ]
            lng_limits = [ lng_limits[0]-degree, lng_limits[1]+degree ]

            mask = self.data['lat'].between(lat_limits[0]/10, lat_limits[1]/10) \
                 & self.data['lng'].between(lng_limits[0]/10, lng_limits[1]/10)

            df = self.data.loc[mask]
            if len(df) >= results_limit: break

        trucks = {}
        for i, row in df.iterrows():
            h = math.hypot(abs((lat)-(row.lat)), abs((lng)-(row.lng)))
            trucks[h] = { 'id': i }

        res = { 'location': { 'lat': lat, 'lng': lng }, 'options': [] }

        for h in sorted(trucks):
            i = trucks[h]['id']
            res['options'].append(self.data.iloc[i].to_dict())

        return res

    def print(self, limit=None) -> None:
        '''
        Print list of trucks

        Arguments:
            limit (int): prints N records (optional, defaults to All records)
        '''
        print(self.data.head(limit))

