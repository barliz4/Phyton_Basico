import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo 1
datos = np.random.rand(10, 10)

# Crear mapa de calor
plt.imshow(datos, cmap="viridis", interpolation="nearest")
plt.title("Mapa de Calor")
plt.colorbar()
plt.show()
            
#--------------------------------------------------------------------------

# Datos de ejemplo 2
categorias = ["Categoría A", "Categoría B", "Categoría C"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()