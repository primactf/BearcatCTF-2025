# What you see
Opening the picture you can read "the password is ctf" in the background of the World Tour section. From there you can do:
```
anthony@pwn:~$ steghide --extract -sf CtfProblem.jpg 
Enter passphrase: ctf
wrote extracted data to "secret-text".
anthony@pwn:~$ cat secret-text 
BCCTF{w34k_s4uc3_4_u}
```