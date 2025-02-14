# Bucle While : Permite ejecutar un bloque de código rápidamente mientras se cumpla una condición

#Condición simple

print("Condicion Simple")

contador = 0
while contador >= 5:
    print(contador)
    contador +=1 #esto evita un bucle infinito

contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle
  
#Bucle con 'Continue'
contador = 0
while contador < 10:
   contador +=1

   if contador % 2 == 0:
      continue
   print (contador)

#Bucle con 'else'

print("Bucle con else")
contador = 0
while contador < 5:
   print(contador)
   contador +=1
else:
   print("El bucle ha terminado")



print("Bucle con else")
contador = 0
while contador < 5:
   print(contador)
   contador +=1
   break #despues de aqui no pasa al 'else' porque el break rompió el bucle
else:
   print("El bucle ha terminado")

