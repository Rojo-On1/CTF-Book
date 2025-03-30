import os
from secret import flag

key = os.urandom(18)

xored = bytes(f ^ k for f, k in zip(flag, key * (len(flag) // len(key) + 1)))

with open("output.txt", "w") as f:
    f.write(f"Key: {key.hex()}\n")
    f.write(f"Ciphertext: {xored.hex()}")
    
# Key: Redacted
# Ciphertext: b3f0716f4a94ef6a6d6ce2b908d52d53c64696af67477dcade387770829324f23852fe78aff3266b5780