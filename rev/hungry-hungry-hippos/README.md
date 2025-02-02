# Hungry Hungry Hippos

Reverse engineering challenge written in Go.

The strings gave a state that decoded to the flag.

To retrieve the initial state, the software hashes the first letter:
`sha256('B') -> df7e....`
Note that the original state *also* starts with df7e.
Then, for each iteration, the first 30 bytes of the new hash is XORed with the SHA256 of the previous state.
The last 2 stay intact, then the character the user inputs is appended to create the state.

The only thing that is not reversible here is the SHA256, and since we have the first 2 bytes of each state's hash and know everything *except* the single missing character for any given state, it is very feasible to guess each character.

The solve.py script does the guessing and outputs the flag:
```
>py hungry.py
b'37fac12ca49e67fcd17d96e7ef64b1a479d2c985269ec7540db1c41c33a19a5a43'
B
BC b'37fac12ca49e67fcd17d96e7ef64b1a479d2c985269ec7540db1c41c33a19a5a43'
BCC b'e983577a3a049150d9d952a908040b5854c0c2c9e5627329c40d10852f4ed55943'
BCCT b'5f8c29a989a87cc2aff9c275269fa1dd527789309db1292255dbd4ff57ab475f54'
BCCTF b'e5a75a2fe276b87a68f14cc466721451260e68c99e74eb780ed704d118cff5f146'
BCCTF{ b'4cfc141a610f5c222009e3791f7fb917a561ad56dd6be067957e8763b033f1607b'
...
BCCTF{N0m_n0M_NoM_Nom_N0W_1m_fu1 b'd4ff538c922fcb2bf39cfc0fac38b8eb821a474a86e118f561f97af6784648eb31'
BCCTF{N0m_n0M_NoM_Nom_N0W_1m_fu11 b'7b78a2b80cf31e5a89ace54b0fcffbab5e35fae6cd5b7f4bb70cd052898c188a31'
BCCTF{N0m_n0M_NoM_Nom_N0W_1m_fu11} b'076b88fdd662220ac6a578ce2cf627925d893d3f53b6bdb6fa297d4afa84d1a27d'
```