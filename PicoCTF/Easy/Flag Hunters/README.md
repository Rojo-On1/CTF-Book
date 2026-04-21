La flag se encuentra en una linea superior, para obtener la flag debemos retornar a la linea 1 y leer su contenido
para ello nos aprovechamos de este codigo inseguro:

```python
for line in song_lines[lip].split(';'):
```

Cada linea es determinada por un `;`, teniendo en cuenta que la instruccion que hace saltar el programa es `return`
la solucion de nuestro reto seria el siguiente payload.

```
;RETURN 0
```

Obteniendo asi la flag:

`picoCTF{70637h3r_f0r3v3r_a5202532}`