#Listas Metodos

lista1= ['a', 'b', 'c', 'd']

## Añadir o insertar elementos a la lista

# lista1.append('e') #Añade un element al final de la lista
# print(lista1)

# lista1.insert(4, 'e') #Inserta un elemento en la posición que le indiquemos como primer argumento
# print(lista1)

# lista1.extend(['f', 'g', 'h']) #Agrega elementos al final de la lista
# print(lista1)


##Eliminar elementos de la lista

# lista1.remove('a')
# print(lista1)

# lista1.pop(-1) #Elimina el ultimo elemento de la lista
# print(lista1)

# del lista1[-1] #Tambien elimina elementos de la lista a lo bestia
# print(lista1)

# lista1.clear() #Elimina todos los elementos de la lista
# print(lista1)

#Eliminar un rango de elementos
# del lista1[1:3]
# print(lista1)

#Ordenar listas
# numbers= [10, 6, 8, 3, 4, 1, 2]
# numbers.sort()
# print(numbers)

# #Ordenar listas creando nueva lista
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# print("Ordenar una lista de cadenas de texto (todo minúscula)")
# frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
# sorted_frutas = sorted(frutas)
# print(sorted_frutas)

# print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
# frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
# frutas.sort(key=str.lower)
# print(frutas)

# animals = ['🐶', '🐼', '🐨', '🐶']
# print(len(animals)) # Tamaño de la listas -> 4
# print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
# print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
# print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
# lista=[1,2,3,4,5]
# lista.append(6)
# lista.insert(1, '10')
# print(lista)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# lista_a.extend(lista_b)
# print(lista_a)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del lista[2:5]
# print(lista)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# numeros = [5, 2, 8, 1, 9, 4, 2]
# numeros.sort()
# print(numeros)  # [1, 2, 2, 4, 5, 8, 9]

# count_2 = numeros.count(2)
# print(count_2)  # 2

# is_7_in_list = 7 in numeros
# print(is_7_in_list)  # False


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# original = [1, 2, 3]

# # Crea una copia de la lista original llamada copia_1 usando slicing.
# copia_1 = original[:]

# # Crea otra copia llamada copia_2 usando copy().
# copia_2 = original.copy()

# # Crea una referencia a la lista original llamada referencia.
# referencia = original

# # Modifica el primer elemento de la lista referencia a 10.
# referencia[0] = 10

# # Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
# print("original:", original)
# print("copia_1:", copia_1)
# print("copia_2:", copia_2)
# print("referencia:", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
# frutas = ["Manzana", "pera", "BANANA", "naranja"]
# frutas.sort(key=str.lower)
# print(frutas)