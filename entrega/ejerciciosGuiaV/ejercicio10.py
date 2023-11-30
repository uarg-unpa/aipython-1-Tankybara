def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio = inicio + 1
        fin = fin - 1
    return False
pal = str(input("Ingrese una palabra: "))
if palindromo(pal):
    print("Es palindromo")
else:
    print("No es palindromo")