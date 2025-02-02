# Times to Die

The RNG for the encryption was seeded on the current microsecond time of the system, multiplied by `2**16` and then converted to an int.

To get the time for the seed, I had to find an NTP packet that was in the provided pcapng.

Then, I just brute forced seed values +/- 100,000 of the value until I got the flag.

Flag: `BCCTF{175_n07_5Ymb0lic_itS_jU57_Hum4n_n47ure}`