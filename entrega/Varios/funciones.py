#def saludo():
#    print("Funcion en AIPython")

#def multiTable(x):
#    i=1
#    for i in range(i,11):
#        print(f"{x}x{i} = {x*i}")

#num=int(input("Ingrese un numero: "))
#print(f"{multiTable(num)}")

#def parImpar(x):
#    if x%2 != 0:
#        return "Es impar"
#    else:
#        return "Es par"
#
#num=int(input("Ingrese un numero: "))
#print(f"{parImpar(num)}")

#def mayorDeTres(x,y,z):
#    mayor=x
#    if y > mayor and y > z:
#        return f"El mayor es {y}"
#    elif z > mayor and z > y:
#        return f"El mayor es {z}"
#    else:
#        return f"El mayor es {mayor}"

#num1=int(input("Ingrese un numero: "))
#num2=int(input("Ingrese otro numero: "))
#num3=int(input("Ingrese un ultimo numero: "))
#print(f"{mayorDeTres(num1,num2,num3)}")

#def sumaLista(v):
#    suma=0
#    for i in range(len(v)):
#        suma=suma+v[i]
#    return suma
#lista=[1,2,3,4,5,6,7,8,9,10]
#print(f"{sumaLista(lista)}")

def buscarSimbolo(simbolo, palabra):
    for letra in palabra:
        if letra == simbolo:
            return True
    return False

def invertirPalabra(palabra):
    return palabra[::-1]

def main():
    word = str(input("Ingrese su palabra: "))
    symbol = input("Ingrese su simbolo a buscar en la palabra: ")
    auten = buscarSimbolo(symbol, word)
    if auten:
        print("Se ha encontrado el simbolo.")
    else:
        print("No se encontro el simbolo. ")
    print(invertirPalabra(word))
main()