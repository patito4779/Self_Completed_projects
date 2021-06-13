
# Now let us take a look at classes in arrays

from itertools import groupby
list = ["Patrick", "Lucky", "Ayo", "Procastination"]
err_list = ["y", "l"]

print("The original list is: " + str(list))
print("The error list is: " + str(err_list))
new_list = []
err = 0
for ele in list:
    for elx in err_list:
        if elx not in ele:
            err = 0
        else:
            err = 1
            break # this break here means that if those elements y and l are in the ele(i.e err = True) then end the loop and return what is left
    if (err == 0):
        new_list.append(ele) # here means append the remaining words in the list that does not contain y and l
print(new_list)
            




