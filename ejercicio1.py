""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control:
    print ("----------------------MENU----------------------")
    print ("1.  CREAR GRUPO ARTEMIS:")
    print ("1.1 LISTA CAMPERS ARTEMIS")
    print ("1.2 AGREGAR CAMPERS A ARTEMOS")
    print ("1.3 ELIMINAR CAMPERS DE ARTEMIS")
    print ("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
    print ("1.5 BUSCAR CAMPER EN LISTA ARTEMIS")
    print ("2.  CREAR GRUPO SPUTNIK")
    print ("2.1 LISTA CAMPERS DE SPUTNIK")
    print ("2.2 AGREGAR CAMPERS A SPUTNIK")
    print ("2.3 ELIMINAR CAMPERS DE SPUTNIK")
    print ("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
    print ("2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")
    opcion = input("Digite opcion:")
    if opcion == "1":
        print("Modificador de participantes campers del grupo Artemis")
        opc = input("Inserta el numero de lo que quieres hacer con el grupo Artemis:")
        if opc == "1.1":
            print("")
    elif opcion =="2":
        print("Modificador de participantes campers del grupo Sputnik")
        opcion = "Sputnik"
    else:
        print("Digita una opcion valida") """

listaArtemis = []
listaSputnik = []


def crearListaArtemis ():   
    print("\n Creador de lista de estudiantes Artemis. Para dejar de ingresar nombres escriba:  exit ")
    i = 1
    while i != 0:
        estudiante = input("Ingrese el nombre del estudiante que desea agregar a la lista de Artemis: ")
        listaArtemis.append(estudiante)   
        if estudiante == "exit":
            i = 0
            listaSputnik.remove("exit")
            print(f"\n{listaArtemis}")
def listadoArtemis():
    print(f"\n Listado de estudiantes en el grupo Artemis: ")
    for x in listaArtemis:
        print(x)
def agregarArtemis ():
    respuesta=input(f"\n T¿e gustaria seguir añadiendo estudiantes a la lista de Artemis?: ( si / no ): ")
    while respuesta == "si":
        estudiante = input(f"\n ingrese el nombre del estudiante: ")
        listaArtemis.append(estudiante)
        respuesta=input(f"\n ¿Te gustaria seguir añadiendo estudiantes a la lista de Artemis?: ( si / no ): ")
        print(f"Nueva lista: \n {listaArtemis}")
def eliminarArtemis():
    print(listaArtemis)
    eliminacion = input(f"\n ¿Qué camper deseas eliminar de Artemis?: ")
    listaArtemis.remove(eliminacion)
    print(f"Nueva lista: \n {listaArtemis}")
def ordenarArtemis():
    listaArtemis.sort()
    print(f"\n La lista de estudiantes en el grupo Artemis ordenada alfabeticamente : \n {listaArtemis}")
def buscarArtemis ():
    print(listaArtemis)
    estudiante= input(f"\n ingrese el nombre estudiante del cuál desea hacer la búsqueda: ")
    posicion= listaArtemis.index(estudiante)
    print(f"El estudiante {estudiante} está en la posición {1+posicion} en la lista del grupo Artemis.")



def crearListaSputnik ():   
    print("\n Creador de lista de estudiantes Sputnik. Para dejar de ingresar nombres escriba: exit")
    i = 1
    while i != 0:
        estudiante = input("Ingrese el nombre del estudiante que desea agregar a la lista de Sputnik: ")
        listaSputnik.append(estudiante)  
        if estudiante == "exit":
            i = 0
            listaSputnik.remove("exit")
            print(f"\n{listaSputnik}")
def listadoSputnik():
    print(f"\n Listado de estudiantes en el grupo Sputnik: ")
    for x in listaSputnik:
        print(x)
def agregarSputnik ():
    respuesta=input(f"\n ¿Te gustaria seguir añadiendo estudiantes a la lista de Sputnik?: ( si / no ): ")
    while respuesta == "si":
        
        estudiante = input(f"ingrese el nombre del estudiante: ")
        listaSputnik.append(estudiante)
        respuesta=input(f"\n ¿Te gustaria seguir añadiendo estudiantes a la lista de Sputnik?: ( si / no ): ")
        print(f"Nueva lista: \n {listaSputnik}")
def eliminarSputnik():
    print(listaSputnik)
    eliminacion = input(f"\n Qué camper deseas eliminar de Sputnik?: ")
    listaSputnik.remove(eliminacion)
    print(f"Nueva lista: \n {listaSputnik}")
def ordenarSputnik():
    listaSputnik.sort()
    print(f"\n La lista de estudiantes en el grupo Sputnik ordenada alfabeticamente : \n {listaSputnik}")
def buscarSputnik ():
    print(listaSputnik)
    estudiante= input(f"\n ingrese el nombre estudiante del cuál desea hacer la búsqueda: ")
    posicion= listaSputnik.index(estudiante)
    print(f"El estudiante {estudiante} está en la posición {1+posicion} en la lista del grupo Sputnik.")

print(f"-------------------------MENU--------------------------------\n 1.  CREAR GRUPO ARTEMIS: \n 1.1 LISTAR CAMPERS DE ARTEMIS \n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERS DE ARTEMIS \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPEREN LISTA DE ARTEMIS \n 2.  CREAR GRUPO SPUTNIK: \n 2.1 LISTAR CAMPERS DE SPUTNIK \n 2.2 AGREGAR CAMPERS A SPUTNIK \n 2.3 ELIMINAR CAMPERS DE SPUTNIK \n 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK \n 2.5 BUSCAR CAMPEREN LISTA DE SPUTNIK")



respuesta = 5
while respuesta != 3:
    respuesta = float(input(f"Digite opción: "))

    if respuesta == 1.0:
        crearListaArtemis ()

    elif respuesta == 1.1:
        listadoArtemis()

    elif respuesta == 1.2:
        agregarArtemis()

    elif respuesta == 1.3:
        eliminarArtemis()

    elif respuesta == 1.4:
        ordenarArtemis()

    elif respuesta == 1.5:
        buscarArtemis()

    elif respuesta == 2.0:
        crearListaSputnik ()
        
    elif respuesta == 2.1:
        listadoSputnik()

    elif respuesta == 2.2:
        agregarSputnik()

    elif respuesta == 2.3:
        eliminarSputnik()

    elif respuesta == 2.4:
        ordenarSputnik()

    elif respuesta == 2.5:
        buscarSputnik()

    elif respuesta != 3:
        print("Digita alguna opcion que sea válida")

