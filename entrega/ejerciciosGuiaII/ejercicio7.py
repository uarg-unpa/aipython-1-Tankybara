nota1 = int(input("Ingrese nota: "))
if nota1 < 0:
    print("ERROR. La nota debe ir de 0 a 100")
else:
    if nota1 in range(0,50):
        print("F")
    elif nota1 in range(50,60):
        print("D")
    elif nota1 in range(60,70):
        print("C")
    elif nota1 in range(70,90):
        print("B")
    else:
        print("A")