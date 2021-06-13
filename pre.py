print("Verificador de precios\n")

art = input("introduce el nombre del articulo para saber el precio\ny 's' para sumar el total: ")
art = art.lower()

gel = 35.50
hilo = 91.00
pilas = 25.00
shampo = 55.00
coto = 32.00
des = 36.50
toa = 37.50
cep = 55.00
aero = 38.00

total = 0
while art != "s":

    if art == "gel" or art == "gel de afeitar":
        total += gel
        print("Gel de afeitar",gel)
    elif art == "hilo":
        total += hilo
        print("Hilo dental",hilo)
    elif art == "pilas":
        total += pilas
        print("Pilas",pilas)
    elif art == "shampo" or art == "sham":
        total += shampo
        print("Shampo",shampo)
    elif art == "cotonetes" or art == "coto":
        total += coto
        print("Cotonetes",coto)
    elif art == "desodorante" or art == "des":
        total += des
        print("Desodorante",des)
    elif art == "toa" or art == "toallitas" or art == "Toallas":
        total += toa
        print("Toallitas",toa)
    elif art == "cep" or art == "cepillo" or art == "cepillo dental":
        total += cep
        print("Cepillo dental",cep)
    elif art == "aero" or art == "aerosol" or art == "aerosol para pies":
        total += cep
        print("Aerosol para pies",aero)

    art = input("Sigue agregando articulo o 's' para sumar todo: ")

print("\nTotal de compra",round(total,2))