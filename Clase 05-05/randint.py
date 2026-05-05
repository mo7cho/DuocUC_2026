from random import randint

frc_min = int(input("Ingrese una frecuencia mínima: "))
frc_max = int(input("Ingrese una frecuencia máxima: "))
rango = randint(frc_min, frc_max)

# 1.- Generación de frecuencia
print(f"La frecuencia generada es: {rango}")

# 2.- Ajuste de frecuencia
if rango % 5 == 0:
    rango += 1
    print(f"La frecuencia es múltiplo de 5, su ajuste es: {rango}")

    if rango > frc_max:
        print(f"La frecuencia supera el máximo ingresado, su ajuste es: {rango}")
        rango +- 2
else:
    print("La frecuencia no es múltiplo de 5")