# Your first step is implementing add — the function that takes an object, hashes it, and updates the right register.
# To do that you need to figure out two things from the hash integer: how to extract the low P bits to get the register index, and how to find the position of the first 1 bit in the remaining upper bits. Both are just integer bit operations. Get those two things working and printing correctly before touching anything else.

# P = number of registers
# larger P = larger memory, more accuracy

import mmh3
from array import array

b = 14
h = mmh3.hash64("Casimirasdasdasdadasd", signed=False)[0]
print("The hash is: ", h)
print("The binary of the hash is: ", bin(h))

M = array('B', [0] * 2**b) # 2^b unsigned byte registers

def add(v: int):
    # simple example of bit manipulation in python
    # nb = v.bit_length()
    # binary = []
    # for bit in range(nb-1, -1, -1):
    #     binary.append((v >> bit) & 1);
    # return binary
    h = mmh3.hash64(v, signed=False)[0]
    
    beg = (1 << b) - 1 # j in the paper
    end = h >> b
   
    num = 0
    ne = end.bit_length()
    while(num < ne and (end >> num) & 1 == 0):
        num += 1
    
    M[beg] = max(M[beg], num)
    

print(add("Casimir"))

def add(v):
    # extract the low P bits to get the register index
    # how to find the position of the first 1 bit
    pass