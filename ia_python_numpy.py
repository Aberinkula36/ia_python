# Tarea evaluable nº5 José Miguel Sáez Teruel parte 1

import matplotlib.pyplot as plt

# Array original
array = [1, 2, 3, 4, 5]

# Calcular el cuadrado de cada elemento
cuadrados = [x**2 for x in array]

# Crear el gráfico
plt.plot(array, cuadrados, marker='o', linestyle='-', color='b', label='y = x^2')

# Añadir etiquetas y título
plt.xlabel('Elementos del array (x)')
plt.ylabel('Cuadrados (y = x^2)')
plt.title('Gráfico de y = x^2')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)  # Añadir una cuadrícula
plt.show()