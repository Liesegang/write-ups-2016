import gmpy2
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

c = list(map(int, open('enc.txt').read().split()))

q = int(gmpy2.gcd(c[0]-c[1] + 1, c[1] - c[2] + 1))
for i in range(1,len(c) - 1):
    q = int(gmpy2.gcd(q,c[i] - c[i+1] + 1))

assert gmpy2.is_prime(q)
print("p: found!")

rand = c[0] % q - 1
print("rand: found!")

p = (q - 1) // 2
p2 = int(gmpy2.iroot(p, 2)[0])
p1 = p // p2

while p2 - p1 < 10 ** 9:
    if p == p1 * p2 and gmpy2.is_prime(p1) and gmpy2.is_prime(p2):
        break
    p2 += 1
    p1 = p // p2

assert p == p1 * p2 and gmpy2.is_prime(p1) and gmpy2.is_prime(p2)
print("p1, p2: found!")

d = []

for i, c_i in enumerate(c):
    d.append((c_i - rand - i - 1) // (rand + i) // q)

res = ""
for i in d:
    if pow(i, 2 * p2, q) == 1 :
        res += '0'
    elif pow(i, 2 * p1, q) == 1:
        res += '1'
    else:
        print('err')
        break

res = int(res,2)

print('flag_enc: found!')

c = long_to_bytes(res)
key = long_to_bytes(rand)
aes = AES.new(key[:16], AES.MODE_CBC, key[16:32])
print(aes.decrypt(c).decode('utf-8'))
