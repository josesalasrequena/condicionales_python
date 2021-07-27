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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print('Introduzca palabra 1:')
palabra1 = input()

print('Introduzca palabra 2:')
palabra2 = input()

print('Introduzca palabra 3:')
palabra3 = input()

print('como quieres ordenar las palabras 1: orden alfabético o 2: cantidad de letras')
orden = input()
if orden == 1:
    # mayor palabra
    if (palabra1 > palabra2) and (palabra1 > palabra3):
        print (palabra1,'es la mayor palabra')
    if (palabra2 > palabra1) and (palabra2 > palabra3):
        print (palabra2,'es la mayor palabra')
    if (palabra3 > palabra1) and (palabra3 > palabra2):
        print (palabra3,'es la mayor palabra')
    # menor palabra
    if (palabra1 < palabra2) and (palabra1 < palabra3):
        print (palabra1,'es la menor palabra', )
    if (palabra2 < palabra1) and (palabra2 < palabra3):
        print (palabra2,'es la menor palabra')
    if (palabra3 < palabra1) and (palabra3 < palabra2):
        print (palabra3,'es la menor palabra')
    
else:
    # mayor palabra
    if (len(palabra1) > len (palabra2)) and (len(palabra1) > len (palabra3)): 
        print (palabra1,'es la mayor palabra')
    if (len(palabra2) > len (palabra1)) and (len(palabra2) > len (palabra3)): 
        print (palabra2,'es la mayor palabra')
    if (len(palabra3) > len (palabra1)) and (len(palabra3) > len (palabra2)): 
        print (palabra3,'es la mayor palabra') 
    # menor palabra
    if (len(palabra1) < len (palabra2)) and (len(palabra1) < len (palabra3)): 
        print (palabra1,'es la menor palabra')
    if (len(palabra2) < len (palabra1)) and (len(palabra2) < len (palabra3)): 
        print (palabra2,'es la menor palabra')
    if (len(palabra3) < len (palabra1)) and (len(palabra3) < len (palabra2)): 
        print (palabra3,'es la menor palabra') 

