El codigo, en escencia valida byte a byte una cadena ingresada con un conunto de valores cifrados.

Podemos extraer dichos valos mediate gdb

```
gef➤ b main
gef➤ c
gef➤ print solution
```
Estos son los valores de la bandera cifrada, analizando el codigo vemos las siguientes operaciones:

```python
def W_value(char : int,c):
    return char ^ WHAT[c]

def H_value(char : int,c):
    return char + WHAT[c]

def A_value(char : int,c):
    return char * WHAT[c]
```

El programa itera sobre una cadena larga y realiza operaciones ariteticas dependiendo la letra y un contrador interno a la palabra "WHAT", revertimos todo este proceso y obtenemos la flag:

```python
from time import sleep

def decrypt(byte : int, exec_chain : str,counter):
    for action in exec_chain[::-1]:
        if action == "W":
            byte = W_value(byte,counter)
        elif action == "H":
            byte = H_value(byte,counter)
        elif action == "A":
            byte = A_value(byte,counter)
        else:
            return "err"
        counter = (counter - 1) % 4
    return chr(byte)

def W_value(char : int,c):
    return char ^ WHAT[c]

def H_value(char : int,c):
    return char - WHAT[c]

def A_value(char : int,c):
    return char // WHAT[c]

WHAT = b"WHAT"
DATA = "?WAWWHT?WAAWWAHHWAWAAAT?WAAHAAHHAAT?WHAAAHAHAWWHT?WHAAHHAHAWHT?WWHHWWHAAAHHWHT?WHHHHHH HAAT?WHHHHHHWWAHHT?WHAAAHAHAWHHHHHAAHT?WHHWHHAHHAAAHAAHHHT?WHHHAHWHHHAHHHAHAAT?WAAHHAHHHAHHWHHHH HT?WHHHHAHHAHAHWHHHHHT?WHHHHHHHWAHHAHHHHHT?WAWT?WHAAAAAAAWT?WHAAHAAAWAWWT?WAAAHAWAWHHT?WAAAHHHHA T?WAHHWHAHAHT?WAHHHHWWHWHAT?WAHWHHHWHHHT?WAHHAAAHHAAHHAHHT?WHHHAHWWHAHAHAWHHAAT?WAHWHHHWAAHHHWAH HHAWT?WAHHHHHAAHHHWHAHHT?WHHHHHAHHAHHHHHAT?WHHHHHHWWHAHWHHHAHHT?WHHHHHHWHHWHWHWHHHAHT?WAAWAAAAAT ?WHAAAAAWWAT?WAWWHWWHAAAAT?WAAAAWWHHHWT?WHAHHAAHWT?WHWHWAHHAHT?WHAHHWWWHWHHT?WHHAHHHHAAAWHAAWAWT ?WWAWHAHHHAHHAWHAAHT?WHHAHHHHWAAHAWHHAWT?WAHHAHWAHHWHHAHWHHT?WHAHHHHWHHAWHHHWAHT?WWHWAHHHHHHHAHH HHWT?WHHWWHHWHAHHHHHHHHT?WHWHHHHHAAHWAHHHHAAHAHWHAT?WAAAAAAT?WWAAWHAWAWAT?WAAAWAHWHT?WHAHWAHAWWT ?WHHHHAAT?WWHAHHHHWWWT?WHHWAWAAAHAHAHHAT?WHAAHHAHAAHAHHT?WWAHHHHHAHHHAAAT?WAHAHHHWHHAHHHWWAT?WHH HHHAWHAHHHWAHT?WHHHHHAHAHHHHHT?WHHHWHHAHHHHHHHT?WHHAHHHWAHAHAWHHAHAAHHHWT?WHAHAHWHHWHAHAAHHHHWHW HAHT?WAAAWAAT?WAAAAHT!".replace(" ","").replace("T","").split("?")[1:]

SOLUTION = (0xf54, 0x16f4a5e260570, 0x9bd5485c77c, 0x523e921c64, 0x131a573ad, 0x8f0366a, 0x31923c, 0x8045, 0x7bdd4f2f841e4, 0x95916508bfe9, 0x8be32212f8, 0x96a96236, 0x8f505cc, 0x2ba72f, 0xd79, 0x67f100a7fe057, 0x165f086e2afb, 0xe629b2305, 0x4759f2cc, 0x1067699, 0x15e23,0xfed, 0xa58a6ff5e80c3, 0x420719f56d10, 0xde2c53af7, 0x869bf143, 0xda18d18, 0x3b669b, 0x10197, 0x2f5ff57445d00, 0x2d028a7a55f4, 0x16d07ce160, 0x5dc6247d, 0x2b0a9cd, 0x1ee163, 0x442c, 0x10deb1377a1730, 0x15288f08a6d8, 0x769ffa893b, 0x16c9a3fc, 0x42356fe, 0x1ca845, 0xae04, 0x2acbc4c1348ca7, 0x156652f56900, 0x141a6b0269, 0x85044ca1, 0x4233d6b, 0x27cf3c, 0x3279, 0x11ab80fced20e4, 0x1d631a31a393, 0x414d72a784, 0x5e787f58, 0x13497804, 0x260b58, 0x9a54, 0xa5d9dfc502eaa, 0x135ac1bc1242, 0x18d84f7478, 0x5394c6b7)

flag = ""
for i in range(len(SOLUTION)):
    counter = (len("".join(DATA[:i+1]))-1) % 4
    print(f"\r[+] FLAG: {flag}",end="")
    flag += decrypt(SOLUTION[i],DATA[i],counter)
    sleep(0.1)
```

Obteniendo asi la flag:
```
[+] FLAG: bctf{1m_p3rplexed_to_s4y_th3_v3ry_l34st_rzr664k1p5v2qe4qdkym}
```
