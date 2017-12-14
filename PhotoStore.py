#!/Python27/python
# -*- coding: utf-8 -*-

"""
Created on Thu Dec 14 12:27:04 2017

@author: Nannapas Banluesombatkul 
@email: nannapas.blsbk@gmail.com
"""

import os
import json
import re

class PhotoStore:
    
    def __init__(self):
        try:
            with open('./config.json', 'r') as f:
                self.__config = json.load(f)
        except Exception:
            print 'ERROR : no config file.'
            exit()
        
    def list_dir(self):
        input_dir = self.__config['path']['input_dir']
        input_dir_list = os.listdir(self.__config['path']['input_dir'])        
        filter_in = self.__config['dir']['filter_in']
        res = []
        if len(filter_in) > 0:
            # it gets only directories matching filter_in regex list
            filter_in = '||'.join(filter_in)
            for x in input_dir_list:
                try:
                    f = os.path.join(input_dir, x)
                    if os.path.isdir(f) and re.search(filter_in, x):
                        res.append(f)
                except:
                    pass
        else:
            # if filter_in is empty, it gets all directory
            for x in input_dir_list:
                try:
                    f = os.path.join(input_dir, x)
                    print f, os.path.isdir(f)
                    if os.path.isdir(f):
                        res.append(f)
                except:
                    pass
        
        return res

photoStore = PhotoStore()
print photoStore.list_dir()