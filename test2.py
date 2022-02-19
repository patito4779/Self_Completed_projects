
def countdown(start):
        
        while start > 0:
                print(start)
                start -= 1
        print("Zero")

countdown(15)





print(1 // 10)




def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = (filesize//block_size)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (block_size + block_size * full_blocks)
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


# This below is a factorial script
def factorial(n):
    result = 1
    for x in range(n):
        result = result * (x + 1)
    return result

for n in range(10):
    print(n, factorial(n))


def multiple(n):
    for num in range(n):
        if num % 7 == 0:
            print(num)
        else:
            exit
    
multiple(100)









