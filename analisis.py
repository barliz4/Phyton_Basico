import pandas as pd

# Crear un DataFrame
# df = pd.read_csv("poblacion.csv")
# print(df)
# df.to_csv("archivo.csv")

df = pd.read_csv("poblacion.csv")

df.to_csv("poblacion.csv")
print(df.tail(5))
