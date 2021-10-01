import numpy as np
import pandas as pd
from pandas.core.series import Series

SEPARADOR = ("*" * 20) + "\n"

#Crear una serie con valores iniciales
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(SEPARADOR)



#Crear una serie de 6 elementos que tengan el mismo valor
iguales = pd.Series(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)



#Estadistica Descriptiva para una serie
print('Notas : ')
print(f"{notas}")
print(f"Cantidad = {notas.count()}")
print(f"Media = {notas.mean()}")
print(f"Minimo = {notas.min()}")
print(f"Maximo = {notas.max()}")
print(f"Desviacion Estandar = {notas.std()}")
print("Sumarizacion Descriptiva: ")
print(notas.describe())
print(SEPARADOR)



#Serie con indices personalizados
print("Series con indices personalizados: ")
notas_asignadas = pd.Series([87, 100, 85, 60, 78], index=["Crescencio", "Domitila", "Rutilio", "Panfilo", "Ludoviko"])

print(notas_asignadas)
print(SEPARADOR)




print("Serie generada a partir de un diccionario")
notas_asignadas_dict = pd.Series({"Crecencio":87, "Domitila":100, "Rutilio":85, "Panfilo":60, "Ludoviko":78})

print(notas_asignadas_dict)
print(SEPARADOR)





#Acceso a elementos en una serie por valor de indice
print(f"La calificacion de Rutilio es {notas_asignadas_dict['Rutilio']}")
print(f"La calificacion de Rutilio es {notas_asignadas_dict.Rutilio}")