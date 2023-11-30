def cantVoc(cadena):
    cant = 0
    for i in range(0,len(cadena)):
        if 'A' in cadena or 'a' in cadena:
            cant += 1
        elif 'E' in cadena or 'e' in cadena:
            cant += 1
        elif 'I' in cadena or 'i' in cadena:
            cant += 1
        elif 'O' in cadena or 'o' in cadena:
            cant += 1
        elif 'U' in cadena or 'u' in cadena:
            cant += 1
    return cant
pal = str(input("Ingrese una palabra: "))
print(f"La cantidad de vocales en '{pal}' es {cantVoc(pal)}")