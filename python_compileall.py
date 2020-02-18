# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:03:22 2020

@author: meiyarasu.selvam
"""
import compileall,shutil,os

dir_path = os.path.dirname(os.path.realpath(__file__))
destination = dir_path+'\\destination'

print(dir_path)

if os.path.exists(destination):
    shutil.rmtree(destination)
compileall.compile_dir(dir_path)
shutil.copytree(dir_path, destination, ignore = shutil.ignore_patterns('*~', '*.py'))

for root, subdirs, files in os.walk(destination):
    if root.endswith('__pycache__'):
        for file in files:
            oldname=os.path.join(root,file)
            newname=os.path.join(root.replace('\__pycache__',''),file.split('.')[0] +'.pyc')
            shutil.move(oldname,newname)
        shutil.rmtree(root)
print("Completed")


    
    
