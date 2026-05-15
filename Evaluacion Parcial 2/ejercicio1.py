med = 60000
dpo = 8000

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo: ")

if edad <= 30:
    if tramo == "A" or tramo == "B":
        dcto_med = 0.18
    elif tramo == "C" or tramo == "D":
        dcto_med = 0.12

elif 31 <= edad <= 60:
    if tramo == "A" or tramo == "B":
        dcto_med = 0.12
    elif tramo == "C" or tramo == "D":
        dcto_med = 0.8
elif edad > 60:
    dcto_med = 0.00

val_med = med * (1 - dcto_med)

if tramo == "A" or tramo == "B":
    dcto_dpo = 0.10
    if edad >= 55:
        dcto_dpo = 0.15
else:
    dcto_dpo = 0.00

val_dpo = dpo * (1 - dcto_dpo)

print(f"El valor de su medicamento es: {round(val_med, 0)}")
print(f"El valor del despacho es: {round(val_dpo, 0)}")