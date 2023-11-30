def cel2far(celsius):
    fahren = (celsius*(9/5))+32
    return fahren
cel = float(input("Ingrese cantidad de grados Celsius: "))
print(f"{cel}°C son {cel2far(cel)}°F")