import numpy as np
import math as m
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

x=np.zeros((4,4))
#print(x)
def add_round_key(x, s, k):
    for i in range(4):
        for j in range(4):
            x[i][j]=state[i][j]^round_key[i][j]
    #print(x)
    return(x)

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    arr=[]
    
    for i in range(0, len(matrix)):
        m=matrix[i]
        for j in range(0,len(m)):
            arr.append(m[j])
    return arr

print(add_round_key(x, state, round_key))
flag=matrix2bytes(x)
print("".join([chr(int(f)) for f in flag]))
