edad = int(input("Ingrese edad: "))
if edad < 4:
    print("Entra gratis")
elif edad in range(4,18+1):
    print("Debe pagar $5")
else:
    print("Debe pagar $10")