# try:
#     # Código que podría generar una excepción
#     # Dentro de este bloque de código, debes colocar
#     # lo que quieres validar por medio de una
#     # Set de variables, etc...
#     resultado = 10 / 0
# except ZeroDivisionError as nombre_de_excepcion:
#     # Código para manejar la excepción
#     print(f"Se produjo una excepción (error): {nombre_de_excepcion}")
# else:
#     # Código a ejecutar si no se produjo ninguna excepción
#     print(f"No se produjo ninguna excepción")
# finally:
#     # Código a ejecutar siempre, independientemente de si se produjo
#     # una excepción o no
#     print("Este bloque se ejecuta siempre")

# Las excepciones más comunes son:
# 1. Divisiones por cero (10/0). -> ZeroDivisionError
# 2. Tipos de datos incorrectos (Aparece cuando intentas concatenar una cadena con un número). -> TypeError
# 3. Error de valores (Se genera cuando hay un problema con el tipo o valor de los
# datos que estás manipulando, como convertir una cadena no numérica a un número). - > ValueError
# 4. Archivos no encontrados (Dar ubicaciones de archivo no existentes). -> FileNotFoundError
# 5. Error de sintaxis (Se genera cuando hay un error de sintaxis en tu código). -> SyntaxError

# Actividad:
bultos = int(input("Ingrese la cantidad de bultos:"))
valLiv = 1000
valNor = 2000
bultLiv = 0
bultNor = 0

for i in range(bultos):
    try:
        pesoBulto = int(input(f"Ingresa el peso del {i}° bulto (1 - 10kg): "))
    except ValueError:
        print("El tipo de dato es incorrecto")

    if  0 < pesoBulto < 6:
        bultLiv += 1
    elif 6 <= pesoBulto >= 10:
        bultNor += 1
    
totalLiv = valLiv * bultLiv
totalNor = valNor * bultNor
total = totalLiv + totalLiv

print(f"{bultLiv} bulto liviano: {valLiv}")
print(f"{bultNor} bulto normales: {valNor}")
print(f"Valor total a pagar: {total}")

    

# Ejemplos:

# Primer ejemplo
# tieneMasBultos = True
# nroBulto = 1
# valorPagarPorKilo = 0
# valorPesoLiviano = 1000
# valorPesoNormal = 4500
# totalLiviano = 0
# totalNormal = 0
# contadorBultosLivianos = 0
# contadorBultosNormales = 0
# cantidadBultos = int(input("Ingrese cantidad de bultos: "))

# while nroBulto <= cantidadBultos:
#     try:
#         pesoBulto = int(input(f"Ingrese el peso (1 a 10kg) del bulto Nro. {nroBulto}: "))
#     except ValueError:
#         print("Peso del bulto debe estar en el rango de 1 y 10kg.")
#         continue

# if 1 <= pesoBulto <= 5:
#     totalLiviano += valorPesoLiviano
#     contadorBultosLivianos += 1
# elif 6 <= pesoBulto <= 10:
#     totalNormal += valorPesoNormal
#     contadorBultosNormales += 1
# else:
#     print("Peso ingresado incorrecto (1 - 10kg)")

# nroBulto += 1

#  Segundo ejemplo
# try:
#     numerador = float(input("Ingrese el numerador (un número): "))
#     divisor = float(input("Ingrese el divisor (un número diferente de cero): "))

#     if divisor == 0:
#         raise ValueError("¡Error! El divisor no puede ser cero.")
    
#     resultado = numerador / divisor
    
#     print(f"El resultado de la división es: {resultado}")
# except ValueError as ve:
#     print(f"Error: {ve}")
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.")
# finally:
#     print("Fin del programa.")