# Definimos una función llamada verificar_tipo
# Recibe un parámetro llamado "valor"
# -> str indica que la función devolverá un texto (string)
def verificar_tipo(valor) -> str:
    
    # Usamos "match", que funciona como un switch (compara valores)
    match valor:
        
        # Si el valor es exactamente 1
        case 1:
            return "Es un número entero"  # Devuelve este mensaje
        
        # Si el valor es exactamente el texto "texto"
        case "texto":
            return "Es una cadena de texto"  # Devuelve este mensaje
        
        # Si el valor es exactamente 3.14
        case 3.14:
            return "Es un número decimal"  # Devuelve este mensaje
        
        # Caso por defecto (si no coincide con ninguno anterior)
        case _:
            return "Es un tipo de dato no reconocido"


# Llamamos a la función y le pasamos el valor 1
resultado = verificar_tipo(1)

# Imprimimos el resultado en pantalla
print(resultado)