import base64

def encoder(input_str, key):
    encoded_chars = []
    for i in range(len(input_str)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(input_str[i]) - ord(key_c)) % 256)
        encoded_chars.append(encoded_c)
    encoded_str = ''.join(encoded_chars)
    return encoded_str

ciphertext = "wpbCi8KIwpfCh8OPwph5wqnCosK6woTCqcKnwq13wrfCh8KzwqnCpMKKccOJwrh8wqTCl3LDgcKHw4U="
key = "THECAT"
print(encoder(base64.b64decode('wpbCi8KIwpfCh8OPwph5wqnCosK6woTCqcKnwq13wrfCh8KzwqnCpMKKccOJwrh8wqTCl3LDgcKHw4U=').decode(), key))