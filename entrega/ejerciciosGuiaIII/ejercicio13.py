n = int(input("Ingrese un numero natural: "))
if n < 0:
    print("Error. Debe ingresar un numero natural: ")
else:
    for i in range(0,n+1):
        if(i%2 == 0):
            print(i)