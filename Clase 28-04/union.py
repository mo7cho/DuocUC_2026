# Definimos la función
# El parámetro puede ser int, str o float
# La función devuelve un string
def verificar_tipo(valor: int | str | float) -> str:
    
    # Usamos match, pero ahora con "patrones de tipo"
    match valor:

        # Si el valor es de tipo verdadero o falso (bool)
        case bool():
            return "Es un booleano"
        
        # Si el valor es de tipo entero (int)
        case int():
            return "Es un número entero"
        
        # Si el valor es de tipo texto (str)
        case str():
            return "Es una cadena de texto"
        
        # Si el valor es de tipo decimal (float)
        case float():
            return "Es un número decimal"
        
        # Caso por defecto si no es ninguno de los anteriores
        case _:
            return "Es un tipo de dato no reconocido"


# Probamos la función con distintos valores
print(verificar_tipo(10))      # entero
print(verificar_tipo("hola"))  # texto
print(verificar_tipo(3.14))    # decimal
print(verificar_tipo(True))    # booleano (caso interesante)