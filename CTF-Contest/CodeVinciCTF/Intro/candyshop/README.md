En el binario se acontece un desbordamiento del rango de los numeros asignados.
Esto lo podemos analizar al leer el codigo, sabemos que si conseguimos introducir un numero
negativo podremos incrementar nuestro capital.

Existe una condicional que nos impide poner numeros negativos sin embargo, si abusamos del desbordamiento
de rango de memoria podemos insertar como valor:

---
Maximo entero = 2147483647
Mimino entero = 2147483649 (-2147483647)
Valor = (2147483649 + 2147483647) - 100
---


Para conseguir asi el monto necesario y ver la flag
