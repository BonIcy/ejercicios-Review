""" 2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

def operacion ():
    print("Por favor Ingresa los siguientes datos: ")
    atleta1 = input("Ingresa el nombre del participante 1 ")
    marca1 = float(input("Ingresa la marca del participante 1 "))
    atleta2 = input("Ingresa el nombre del participante 2 ")
    marca2 = float(input("Ingresa la marca del participante 2 "))
    atleta3 = input("Ingresa el nombre del participante 3 ")
    marca3 = float(input("Ingresa la marca del participante 3 "))
    
    if marca3 > marca2 and marca3 > marca1:
        print("----------Premios-----------")
        print(f"\t Felicidades {atleta3} has ganado la medalla de oro")
        if marca3 > 15.50:
            print(" \t Feliciades, acabas de romper el record, por lo que tu pago por esta hazaña será de 500 millones")
            
    if marca2 > marca3 and marca2 > marca1:
        print("----------Premios-----------")
        print(f"\t Felicidades {atleta2} has ganado la medalla de oro")
        if marca2 > 15.50:
            print(" \t Feliciades, acabas de romper el record, por lo que tu pago por esta hazaña será de 500 millones")
            
    if marca1 > marca2 and marca1 > marca3:
        print("----------Premios-----------")
        print(f"\t Felicidades {atleta1} has ganado la medalla de oro")
        if marca1 > 15.50:
            print(" \t Feliciades, acabas de romper el record, por lo que tu pago por esta hazaña será de 500 millones")
    return()

operacion()