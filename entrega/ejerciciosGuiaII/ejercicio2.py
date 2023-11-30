miEdad = int(input("Ingresar mi edad: "))
suEdad = int(input("Ingresar su edad: "))
if miEdad == suEdad:
    print("Empate en el Maracaná. La Libertadores se define por penales.")
else:
    if miEdad > suEdad:   
        print("Yo soy mayor.")
        if miEdad-suEdad == 1:
            print("Por un año")
        elif miEdad-suEdad > 1:
            print("Por años.")
    else:
        print("Usted es mayor.")
        if suEdad-miEdad == 1:
            print("Por un año")
        elif suEdad-miEdad > 1:
            print("Por años.")

        