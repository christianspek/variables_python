# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
from __future__ import division


print("Ingrese por consola el primer numero decimal a operar:")
numero_1 = int(input())

print("Ingrese por consola el segundo numero decimal a operar:")
numero_2 =int(input())
print("El valor almancenado en la variable numero_1 es:", numero_1)
print(numero_1)
print("El valor almacenado en la variable numero_2 es:" , numero_2)


# Alumno: Imprima en pantalla los dos números enteros solicitados

# print(....)

# Alumno: Calcule la suma, resta, división y multiplicación
# de los números ingresados numero_1, numero_2

# Crear una variable llamada suma donde se 
# almacene el valor de la suma de las variable numero_1 y numero_2
suma = numero_1 + numero_2


print("El resultado de sumar", numero_1, "y", numero_2, "es", suma)
#el resultado de sumar 10 y 4
# Crear una variable llamada resta donde se 
# almacene el valor de la resta de numero_1 menos numero_2
resta = numero_1 - numero_2
print("El resultado de restar",numero_1,"y", numero_2, "es", resta)
# el resultado de restar 10 y 4 es 6
# Crear una variable llamada division donde se 
# almacene el valor de la division de numero_1 dividido numero_2

# Crear una variable llamada multiplicacion donde se 
# almacene el valor de la multiplicacion de numero_1 por numero_2
division = numero_1 / numero_2
print("El resultado de dividir", numero_1, "y", numero_2, "es", division)
multiplicacion = numero_1 * numero_2
print("El resultado de multiplicar", numero_1, "y", numero_2, "es", multiplicacion)

# Imprima en pantalla todos los resultados
