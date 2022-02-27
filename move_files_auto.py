

# The aim of this script is to automate the movement of files of a .log extension to another folder

# 1. Let us first write a script that just moves files of a certain extension from one folder if it exists to another folder

import os
import shutil
import subprocess

base_path = os.getenv("HOME")
files_path = base_path + "\OneDrive\Desktop\PythonProjects\Self_Completed_projects/"


def move_files_log(path):
    
    for files in os.listdir(path):
        if ".log" in files:
            shutil.move(path+files, path+"test_receiving_syncfolder")
        continue

move_files_log(files_path)


#print("".join([str(i) for i in range(4)]))
