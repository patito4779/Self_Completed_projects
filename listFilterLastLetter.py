
# now let us run a program such that a set of letters ina list can be filtered out 
# The purpose of this program is to upadate a new list with data of names that does not end with y
from itertools import groupby
name_list = ["Patrick", "Lucky", "Henry", "Akpo", "Ayo", "Tommy", "Tobias"]
err_list = ["y"] # this is the ending letter we want to eliminate from our name_list

print("The original list is: " + str(name_list))
print("The error list is: " + str(err_list))

updated_list = [] # This will be our new updated list
err = 0            

for ele in name_list:           # Here we have a nested for loop which loops through the contents of the name_list and also through the err_list
    for elx in err_list:
        if elx != ele[-1]:      # This line serves to exclude all contents of the name_list which does not end with "y"
            err = 0
        else:
            err = 1
            break
    if (err == 0):
        updated_list.append(ele)

print("This is our updated name list of the students in ICAMS: " + str(updated_list))


