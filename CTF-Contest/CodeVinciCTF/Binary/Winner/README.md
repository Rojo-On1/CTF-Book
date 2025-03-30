Al analizar el binario con ghidra podemos ver que el tamano del buffer del nombre es de 30 bytes
Vemos una funcion que al comparar un valor aleatorio con el nombre ejecuta cat flag.txt
Empezamos revisando el binario con ltrace y al insertar 30 "a" vemos que podemos sobrescribir la 
primera variable.
Le adicionamos valores nulos hasta sobrescribir el siguiente registro obteniendo la FLAG

python -c "print('a'*30 + '\0'*32)" | ./winner
