def listprom(vec):
    suma = 0
    prom = 0
    for i in range(0,len(vec)):
        suma = suma + vec[i]
    prom = suma/len(vec)
    return prom
lis = [1,3,5,7,9]
print(f"El promedio de la lista es {listprom(lis)}")