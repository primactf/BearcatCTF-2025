import random
from time import time
import binascii
info = binascii.unhexlify("9d80c4df97fe91a0bb2867c78700c43c4eeb92770ea6ca6934bbcd5ffd40d548aba049344921e1db129e94a382f6678d")
def xor(bytes1, bytes2):    
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

def pad(plaintext, length):
    pad_len = length - (len(plaintext)%length)
    return plaintext + bytes([pad_len]*pad_len)

def decrypt(plaintext, timemulti):
    key = timemulti
    random.seed(key)
    blocks = []
    for i in range(0,len(plaintext),4):
        ct_block = xor(plaintext[i:i+4],random.randbytes(4))
        blocks.append(ct_block)
    ciphertext = b''.join(blocks)
    return ciphertext

timestamp = int((1738088104.0781597 - (19.936517) + 14.456260) * 2 ** 16)
for i in range(-100000, 100000):
    x = decrypt(info, timestamp+i)
    if x.startswith(b"BCCTF"):
        print(x)
        break