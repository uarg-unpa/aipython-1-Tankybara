meinText = str(input("Ingrese su texto: "))
print("Texto es: ",meinText)
meinText = meinText.upper()
print("Texto en mayúscula es: ",meinText)
meinText = meinText.lower()
print("Texto en minúscula es: ",meinText)
meinText = meinText.title()
print("Texto en título es: ",meinText)
#Comparaciones
print("-----Comparaciones-----")

numero1 = int(input("Ingrese un numero: "))
numero2 = input("Ingrese otro numero: ")
numero2 = int(numero2)
if numero1 > numero2:
    mayor = numero1
else:
    mayor = numero2
print(mayor)