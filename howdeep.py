####
# Author:           Patrick Caamano
# Last update:      08.10.2013
# Description:      This Script shows you which directory has the deepest structure of folders and how deep it goes.
#                   Be sure you have the permissions to access the folders in the directory you choose.
#                   MANUAL: write in command line "python howdeep.py /your/directory"
####

import sys
import os

def howdeep(path):
    
    amount = 0

    if os.path.isdir(path):
        dirlist = get_list(path)
      
        for dir in dirlist:
            handlelist = get_list(dir)
            dirlist.extend(handlelist)

        for path in dirlist:
            path = path.replace(os.path.commonprefix(dirlist), '')
            tmp_amount = path.count('/')
                
            if tmp_amount > amount:
                amount = tmp_amount

            print path

        print "\n\nThe longest directory is %s folders deep." % amount
    
    else:
        print "This folder doesn't exist."

def get_list(path):

    pathlist = []

    tmplist = os.listdir(path)
    for dir in tmplist:
            
        dir = path + dir + '/'

        if os.path.isdir(dir):
            pathlist.append(dir)
    
    return pathlist
    
if __name__ == '__main__':
    
    path = sys.argv[1]
    
    if not path:
        print "You have to write a directory path."
    
    elif not path[-1] == '/':
        path = path + '/'
        howdeep(path)
    
    else:
        howdeep(path)
