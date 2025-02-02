# Shimbles the E-L-F
Simply using ltrace on this binary will show you that the binary does a strcmp to `elfmagic` with your input.
```bash
anthony@pwn:~$ ltrace ./Shimbles-the-elf 
puts("          __\n         .-'  |\n   "...          __
         .-'  |
        /   <\|
       /     \
       |_.- o-o
       / C  -._)\
      /',        |
     |   `-,_,__,'
     (,,)====[_]=|
       '.   ____/
        | -|-|_
        |____)_)

)                   = 203
puts("Schimbles: Hello, mortal! I am S"...Schimbles: Hello, mortal! I am Schimbles, the enchanted gnome.
)                     = 63
puts("Schimbles: I've encrypted your p"...Schimbles: I've encrypted your precious data and you'll never see it again...
)                     = 78
puts("Schimbles: ...unless you can dec"...Schimbles: ...unless you can decrypt my file.

)                     = 47
printf("Schimbles: Enter the decryption "...)                   = 37
fgets(Schimbles: Enter the decryption key: hello
"hello\n", 128, 0x75b37541aaa0)                           = 0x7ffcc12c1eb0
strcspn("hello\n", "\n")                                        = 5
strlen("Yx9X\331\031\330\231")                                  = 8
strcmp("hello", "elfmagic")                                     = 3
strlen("5\2679\271=\016\216\264\247"\216.-.*\251\211\233")      = 18
printf("\nSchimbles: %s\n", "WRONG! Try again.\n"
Schimbles: WRONG! Try again.

)              = 31
+++ exited (status 0) +++
```

Simply providing `elfmagic` will get you the flag.
```bash
anthony@pwn:~$ ltrace ./Shimbles-the-elf 
puts("          __\n         .-'  |\n   "...          __
         .-'  |
        /   <\|
       /     \
       |_.- o-o
       / C  -._)\
      /',        |
     |   `-,_,__,'
     (,,)====[_]=|
       '.   ____/
        | -|-|_
        |____)_)

)                   = 203
puts("Schimbles: Hello, mortal! I am S"...Schimbles: Hello, mortal! I am Schimbles, the enchanted gnome.
)                     = 63
puts("Schimbles: I've encrypted your p"...Schimbles: I've encrypted your precious data and you'll never see it again...
)                     = 78
puts("Schimbles: ...unless you can dec"...Schimbles: ...unless you can decrypt my file.

)                     = 47
printf("Schimbles: Enter the decryption "...)                   = 37
fgets(Schimbles: Enter the decryption key: elfmagic
"elfmagic\n", 128, 0x75717021aaa0)                        = 0x7ffeb55c4780
strcspn("elfmagic\n", "\n")                                     = 8
strlen("Yx9X\331\031\330\231")                                  = 8
strcmp("elfmagic", "elfmagic")                                  = 0
strlen("\246&&:\260\237\275(\275\237\2657;(5\037\2649")         = 18
puts("\nSchimbles: Ha! You have bested "...
Schimbles: Ha! You have bested me!
)                    = 36
printf("Schimbles: Here is your flag: %s"..., "BCC{n0t_t0day_e1f}"Schimbles: Here is your flag: BCC{n0t_t0day_e1f}
) = 49
+++ exited (status 0) +++
```
Corrected format:
```BCCTF{n0t_t0day_e1f}```