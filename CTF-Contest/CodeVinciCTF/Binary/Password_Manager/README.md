Revisamos el binario con strings y vemos las cabecera de upx
Por lo que podemos ver que fue comprimido con upx

Descomprimimos el binario con 
```bash
upx -d PasswordManager
```

Ahora al revisarlo podemos ver la contrasena para entrar al binario
```
CiaoSonoBenjaminQuestaPasswordNonLaVedraiMai
```
Obteniendo la [flag](https://github.com/Rojo-On1/CTF-Book/blob/main/CTF-Contest/CodeVinciCTF/Binary/Password_Manager/images/flag.png)
