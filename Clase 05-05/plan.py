# Valores base (costos originales)
mat = 120000   # costo de la matrícula
seg = 25000    # costo del seguro

# Se solicita la edad al usuario y se convierte a entero
edad = int(input("Ingrese su edad: "))

# Se solicita el tipo de plan (1, 2 o 3)
plan = int(input("""
Elija su tipo de plan: 
1.- Básico
2.- Pro
3.- Élite
"""))

# Estructura match-case (similar a switch en otros lenguajes)
match plan:
    case 1:  # Plan Básico
        if edad <= 25:
            dcto_mat = 0.10   # 10% de descuento
        elif 26 <= edad <= 50:
            dcto_mat = 0.05   # 5% de descuento
        else:
            dcto_mat = 0.00   # sin descuento

    case 2 | 3:  # Plan Pro o Élite (ambos comparten lógica)
        if edad <= 25:
            dcto_mat = 0.20   # 20% de descuento
        elif 26 <= edad <= 50:
            dcto_mat = 0.15   # 15% de descuento
        else:
            dcto_mat = 0.00   # sin descuento

    case _:  # cualquier otro valor (error)
        print("Error: plan no válido. Intente nuevamente.")

# Cálculo del valor final de la matrícula
# (1 - descuento) representa el porcentaje que sí se paga
val_mat = mat * (1 - dcto_mat)

# Segundo match-case para el seguro
match plan:
    case 3:  # Solo el plan Élite tiene descuento en seguro
        if edad > 40:
            dcto_seg = 0.60   # 60% de descuento
        else:
            dcto_seg = 0.50   # 50% de descuento
    case _:
        dcto_seg = 0.00       # otros planes no tienen descuento

# Cálculo del valor final del seguro
val_seg = seg * (1 - dcto_seg)

# Impresión de resultados usando f-strings con formato
# : → indica que viene un formato
# , → agrega separador de miles
# .0f → número decimal con 0 decimales
print(f"Valor de la matrícula: {val_mat:,.0f}")
print(f"Valor del seguro: {val_seg:,.0f}")
print(f"Total: {val_mat + val_seg:,.0f}")