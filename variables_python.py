import sys

#Definir variables 
entero = 15
flotante = 2.5
cadena = "Hola"

#Concatenacion
resultado_concatenacion = cadena + str(entero) + str(flotante)
print("Resultado de la concatenación:", resultado_concatenacion)

#Límite de enteros:
# Python no tiene límite teórico para enteros, pero está limitado por la memoria del sistema.
# En sistemas de 64 bits, el límite es 2^63 - 1.
print("Límite de enteros en Python:", sys.maxsize)

#Límite de flotantes:
# El límite para los flotantes está dado por la constante sys.float_info.max.
# Sin embargo, pueden ocurrir errores de redondeo en cálculos muy grandes.
print("Límite de flotantes en Python:", sys.float_info.max)

# La suma de los primeros n números pares es n * (n + 1).
n = int(input("Ingrese un número entero para n: "))
suma_pares = n * (n + 1)

print(f"Suma de los primeros {n} números pares:", suma_pares)