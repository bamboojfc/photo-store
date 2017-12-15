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
from shutil import copyfile

class Log:

    def __init__(self):
        with open('./config.json', 'r') as f:
            self.__config = json.load(f) 
        self.__input_dir = self.__config['path']['input_dir']
        self.__log_file = os.path.join(self.__input_dir, self.__config['path']['log_file'])

    def write(self, text):
        with open(self.__log_file, "a") as text_file:
            print text
            text_file.write(text + '\r\n')

    def end(self):
        text = '============== DONE ==============='
        with open(self.__log_file, "a") as text_file:
            print text
            text_file.write(text + '\r\n')

class PhotoStore:

    def __init__(self):
        # try:
        with open('./config.json', 'r') as f:
            self.__config = json.load(f) 
        self.__input_dir = self.__config['path']['input_dir']
        self.__output_dir = self.__config['path']['output_dir']
        self.__filter_in = self.__config['dir']['filter_in']
        self.__filter_out = self.__config['file_type']['filter_out']
        if len(self.__filter_in) > 0:
            self.__filter_in_regexp = '|'.join(self.__filter_in)
        if len(self.__filter_out) > 0:
            self.__filter_out_regexp = '|'.join(self.__filter_out)
        self.__log = Log()
        # except Exception:
        #     self.__log.write('ERROR : no config file.')
        #     exit()
        
    def list_dir(self):
        input_dir_list = os.listdir(self.__input_dir)  
        self.__log.write('Get all directories from ' + str(self.__input_dir))
        #self.__log.write('All: ' + str(', '.join(input_dir_list)))
        
        res = []
        if len(self.__filter_in) > 0:
            # it gets only directories matching filter_in regex list
            for x in input_dir_list:
                try:
                    f = os.path.join(self.__input_dir, x)
                    if os.path.isdir(f) and re.search(self.__filter_in_regexp, x.lower()):
                        res.append(f)
                except:
                    pass
        else:
            # if filter_in is empty, it gets all directory
            for x in input_dir_list:
                try:
                    f = os.path.join(self.__input_dir, x)
                    if os.path.isdir(f):
                        res.append(f)
                except:
                    pass
        self.__log.write('Filtered: '+ ', '.join(res))
        return res

    def walk_in_directory(self, current_input_path = None, d = None, current_output_path = None):
        if current_input_path is None and current_output_path is None:
            current_input_path = self.__input_dir
            current_output_path = self.__output_dir

        current_input_path = os.path.join(current_input_path, d)
        current_output_path = os.path.join(current_output_path, os.path.basename(d))
        
        if os.path.isdir(current_input_path):
            self.mkdir(current_output_path)            
            file_list = os.listdir(current_input_path)
                      
            for f in file_list:
                self.walk_in_directory(current_input_path, f, current_output_path)
        else:
            if len(self.__filter_out) == 0 or not re.search(self.__filter_out_regexp, d.lower()):
                self.copy_file(current_input_path, current_output_path)

    def mkdir(self, outdir):
        self.__log.write('Create directory: ' + str(outdir))
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        else:
            self.__log.write('\tFAILED: ' + str(outdir) + ' has been already created.')

    def copy_file(self, infile, outfile):
        self.__log.write('\tCopy file from ' + str(infile) + ' to ' + str(outfile))
        copyfile(infile, outfile)

    def start(self):
        self.__directories = self.list_dir()
        self.__log.write('list of all directories:' + str(self.__directories) + '\n')
        for d in self.__directories:
            self.__log.write('#### Start walking into directory: ' + str(d) + '####')
            self.mkdir(self.__output_dir)          
            self.walk_in_directory(d = d)
            self.__log.write('\n')
        self.__log.end()

photoStore = PhotoStore()
photoStore.start()