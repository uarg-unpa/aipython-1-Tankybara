n = int(input("Ingrese un numero: "))
for i in range(2,n):
    if n%i == 0:
        print("No es primo.", n, "es divisor")
        break
    elif i == n-1:
        print("Es primo.")