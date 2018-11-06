import math
for _ in range(int(input())):
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
    
    print(bit, end = " ")
    print(nibble, end = " ")
    print(byte)
