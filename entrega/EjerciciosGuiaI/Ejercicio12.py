cantInvertir=int(input("Ingrese cantidad a invertir: "))
interes=float(input("Ingrese porcentaje de intereses: "))
interes=interes/100
anios=int(input("Ingrese cantidad de anios: "))
capital=cantInvertir+(cantInvertir*interes)
capital=capital*anios
print(f"La cantidad de capital total es {capital}")