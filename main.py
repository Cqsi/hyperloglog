# Your first step is implementing add — the function that takes an object, hashes it, and updates the right register.
# To do that you need to figure out two things from the hash integer: how to extract the low P bits to get the register index, and how to find the position of the first 1 bit in the remaining upper bits. Both are just integer bit operations. Get those two things working and printing correctly before touching anything else.

import mmh3

h = mmh3.hash64("hello world", signed=False)[0]
#print(h)