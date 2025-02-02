# Turing Approved
This challenge was written in the Brainfuck programming language.

My solve solution involved converting it to JS operations using `unfuck`:

```js
var lol = "(code)"
var uf = require('unfuck');

var compiler = uf.compiler({
    type: Uint16Array,
    in: Number,
    out: String,
    width: 9999
});

console.log( compiler.compile(lol))
```

Then I logged the state from time to time in the generated JS until I saw something that looked like ASCII:

```
C:\CTF\bearcat25>node lol2.js
Uint16Array(9999) [
  125, 0, 0, 115, 0, 0, 115, 0, 0, 105, 0, 0,
  119, 0, 0, 115, 0, 0,  95, 0, 0, 101, 0, 0,
  104, 0, 0, 116, 0, 0,  95, 0, 0, 101, 0, 0,
  109, 0, 0,  97, 0, 0, 108, 0, 0,  98, 0, 0,
  123, 0, 0,  70, 0, 0,  84, 0, 0,  67, 0, 0,
   67, 0, 0,  66, 0, 1,   0, 0, 0,   0, 0, 0,
    0, 0, 0,   0, 0, 0,   0, 0, 0,   0, 0, 0,
    0, 0, 0,   0, 0, 0,   0, 0, 0,   0, 0, 0,
    0, 0, 0,   0,
  ... 9899 more items
]
```
I decoded/reversed these ASCII points and got the flag.

Flag: `BCCTF{blame_the_swiss}`