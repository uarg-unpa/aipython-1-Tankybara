def factorial(num):
    for i in range(num-1,0,-1):
        num = num*i
    return num
n = int(input("Ingrese su numero: "))
print(factorial(n))