from subprocess import Popen,PIPE
from string import printable as chars


def rol(value, shift, n_bits=8):
	return ((value << shift) | (value >>  (n_bits - shift))) & 0xFF

def ror(value, shift, n_bits=8):
	return ((value >> shift) | (value <<  (n_bits - shift))) & 0xFF

def getKeys(seed : int,lenght: int) -> tuple:
	p = Popen(f"./solution {seed} {lenght}",shell=True,text=True,stdout=PIPE)
	return (int(i) for i in p.stdout.read().strip().split() if i.isnumeric())

def encrypt(char, xor_key, rol_key):
	return rol(ord(char) ^ xor_key,rol_key)

def decrypt(char, xor_key, ror_key):
	return chr(ror(char,ror_key) ^ xor_key)

data = open("../flag.enc","rb").read()
seed = int(data[:4][::-1].hex(),16)
ciphertext = data[4:]

flag = ""
keys = getKeys(seed,len(ciphertext))
print("SEED: ",hex(seed))

keys = getKeys(seed,len(ciphertext))
for i in range(len(ciphertext)):
	xor_key = next(keys)
	shift_key = next(keys)
	flag += decrypt(ciphertext[i],xor_key,shift_key)

print("FLAG: ",flag)
