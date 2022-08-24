"""
Leetcode Problem 190
Reverse Bits
"""

def reverseBits(n): 
    reversed = '{:032b}'.format(n)[::-1]
    return int(reversed,2)




#n = 0b00000010100101000001111010011100
n = 0b11111111111111111111111111111101 
print(reverseBits(n))