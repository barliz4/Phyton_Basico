"""
lista = [1,2,3,4, 5,6,7,8,9]
print (lista)
print(len(lista))
print(type(lista))
for i in range (len(lista)):    #Len = Longitud
    print(lista[i])

    elemento = input ("Agregar elementos a la lista \n")
    lista.append(float(elemento))
    print(lista)
"""

lista = [1, 2, 3]
elemento = lista.pop()  # elemento es 3, lista ahora es [1, 2]
print (lista)


