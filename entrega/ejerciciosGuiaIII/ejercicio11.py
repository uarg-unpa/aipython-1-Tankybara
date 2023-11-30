num = int(input("Ingrese un numero: "))
for i in range(1,num+1):
    if i%2 != 0:
        for j in range(i,0,-1):
            if j%2 != 0:
                print(j,end=" ")
        print("")
# Consultar con el profe la resolucion del ejercicio