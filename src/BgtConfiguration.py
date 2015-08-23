'''
Created on Aug 20, 2015
A class that reads configuration from a configuration file and command line parameters,
and gives out this information.

@author: bgt
'''

import ConfigParser

class BgtConfiguration(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.fileConfig = None

        self.inputfiles = []
    
    def get(self, section, option):
        return self.fileConfig.get(section, option)
    
    def parseCommandLine(self, argv):
        if len(argv) < 2:
            raise BadCommandLineException("Too few commandline parameters.")
        self.inputfiles = argv
        argv.pop(0)

    def readConfigfile(self, configFilePathName):
        self.fileConfig = ConfigParser.ConfigParser()
        self.fileConfig.readfp(open(configFilePathName))

class BadCommandLineException(Exception):
    pass

        