# Your first step is implementing add — the function that takes an object, hashes it, and updates the right register.
# To do that you need to figure out two things from the hash integer: how to extract the low P bits to get the register index, and how to find the position of the first 1 bit in the remaining upper bits. Both are just integer bit operations. Get those two things working and printing correctly before touching anything else.

 # simple example of bit manipulation in python
    # nb = v.bit_length()
    # binary = []
    # for bit in range(nb-1, -1, -1):
    #     binary.append((v >> bit) & 1);
    # return binary

# P = number of registers
# larger P = larger memory, more accuracy

import mmh3
from array import array

b = 14
h = mmh3.hash64("Casimirasdasdasdadasd", signed=False)[0]
print("The hash is: ", h)
print("The binary of the hash is: ", bin(h))

M = array('B', [0] * 2**b) # 2^b unsigned byte registers

# 1. hash
# 2. find register index
# 3. compute trailing zeros
# 4. update register
def add(v: int):
    h = mmh3.hash64(str(v), signed=False)[0]
    print("hash: ", h)
    
    mask = (1 << b) - 1
    j = h & mask
    print("j is ", j)
    w = h >> b
    print("w is ", w)
   
    num = 0
    ne = w.bit_length()
    while(num < ne and (w >> num) & 1 == 0):
        num += 1
    
    M[j] = max(M[j], num)
    

print(add(1234232))