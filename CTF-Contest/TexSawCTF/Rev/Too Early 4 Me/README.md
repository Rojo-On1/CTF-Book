Al analizar el binario con ghidra encontramos en la funcion main, una funcion que se llama mediante una senal del sistema (ALARM)

```cpp
void sigalrm_handler(void)

{
  decode_flag();
  return;
}
```

si ejecutamos el exploit o el siguiente comando:

```bash
kill -14 {PID}
```
y conseguimos la flag.

```
texsaw{how_signalicious_much_swag}
```
