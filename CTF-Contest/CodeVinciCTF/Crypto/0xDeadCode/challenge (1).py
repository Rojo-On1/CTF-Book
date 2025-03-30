#! /bin/python3

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import signal

from secret import FLAG
assert FLAG.startswith(b"CodeVinciCTF{")
assert FLAG.endswith(b"}")

TIMEOUT = 300

# CodeVinci's secret sauce
def encrypt(m: int, n: int, e: int) -> int:
    return pow((m ** 3 + m ** 2 + 0xdeadc0de) % n, e, n)

def handle():
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    e = 65537
    m = bytes_to_long(FLAG)
    c = encrypt(m, n, e)
    print(f"n: {hex(n)}")
    print(f"e: {hex(e)}")
    print(f"Ciphertext: {long_to_bytes(c).hex()}")

def timeout_handler(signum, frame):
    exit(0)

signal.signal(signal.SIGALRM, timeout_handler)

if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
