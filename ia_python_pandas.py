# Tarea evaluable nº5 José Miguel Sáez Teruel parte 2

import pandas as pd

# Datos de los estudiantes
data = {
    'Nombre': ['Ana', 'Oceania', 'Marta', 'Julie', 'Pablo'],
    'Edad': [20, 21, 19, 22, 20],
    'Calificación': [85, 90, 88, 92, 87]
}

# Añadir columna 'Aprobado'
data['Aprobado'] = ['Aprobado' if calificacion >= 60 else 'Suspenso' for calificacion in data['Calificación']]

# Calificación promedio
promedio = sum(data['Calificación']) / len(data['Calificación'])

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Mostrar la calificación promedio
print(f"\nCalificación promedio: {promedio}")
# Crear el DataFrame
df = pd.DataFrame(data)