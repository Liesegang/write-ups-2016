import gmpy2
data = b''

data = int.from_bytes(open("enc.raw", "rb").read(), byteorder='big')
data = int(gmpy2.iroot(data, 65537)[0])
print(data.to_bytes((data.bit_length() + 7) // 8, byteorder='big'))

