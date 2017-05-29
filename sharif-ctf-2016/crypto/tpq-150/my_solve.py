import socket
from Crypto.PublicKey import RSA
import gmpy2
import time

def recv_until(f, end='\n'):
    data = b''
    while not data.endswith(end.encode('utf-8')):
        data += f.recv(1)
    return data

host = "ctf.sharif.edu"
port = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

def ask(i, j):
    recv_until(client, '[Q]uit.\n')
    client.send(b'C')
    recv_until(client, ' space.\n')
    client.send('{} {}'.format(i, j).encode('utf-8'))
    res = recv_until(client)
    return int(res.decode('utf-8').split()[-1])

def end():
    recv_until(client, '[Q]uit.\n')
    client.send(b'Q')
    client.close()
    return

c01 = ask(0, 1)
c02 = ask(0, 2)
c03 = ask(0, 3)

c21 = ask(2, 1)
c31 = ask(3, 1)

end()

p = int(gmpy2.gcd(c01 - c02, c02 - c03))
q = int(gmpy2.gcd(c01 - c21, c21 - c31))
assert(gmpy2.is_prime(p))
assert(gmpy2.is_prime(q))

print('p=', p)
print('q=', q)

d = RSA.inverse(65537, (p-1)*(q-1))
rsa = RSA.construct((p * q, 65537, d, p, q))
decrypted = rsa.decrypt(c01)

print(RSA.long_to_bytes(decrypted))
