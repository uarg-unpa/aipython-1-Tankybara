edad = int(input("Ingrese edad: "))
monthIncome = int(input("Ingrese los ingresos mensuales"))
if edad > 18 and monthIncome >= 100000:
    print("Debe pagar impuestos.")
else:
    print("No debe pagar impuestos.")