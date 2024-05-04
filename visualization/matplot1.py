import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Matplot para hacer un gráfico de barras apiladas
# cambiar documento
df = pd.read_csv(f'../goldendata/files/goldens/g_c_bm.csv')
# sascar filas que sea 0 en like_count y comment_count(cambiar columnas)
df = df[(df['like_count'] > 0) & (df['comment_count'] > 0)]

# definir columnas grafico y valores de cada pila de barra
tiempo = df['Forecast'].values
interacciones = {
    "likes": df['like_count'].values,
    "comentarios": df['comment_count'].values,
}
width = 0.5

fig, ax = plt.subplots()
#cambiar manualmente dependiendo del numero de columnas
bottom = np.zeros(13)

for boolean, social_count in interacciones.items():
    p = ax.bar(tiempo, social_count, width, label=boolean, bottom=bottom)
    bottom += social_count
#definir titulo y leyenda
ax.set_title("interacciones clima")
ax.legend(loc="upper right")

plt.show()