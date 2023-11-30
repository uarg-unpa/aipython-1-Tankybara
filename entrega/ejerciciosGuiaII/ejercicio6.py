a=int(input("Ingrese un numero del 1 al 7: "))
if a < 1 or a > 7:
    print("Error. Debe ingresar un numero del 1 a 7")
else:
    if a == 1:
        print("Lunes")
    elif a == 2:
        print("Martes")
    elif a == 3:
        print("Miercoles")
    elif a == 4:
        print("Jueves")
    elif a == 5:
        print("Viernes")
    elif a == 6:
        print("Sabado")
    elif a == 7:
        print("Domingo")