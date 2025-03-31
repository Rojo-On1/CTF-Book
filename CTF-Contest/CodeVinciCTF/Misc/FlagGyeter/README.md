Primero formatearemos el texto: 

```bash
- sed -e "s/yap/print/g" chall.gyat
- sed -e "s/glaze/import/g" chall.gyat
- sed -e "s/: /\n\t/g" chall.gyat
- sed -e "s/char/print/g" chall.gyat
- sed -e "s/chat is this real/if/g" chall.gyat
- sed -e "s/only in ohio yap/else/g" chall.gyat
```
El resto queda por definir por el usuario

La clave esta en enviar cadenas hasta alcanzar una determinada longitud
