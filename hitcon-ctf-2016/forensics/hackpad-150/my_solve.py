with open('hackpad.pcap', 'rb') as f:
    raw = f.read()

contents = []

indx = raw.find(b'msg=')
target = raw[indx + 4:indx + 4 + 672]
target = target.decode('utf-8')

find = b'msg='
last = indx + 1
while True:
    last = raw.find(find, last + 1)
    if last == -1:
        break
    contents.append(raw[last + 4: last + 4 + 64].decode('utf-8'))

key = []
prev_ln = ""
for line in contents:
    if line.startswith('0' * 30) and prev_ln != "":
        if not prev_ln.startswith('0' * 30):
            key.append(prev_ln[:32])
    prev_ln = line

key.append(contents[-1][:32])


res = ""
for k in key:
    t = target[:32]
    target = target[32:]
    for i in range(16):
        res += chr(int(t[2 * i:2 * i + 2], 16) ^ int(k[2 * i:2 * i + 2], 16) ^ 0x10)

print(res)
