

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        for i in range(start, stop-1, -1):                     # Range does not include the last value, then we use the end value stop-1
                return_string = return_string + str(i)
                if (i > stop):                                 # This line adds a comma between the numbers until i = stop
                    return_string = return_string + ","

    else:
        return_string = "Counting up: "
        for i in range(start, stop+1, 1):                       # Range does not include the end value hence we use the stop+1 
                return_string = return_string + str(i)
                if (i < stop):
                    return_string = return_string + ","

                

                

    return return_string
            

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5" 

