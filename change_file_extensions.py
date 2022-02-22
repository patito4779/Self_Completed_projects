# This short script goes through set of files in a linux folder and changes the file extension accordingly.

import os
# Get the working home directory which you can also print to screen
cwd = os.getenv("HOME")
# print(cwd)

# Enter the path to the folder where the files you want to rename are located
path = cwd+"Desktop/test"
def change_extension(path):
    # Traverse through the files in the path
    for files in os.listdir(path):
        # checking if there is an extension ".inp"
        if ".inp" in files:
            old_name = path + "/" + files
            # IF found then we replace the extension with fortran 90 extension or whatever with want
            new_name = old_name.replace(".inp", ".f90")
            os.rename(old_name, new_name)
        # Then we continue if our intended extension is not found
        continue

change_extension(path)
