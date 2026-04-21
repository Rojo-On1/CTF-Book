Al ejecutar el binario vemos que nos da la flag encriptada, al intentar hacerle reversing al binario vemos que no tenemos exito, y tampoco me fue posible manejar el depurador para ver como era generado debido a las restricciones del programa.

Sin embargo por intuicion podemos pensar que esto es un cifrado XOR Lineal, al validar esta teoria haciendolo XOR a cada Byte de la flag encriptada con la flag desencriptada.

```py
flag = open("flag.txt","rb")
ct = bytes.fromhex("235a201d70201548251358110c552f135409")
"".join([chr(i^j) for i,j in zip(flag,ct)])

# Salida S3Cr3t....
```


Ya con la llave  podemos descifrar cualquier texto cifrado.

Asi obtenemos la flag:

```
'picoCTF{xor_unpack_4nalys1s_530ca742}'
```

> Nota: Si lees las cadenas imprimibles del binario puedes ver que esta empaquetado con UPX, al desempaquetarlo si buscas la funcion get_secret veras la key igualmente.