Para solventar el reto se tomaron dos caminos.

1. La via que codifique rapidamente sin intentar entender el funcionamiento de la funcion, a base de fuerza bruta.

```python
import string
from itertools import product
import time
CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}-"

def make_char(pair: tuple) -> str:
    return chr((ord(pair[0]) << 8) + ord(pair[1]))

combos = [a+b for a in CHARS for b in CHARS]    
flag_enc = open('enc','r',encoding="utf-8").read().strip()

flag = ""

for char in flag_enc:
    for candidate in combos:
        if make_char(candidate) == char:
            flag += "".join(candidate)
            print(f"\r\rFLAG: {flag}",end="")
            time.sleep(0.05)
            break
```

Teniendo en cuenta que cada caracter se crea utilizando dos valores, probe todas las combinaciones posibles de dos valores hazta coincidir una a una.

2. La via logica.
Leyendo un poco nos damos cuenta que es una operacion sencilla de entender.

- A nivel binario aplica un desplazamiento dejando un espacio de 8 bits a la derecha.
- Luego rellena ese espacio con el caracter siguiente.

Convierte dos caracteres en uno.

Para revertir esto es sencillo, desplazamos 8 bits a la derecha para obtener el primer valor y aplicamos una mascara para obtener el segundo y separar los 16 bits en dos 8 bits.

```python
flag = open('enc','r',encoding="utf-8").read().strip()
print("".join([bytes((ord(i) >> 8,ord(i) & 0xFF)).decode() for i in flag]))
```