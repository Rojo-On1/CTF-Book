#! /bin/python3

from Crypto.Util.number import bytes_to_long, getPrime
import string
import random
import signal

from secret import FLAG
assert FLAG.startswith("CodeVinciCTF{")
assert FLAG.endswith("}")

TIMEOUT = 300


secret_seed = bytes_to_long(FLAG.encode())

def banner():
    print("""
-----------------------------------------------------

oooooooooo.  ooooooooo.   ooooo      ooo   .oooooo.    
`888'   `Y8b `888   `Y88. `888b.     `8'  d8P'  `Y8b   
888     888  888   .d88'  8 `88b.    8  888           
888oooo888'  888ooo88P'   8   `88b.  8  888           
888    `88b  888`88b.     8     `88b.8  888     ooooo 
888    .88P  888  `88b.   8       `888  `88.    .88'  
o888bood8P'  o888o  o888o o8o        `8   `Y8bood8P'   

-----------------------------------------------------

Welcome to BRNG (Big Random Number Generator), every big number lover's favorite place!
This is the trial version, so you will only receive three generation tokens.
    """)

def menu(tokens):
     if input(f"\nPress Enter to generate a new random number (you have {tokens} tokens left)") != "":
         print("\nAn error occurred—maybe if you had just pressed Enter, this wouldn’t have happened.")
         exit(0)

def handle():

    tokens = 3

    public_seed = getPrime(1024) * getPrime(1024)

    banner()

    while tokens > 0:
        menu(tokens)
        if not pow(tokens, 2, 4): print(f'\n{public_seed}{"".join(random.choices(string.digits, k=6))}')
        else:
            magic_touch = 0
            while len(str(magic_touch)) != 5:
                magic_touch = getPrime(16)
            print()
            print(pow(secret_seed, magic_touch, public_seed), magic_touch, sep=str(random.randint(0, 9)))
        tokens -= 1
    else: print("\nGoodbye, and thank you for using the trial version of BRNG!")

def timeout_handler(signum, frame):
    exit(0)

signal.signal(signal.SIGALRM, timeout_handler)

if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
