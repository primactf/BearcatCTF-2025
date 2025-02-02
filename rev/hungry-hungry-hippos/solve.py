import hashlib
import binascii
import string
alphabet = string.ascii_letters + "01234567890{}_-"
def sha256_hash(data):
  if isinstance(data, str):
    data = data.encode('utf-8')
  sha256_hash = hashlib.sha256(data)
  return sha256_hash.hexdigest()
def xor(bytes1, bytes2):    
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))
def sha256_hex(data):
  if isinstance(data, str):
    data = data.encode('utf-8')
  sha256_hash = hashlib.sha256(data)
  return sha256_hash.digest()   
data = "df7e37fae9835f8ce5a74cfca4b21f846274d39b264308ee3ec776f03acd3eb859b78e7e0286a9a9080b431acc68829532c7b0056b59ce491ed71f1edd86d4ff7b78076b88fdd662220ac6a578ce2cf627925d893d3f53b6bdb6fa297d4afa84d1a2"
lol = binascii.unhexlify(data)

data2 = ""
data3 = ""
prev_chunk = ""
last_hash = ""
last_char = ""

def funny(c1, c2):
    nested_hash = sha256_hex(sha256_hex(c1) + c2)
    return xor(nested_hash, sha256_hex(c1)[2:]) + nested_hash[30:] + c2

for i in range(0, len(data) // 4):
    chunk = data[i*4:i*4+4]
    if prev_chunk == "":
        for j in alphabet:
            hash = sha256_hash(j)
            if hash[:4] == chunk:
                last_hash = hash
                prev_chunk = chunk
                last_char = j
                data3 = hash[:4]
                data2 += j
                print(data2)
                break
    else:
        for j in alphabet:
            hash = binascii.hexlify(funny(last_char.encode(), j.encode()))
            tdata3 = ""
            if data3 != "df7e":
                funny2 = sha256_hex(binascii.unhexlify(data3[:(i-1)*4]) + binascii.unhexlify(last_hash) + j.encode())
                tdata3 = xor(binascii.unhexlify(data3[(i)*4:-4]), funny2) + funny2[30:] + j.encode()
                hash = binascii.hexlify(tdata3)
            if hash[:4].decode("ascii") == chunk:
                last_hash = hash[:-2]
                prev_chunk = chunk
                last_char = j
                data3 = data3[:i*4] + hash.decode("ascii") + binascii.hexlify(j.encode()).decode("ascii")
                data2 += j
                print(data2, hash)
                break
        if len(data2) != i+1: break