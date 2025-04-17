Si aplicamos el siguiente filtro a la captura podemos ver los siguiente:
ip.src == 147.182.177.196 && icmp

![imagen_pings](images/traza.png)

Si tomando el cuante el valor del seq extraemos el contenido vemos la flag:

'''
TexSAW{not_the_fake_one}
'''
