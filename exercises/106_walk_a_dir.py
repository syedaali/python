__author__ = 'syedaali'


import os


for directory, dirs, files in os.walk(r'/Users/syedaali/PycharmProjects/'):
    print 'Directory: ', directory
    print 'Children directories: ', dirs
    print 'Children files: ', files
