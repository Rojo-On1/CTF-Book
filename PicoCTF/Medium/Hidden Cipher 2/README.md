Este es facil, te piden que ingreses el resultado de la operacion matematica y luego te dan la llave encodeada:

```
"""
What is 4 - 0? 4
Encoded flag values:
448, 420, 396, 444, 268, 336, 280, 492, 408, 388, 428, 404, 380, 408, 432, 388, 412, 500
"""
```

Leyendo un poco el codigo revisamos la funcion como es que encodea la flag


```c
void encode_flag(long flag,int math_question)
{
  int i;
  
  puts("Encoded flag values:");
  for (i = 0; *(char *)(flag + i) != '\0'; i = i + 1) {
    // Aqui esta la magia
    printf("%d",(ulong)(uint)(*(char *)(flag + i) * math_question));

    if (*(char *)(flag + (long)i + 1) != '\0') {
      printf(", ");
    }
  }
  putchar(10);
  return;
}
```

Basicamente multiplica cada caracter por el resultado, es tan simple como dividirlo, aqui el script de solucion:

```python
from pwn import *
import re
    
host = "crystal-peak.picoctf.net"
port = 52049

p = remote(host,port)
match = re.search(r'is (.*?)\?',p.recv().decode())
solution = str(eval(match.group(1)))

log.info(f"Key: {solution}")

p.sendline(solution.encode())

p.recvuntil(b"Encoded flag values:")

flag = ''.join([chr(int(i)//int(solution)) for i in p.recv().decode().strip().split(", ")])

log.success(f"Flag: {flag}")
```

Asi obtenemos la flag:

```
picoCTF{m4th_b3h1nd_c1ph3r_aec6274b}
```



