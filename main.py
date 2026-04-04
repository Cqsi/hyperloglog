# Your first step is implementing add — the function that takes an object, hashes it, and updates the right register.
# To do that you need to figure out two things from the hash integer: how to extract the low P bits to get the register index, and how to find the position of the first 1 bit in the remaining upper bits. Both are just integer bit operations. Get those two things working and printing correctly before touching anything else.

import mmh3

h = mmh3.hash64("Casimirasdasdasdadasd", signed=False)[0]
print("The hash is: ", h)
print("The binary of the hash is: ", bin(h))

def num_of_zeros(v: int):
    # simple example of bit manipulation in python
    # nb = v.bit_length()
    # binary = []
    # for bit in range(nb-1, -1, -1):
    #     binary.append((v >> bit) & 1);
    # return binary
    nb = v.bit_length()
    num = 0
    while(num < nb and (v >> num) & 1 == 0):
        num += 1
    
    return num

print(num_of_zeros(h))

def add(v):
    # extract the low P bits to get the register index
    # how to find the position of the first 1 bit
    pass