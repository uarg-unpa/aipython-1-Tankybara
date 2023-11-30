num = int(input("Ingrese un numero: "))
if num <= 3:
    print("ERROR. Debe ingresar un numero mayor a 3.")
else:
    for i in range(1,num):
        if(i%2 != 0):
            print(i)