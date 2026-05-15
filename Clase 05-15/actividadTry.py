totalIngresos = 0

print("Venta de pasajes")
while True:
    try:
        psj = int(input("Ingrese la cantidad de pasajes que desea vender: "))
        break
    except ValueError:
        print("Error, el valor debe ser númerico.")

for i in range(psj):
    try:
        val = float(input(f"Ingrese el valor del {i + 1}° pasaje: "))
        totalIngresos += val
    except ValueError:
        print("Necesitas ingresar un valor numérico.")
        break
    
print(f"Total de ingresos de las ventas: ${totalIngresos:,.0f}")