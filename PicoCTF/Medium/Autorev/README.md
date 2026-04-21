Este es un reto peculiar aparentemente de `Scripting`. En el debemos responder el secreto en menos de 1 segundo port binario, siendo 20 binarios.

Analizando uno de los binarios que aparecen vemos esto:

```c
0040113e c7 45 fc        MOV        dword ptr [RBP + local_c],0x8670a025
        25 a0 70 86
00401145 c7 45 f8        MOV        dword ptr [RBP + local_10],0x0
        00 00 00 00
```

Donde 0x8670a025 (mejor dicho, su valor entero), es el secreto que nos piden, entonces para obtener los secretos de los binarios debemos buscar las siguientes opcodes `c7 45 fc`, ya que al lado de este se encuentra siempre el secreto.

Para lograrlo usamos este script.

```python
from pwn import *
import time
import os 

def solve(data):
    index = data.find(b"\xc7\x45\xfc") + 3
    secret = int(data[index:index+4][::-1].hex(),16)
    return secret

p = remote("mysterious-sea.picoctf.net", 49658)
progress = log.progress("Solving challenges")

for i in range(20):
    progress.status(f"[{i}/20]")
    data = p.recvuntil(b"What's the secret?:").decode().split("\n")[-2]
    secret = solve(bytes.fromhex(data))
    p.sendline(str(secret).encode())

p.recvuntil(b"flag: ")

flag = p.recv().strip().decode()

progress.success()
log.success(f"Flag: {flag}")
```

Con el cual obtuvimos la flag:

```
picoCTF{4u7o_r3v_g0_brrr_78c345aa}
```
