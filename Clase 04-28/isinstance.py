# Definimos la función llamada verificar_tipo
# Recibe un parámetro llamado "valor"
# Puede ser int (entero), str (texto) o float (decimal)
# -> str indica que la función devolverá un texto
def verificar_tipo(valor: int | str | float) -> str:
    
    # Verificamos si el valor es de tipo booleano (True o False)
    # Se evalúa primero porque bool hereda de int en Python
    # SIEMPRE debes poner bool antes que int
    # Si no lo haces, True se detectará como entero
    if isinstance(valor, bool):
        return "Es un booleano"
    
    # Verificamos si el valor es de tipo entero
    elif isinstance(valor, int):
        return "Es un número entero"
    
    # Verificamos si el valor es de tipo cadena de texto
    elif isinstance(valor, str):
        return "Es una cadena de texto"
    
    # Verificamos si el valor es de tipo decimal (float)
    elif isinstance(valor, float):
        return "Es un número decimal"
    
    # Si no es ninguno de los tipos anteriores
    else:
        return "Es un tipo de dato no reconocido"


# -------------------------
# PRUEBAS DEL PROGRAMA
# -------------------------

# Llamamos a la función con un número entero
print(verificar_tipo(10))      
# Resultado: "Es un número entero"

# Llamamos a la función con un texto
print(verificar_tipo("hola"))  
# Resultado: "Es una cadena de texto"

# Llamamos a la función con un número decimal
print(verificar_tipo(3.14))    
# Resultado: "Es un número decimal"

# Llamamos a la función con un valor booleano
print(verificar_tipo(True))    
# Resultado: "Es un booleano"