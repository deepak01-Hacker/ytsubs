import os

def getRecordObject():
    dir_path = os.path.dirname(os.path.realpath(__file__))+'/readme.txt'
    object = open(dir_path, 'w')
    
    return object