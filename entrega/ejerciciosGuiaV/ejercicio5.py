def parImpar(num):
    if(num%2 == 0):
        return "Es par"
    else:
        return "No es par"
n = int(input("Ingrese su numero: "))
print(parImpar(n))