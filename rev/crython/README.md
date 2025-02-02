# Crython
Crython was a *very large* Python file that verified the flag.

To reverse Crython, first I folded constants recursively using an AST NodeTransformer. The application used unary (single parameter) and binary (two parameter) operations of various types that I had to implement in my NodeTransformer, and also calls to sum() that had to be implemented and folded as well.

This left with a script looking something like this:

```py
if (f & 1) << 162 ^ (f & 2) << 291 ^ (f & 4) << 294 ^ (f & 8) << 67 ^ (f & 16) << 294 ^ (f & 32) << 276... ^ 14154190239817593391562602231552196407925674789718962804833972736086242830332675315723974651
```

At this point it was just a matter of rearranging the bits. Each bit in the number corresponded to a bit in the flag, but it was just jumbled up a bit.

To rearrange the bits I just used some regex magic to extract each bit and compare them to the number in the if statement.

Flag: `BCCTF{D0n7_cry_175_4LL_g01n6_t0_b3_0K}`