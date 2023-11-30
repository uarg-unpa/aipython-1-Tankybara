def multiLista(lista):
    prod = 1
    for i in range(0,len(lista)):
        prod = prod*lista[i]
    return prod
lis = [1,3,5,7,9]
print(multiLista(lis))