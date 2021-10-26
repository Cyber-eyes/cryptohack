from binascii import unhexlify

def bxor(ba1,ba2):
    return bytes([_a^_b for _a,_b in zip(ba1,ba2)])
    
k1=bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
print(k1)
a=bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
print(a)
k2=bxor(a,k1)
print(k2)
b=bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
print(b)
k3=bxor(b,k2)
print(k3)
c=bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
print(c)
f=bxor(k1,k2)
f2=bxor(f,k3)
flag=bxor(f2,c)
print(flag)
