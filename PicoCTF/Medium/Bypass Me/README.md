Este reto fue bastante facil, me descargue el binario para trabajar local y revisando la funcion `main` con el 
`Ghidra` encontre esto:

```c
sanitize(buf,sanitized);
printf("\nRaw Input:      [%s]\n",buf);
printf("Sanitized Input:[%s]\n",sanitized);
puts("Hint: Input must match something special...");
iVar2 = strcmp(buf,password);
if (iVar2 == 0) {
  auth_sequence();
  __stream = fopen("../../root/flag.txt","r");
  if (__stream == (FILE *)0x0) {
    puts("Flag file not found.");
  }
```

Teniendo en cuenta esta comparacion ponemos un `breakpoint` justo antes de la ejecucion de la funcion `strcmp` y listo, podemos ver la password `SuperSecure`

Una vez ejecutado tenemos que la flag es:

```
picoCTF{d3bugg3r_p0w3r_is_4w3s0m3_9d5f0f68}
```