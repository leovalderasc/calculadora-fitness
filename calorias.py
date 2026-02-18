peso = float(input("Peso en kg: "))
altura = float(input("Altura en cm: "))
edad = int(input("Edad: "))

calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5

print("Tus calorías de mantenimiento aproximadas son:", int(calorias))
