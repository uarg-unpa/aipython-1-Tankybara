def maximo(x,y,z):
    mayor=x
    if y > mayor and y > z:
        return f"El mayor es {y}"
    elif z > mayor and z > y:
        return f"El mayor es {z}"
    else:
        return f"El mayor es {mayor}"

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese un ultimo numero: "))
print(f"{maximo(num1,num2,num3)}")