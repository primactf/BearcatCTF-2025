# OK Jail

Slightly modified explanation from team Discord:



The system runs code in this format:
`builtins.{cell}(ok.{inmate}(*{name}))`
where:
- `name` is arbitrary JSON we can input
- `cell` is any builtin function
- `inmate` is any function on the ok object (probably an int)

`ok` is evaluated but we have a very limited character set (`~(0)|<`).

I found `int.to_bytes` which I figured was our best bet - use the eval builtin to run some short code from an integer converted using to_bytes.
By crafting an `ok` value that is `eval(input())` in integer form using the very limited characters , then setting `inmate` to `to_bytes`, `cell` to `eval`, and `name` to `[13, "big"]` (length 13 in big endian) we now are able to run whatever we want

I generated the `ok` value using some bit shifting / bitwise OR shenanigans. Each bit was generated using a bunch of left shifts by 1 (`(~0<0)<<0<<((~0<0)<<0)` = `1 << 1`, `(~0<0)<<0<<((~0<0)<<0)<<((~0<0)<<0)` = `1 << 2`, etc.)

You can see more of my thought process in `solve.py`.