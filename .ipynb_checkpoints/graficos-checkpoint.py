import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["A", "B", "C", "D"]    #Estas serán las categorías del eje X del gráfico.
valores = [30, 15, 7, 10]   #Estos valores se usan para determirnar  la altura de las barras

# Crear gráfico de barras
plt.bar(categorias, valores, color="skyblue")   #Se crea un gráifo de barras utilizando la funcion bar 
plt.title("Gráfico de Barras")  #Se establece el el titulo gráfico
plt.xlabel("Categorías")    #El eje X representa, esto se refeleja bajo las barras
plt.ylabel("Valores")   #Las barras representan el eje Y
plt.show()      #Se  muestra el gráfico en una ventana
            


"""  Ejemplo 2
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de líneas
plt.plot(x, y, marker="o", color="green", linestyle="--")
plt.title("Gráfico de Líneas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
"""

"""     Ejemplo 3
# Datos de ejemplo  
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Crear gráfico de dispersión
plt.scatter(x, y, color="purple")
plt.title("Gráfico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
"""


# Datos de ejemplo
datos = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# Crear histograma
plt.hist(datos, bins=5, color="orange", edgecolor="black")
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
            