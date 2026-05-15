from random import randint

inf = int(input("Ingrese un límite inferior: "))
sup = int(input("Ingrese un límite superior: "))

num = randint(inf, sup)

if num % 2 != 0:
    num += 1
    if num >= sup:
        num -= 1

int1 = int(input("Intente adivinar: "))

if int1 != num:
    if int1 < num:
        print("El número es mayor.")
    elif int1 > num:
        print("El número es menor")

    int2 = int(input("Intente de nuevo: "))

    if int2 > num:
        print("El número es mayor.")
        if num < int1:
            print(f"Te daré una pista: El número que buscas está más cerca de {int2} que de {int1}")
        else:
            print(f"Te daré una pista: El número que buscas está más cerca de {int1} que de {int2}")
    elif int2 < num:
        print("El número es menor")
        if num > int1:
            print(f"Te daré una pista: El número que buscas está más cerca de {int2} que de {int1}")
        else:
            print(f"Te daré una pista: El número que buscas está más cerca de {int1} que de {int2}")
    
    if int2 != num:
        int3 = int(input("Intente una última vez: "))

        if int3 != num:
            print("Perdiste.")
            print(f"El número era: {num}")
        else:
            print("Felicitaciones, adivinó en su último intento.")
    else:
        print("Felicitaciones, adivinó en su segundo intento.")
else:
    print("Felicitaciones, adivinó en su primer intento.")