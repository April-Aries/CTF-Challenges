encoded_flag = open("enc").read()
flag = ""

# Encode: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
for i in range(0, len(encoded_flag)):
    character1 = chr((ord(encoded_flag[i]) >> 8))
    character2 = chr(encoded_flag[i].encode('utf-16be')[-1])
    flag += character1
    flag += character2

print("Flag: " + flag)
