a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
if a < b:
    i=a
    for i in range(a,b,1):
        print(i)
else:
    i=b
    for i in range(b,a,1):
        print(i)