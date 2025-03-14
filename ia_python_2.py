# Tarea evaluable nº4 José Miguel Sáez Teruel parte 2
if __name__ == "__main__":
    age = int(input("Por favor, indica tu edad: "))  # Convertir la edad a entero

    # Comprobar la edad del usuario
    if age < 12:
        print("Niño.")  # Niño
    if age > 12 and age <= 17:
        print("Adolescente.")  # Adolescente
    if age > 18 and age <= 64:
        print("Adulto.")  # Adulto
    if age >= 65:
        print("Adulto mayor.") # Adulto mayor