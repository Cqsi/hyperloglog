import mmh3
from array import array
import random

b = 14
m = 2**b

M = array('B', [0] * m) # 2^b unsigned byte registers

# 1. hash
# 2. find register index
# 3. compute trailing zeros
# 4. update register
def add(v: int):
    h = mmh3.hash64(str(v), signed=False)[0]
    
    mask = (1 << b) - 1
    j = h & mask
    w = h >> b
   
    num = 1
    ne = 64 - b
    while(num < ne and (w >> (ne - num)) & 1 == 0):
        num += 1
    
    M[j] = max(M[j], num)

def count():
    Z = 0
    for i in range(m):
        Z += 2**(-M[i])
    Z = 1/Z
    a_m = 0.7213/(1+1.079/m)

    return a_m*m**2*Z

length = 10000000
comp = set()

for i in range(length):
    ran = random.randint(1, length)
    add(ran)
    comp.add(ran)
    if i%(int(length/10)) == 0:
        print(str(i/length*100)+"%")


print("HyperLogLog: ", count())
print("Actual: ", len(comp))