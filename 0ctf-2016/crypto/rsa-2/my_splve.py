import gmpy2

with open('flag.enc', 'rb') as f:
    s = int.from_bytes(f.read(), 'big')

n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067

for k in range(10000000):
    d = gmpy2.iroot(s + n * k, 3)
    print(d)
    if d[1]:
        print(int(d[0]).to_bytes((int(d[0]).bit_length() + 7) // 8, 'big'))
        break
