#contpar=0
#contimpar=0
#for _ in range(20):
#    num=int(input("Ingrese num: "))
#   if num%2==0:
#        contpar=contpar+1
#    else:
#        contimpar=contimpar+1
#print(f"Cantidad de numeros pares: {contpar}")
#print(f"Cantidad de numeros impares: {contimpar}")

#num1=int(input("Ingrese num1: "))
#num2=int(input("Ingrese num2: "))
#num3=int(input("Ingrese num3: "))
#producto = num1*num2*num3
#sumatoria= num1+num2+num3
#print(f"La suma es {sumatoria}, y el producto es {producto}")

#Con iteracion While
#num=int(input("Ingrese un numero: "))
#cont=1
#suma=0
#prod=1
#while cont<=3:
#    suma=suma+num
#    prod=prod*num
#    num=int(input("Ingrese otro numero: "))
#    cont=cont+1
#print(f"La suma es {suma}, y el producto es {prod}")

#Con iteracion For
#suma=0
#prod=1
#for _ in range(3):
#    num=int(input("Ingrese otro numero: "))
#    suma=suma+num
#    prod=prod*num
#print(f"La suma es {suma}, y el producto es {prod}")

#Numero menor con iteracion For
#menor=int(input("Ingrese un numero: "))
#for _ in range(4):
#    num=int(input("Ingrese un numero: "))
#    if num < menor:
#        menor = num
#print(f"El menor de cinco numeros es {menor}")

#Numero menor con iteracion While
menor=int(input("Ingrese un numero: "))
cont=1
while cont<=4:
    num=int(input("Ingrese un numero: "))
    if num < menor:
        menor = num
    cont=cont+1
print(f"El menor de todos los numeros es {menor}")