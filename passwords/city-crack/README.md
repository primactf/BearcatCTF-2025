# City Crack
> International hackers have left two different encrypted hashes behind. The first hash is `1fae39b5bc83699450281dc7bb472d59`, and the second hash is `5f6b9145ac86d19e917a08e6c20de0c907472a90`. To find the flag, decrypt both hashes and combine the results in alphabetical order, separated by an underscore. These paswords are based off of capital cites with some modifications.

We have an MD5 and SHA1 hash, each of which are based on capital cities modified with some unknown rules.
I first scraped a wordlist of capital cities. (Later on I ended up using another wordlist from my teammate that was cleaned up)

My teammate cracked the MD5 hash with OneRuleToRuleThemAll + leetspeak.rule:

```
1fae39b5bc83699450281dc7bb472d59:T0kyO
```

I later got the SHA1 hash with OneRuleToRuleThemAll + d3ad0ne.rule:

```
5f6b9145ac86d19e917a08e6c20de0c907472a90:p@R!s
```

Flag: `BCCTF{p@R!s_T0kyO}`