def flip(value):
    num_bytes = max(1, (value.bit_length() + 7) // 8)
    b = value.to_bytes(num_bytes, byteorder='big')
    # Reverse the bytes (flip endianness)
    return b[::-1]

def xor(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

values = [
    0x7f04487763707073,
    0x435d4005406c0405,
    0x734107796803406e,
    0x4c
]
    
key = b"1337" 

decrypted_chunks = []

for val in values:
    decrypted = xor(flip(val), key)
    print(decrypted.decode(), end="")

#BCCTF{7H47_w4snt_s0_H4rD}