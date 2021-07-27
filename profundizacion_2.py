# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero1 = int(input('Introduzca numero 1:'))
numero2 = int(input('Introduzca numero 2:'))
numero3 = int(input('Introduzca numero 3:'))
numeropar1=numero1%2
numeropar2=numero2%2
numeropar3=numero3%2

if numeropar1==0:
    print (numero1,'es par')
else:
    print (numero1,'es impar')

if numeropar2==0:
    print (numero2,'es par')
else:
    print (numero2,'es impar')

if numeropar3==0:
    print (numero3,'es par')
else:
    print (numero3,'es impar')
