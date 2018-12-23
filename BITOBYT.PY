import math
for _ in range(int(input())): #number of test cases
    time = int(input())
    byte, nibble, bit = 0,0,0
    if time%26 > 10:
        byte = 2**(time//26) 
    elif time%26 <= 10 and time%26 > 2:
        nibble = 2**(time//26)
    elif time%26 == 0:
        byte = 2**((time//26) - 1)
    else:
        bit = 2**(time//26)
    
    print(bit, end = " ") # bit 
    print(nibble, end = " ") # nibble
    print(byte) # byte
