# Función para intentar convertir el texto a su tipo real
def convertir_valor(texto):
    
    # Convertimos el texto a minúsculas
    # Esto ayuda a reconocer "TRUE", "True", "true" como lo mismo
    texto = texto.lower()
    
    # -------------------------
    # DETECCIÓN DE BOOLEANOS
    # -------------------------
    
    # Si el texto es "true", devolvemos el valor booleano True
    if texto == "true":
        return True
    
    # Si el texto es "false", devolvemos False
    elif texto == "false":
        return False
    
    # -------------------------
    # INTENTAR CONVERTIR A ENTERO
    # -------------------------
    
    # Intentamos convertir el texto a número entero
    try:
        return int(texto)
    
    # Si falla (por ejemplo, "hola"), no hace nada y sigue
    except:
        pass
    
    # -------------------------
    # INTENTAR CONVERTIR A DECIMAL
    # -------------------------
    
    # Intentamos convertir el texto a número decimal (float)
    try:
        return float(texto)
    
    # Si falla, continúa
    except:
        pass
    
    # -------------------------
    # SI NO ES NADA DE LO ANTERIOR
    # -------------------------
    
    # Se devuelve como texto (string)
    return texto


# -----------------------------------
# FUNCIÓN PARA DETECTAR EL TIPO
# -----------------------------------

def verificar_tipo(valor: int | str | float | bool) -> str:
    
    # Usamos match para identificar el tipo de dato
    match valor:

        # Si es booleano
        case bool():
            return "Es un booleano"
        
        # Si es entero
        case int():
            return "Es un número entero"
        
        # Si es texto
        case str():
            return "Es una cadena de texto"
        
        # Si es decimal
        case float():
            return "Es un número decimal"
        
        # Si no coincide con nada
        case _:
            return "Es un tipo de dato no reconocido"


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

# Pedimos un dato al usuario (siempre será texto)
entrada = input("Ingresa un valor: ")

# Convertimos ese texto al tipo más adecuado
valor_convertido = convertir_valor(entrada)

# Detectamos qué tipo de dato es
resultado = verificar_tipo(valor_convertido)

# Mostramos el resultado en pantalla
print("Resultado:", resultado)