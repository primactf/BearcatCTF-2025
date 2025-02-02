# Bonkers Flag Innit
> I recently discovered an obscure Windows filename function! So I picked a random word from the dictionary (with British inspirations) as the flag, and ran it through. Here's the output! --> `FLD20C~1` <--

This is a Windows 8.3 filename, used for backwards compatibility with old DOS operating systems that could only have 8 characters in the filename and 3 in the extension.

The checksum algorithm was reversed and described in this archived blog post, including example source code: https://web.archive.org/web/20150610125659/https://usn.pw/blog/gen/2015/06/09/filenames/ 

From there it was just a matter of bruteforcing the checksum with various words. I chose a wordlist off GitHub from somewhere and it just so happened to have the right word.

Flag: `BCCTF{flibbertigibbet}`