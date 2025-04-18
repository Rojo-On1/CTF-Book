Si revisamos el codigo fuente vemos en la funcion check_password.

```cpp
void check_password(char *pass)

{
  long End_canary;
  int contador;
  undefined8 pass_part1;
  undefined4 pass_part2;
  long Canary;
  
  Canary = *(long *)(End_canary + 0x28);
  pass_part1 = 0xfa96cdd1fad195cb;
  pass_part2 = 0xc291c9c3;
  strlen(pass);
  contador = 0;
  do {
    if (7 < contador) {
      printf("Correct! Here\'s your flag: texsaw{%s}\n",pass);
salir:
      if (Canary != *(long *)(End_canary + 0x28)) {
        __stack_chk_fail();
      }
      return;
    }
    if (((int)pass[contador] ^ 0xa5U) != (uint)*(byte *)((long)&pass_part1 + (long)contador)) {
      puts("Wrong password!");
      goto salir;
    }
    contador = contador + 1;
  } while( true );
}

```

La contrasena son una serie de bytes xoreados con 0xa5 los cuales podemos descifrar con le codigo siguiente.

```python
from pwn import p64,log
PASSWORD = [0xfa96cdd1fad195cb,0xc291c9c3]
password_hex = p64(PASSWORD[0]) + p64(PASSWORD[1]).replace(b"\00",b"")
FLAG = bytes(b ^ 0xA5 for b in password_hex).decode()
log.success("FLAG: texsaw{" + FLAG + "}")
```

y conseguimos la flag:

```
FLAG: texsaw{n0t_th3_fl4g}
```
