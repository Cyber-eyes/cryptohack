from Crypto.Util.number import long_to_bytes

p = 986369682585281993933185289261 #prime number 1
q = 752708788837165590355094155871 #prime number 2
e = 3 #encryption key
#n = p * q #prime product
n = 742449129124467073921545687640895127535705902454369756401331
c = 39207274348578481322317340648475596807303160111338236677373 #ciphertext
phi = (p-1)*(q-1)
d = pow(e, -1, phi) #decryption key

pt = pow(c, d, n)
decrypted = long_to_bytes(pt)

print(decrypted)
