import base64
from Crypto.PublicKey import RSA

with open('redacted') as f:
	c = f.readlines()

c = "".join(c[1:-1])
c = base64.b64decode(c)

# e
e_begin = 0x10e
e_length = 0x3

# p
p_begin = 0x0218
p_length = 0x81

# q
q_begin = 0x29c
q_length = 0x81

e = int.from_bytes(c[e_begin:e_begin + e_length], byteorder='big')
p = int.from_bytes(c[p_begin:p_begin + p_length], byteorder='big')
q = int.from_bytes(c[q_begin:q_begin + q_length], byteorder='big')

print(e)
print(p)
print(q)

n = p * q
d = RSA.inverse(e, (p-1)*(q-1))
res = RSA.construct((n, e, d, p, q))

with open('private_key', 'wb') as f:
	f.write(res.exportKey())