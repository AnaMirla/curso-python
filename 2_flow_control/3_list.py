# Listas

# print("Crear listas")

lista1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2= ["ana", "betsaida", "cecilia", "diana", "esther"]
lista3= [1, "hola", 3.14, True, False]

lista_vacia= []
lista_de_listas= [[1,2], [3,4], [5,6]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

# Acceso a elementos por indice

print("\nAcceso a elementos por indice")
print()
print(lista1[0]) 
print(lista2[1])
print(lista2[-1]) #muestra el ultimo elemento

# Slicing (rebanado) de listas
print(lista1[1:3]) #muestra los elementos de la posicion 1 a la 3
print(lista1[:3]) #muestra los elementos desde el inicio hasta la posicion 3
print(lista1[:]) #Crea una copia de la lista
print(lista1[::3]) #muestra los elementos de la lista saltando de 2 en 2
print(lista1[::-1]) #muestra la lista en orden inverso

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista (forma larga y menos eficiente)
lista1 = lista1 + [11, 12, 13]
print(lista1)

# Añadir elementos a una lista (forma corta y mas eficiente)
lista1 += [11,12,13]
print(lista1)

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:14]
print(mensaje_secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista = [1, 2, 3]
nueva_lista = lista + lista
print(nueva_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
lista = [1,2,3,4,5,6,7,8,9,10]
centro = lista[len(lista)//2]
print(centro)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista= [1, 2, 3, 4, 5, 6]
mitad1 = lista[:len(lista)//2]
mitad2 = lista[len(lista)//2:]
mitad1 = mitad1[::-1]
lista = mitad1 + mitad2
print(lista)