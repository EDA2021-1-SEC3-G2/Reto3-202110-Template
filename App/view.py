"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import sys
import config as cf
import sys
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar característica en un rango")
    print("3- Buscar música para festejar")
    print("4- Buscar música para estudiar")
    print("5- Buscar elementos por género o crear género")


catalog = None


def iniciarCatalog():
    return controller.initCatalog()


def loadVideos(catalog):
    controller.loadVideos(catalog)


def reqcuatro(answer):
    for lista in lt.iterator(answer):
        print("Para el género "+str(lt.getElement(lista, 1))+" hay "+str(lt.getElement(lista, 2))+" reproducciones de "+str(lt.getElement(lista, 3))+" diferentes artistas.")
        for elemento in lt.iterator(lt.getElement(lista, 4)):
            print(elemento)
        print("")
        print("")

def thirdreq(answer):
    print("La cantidad de pistas únicas es "+str(lt.getElement(answer, 1)))
    for elemento in lt.iterator(lt.getElement(answer, 2)):
        print(elemento)
    print("")
    print("")

def secondreq(answer):
    print("La cantidad de pistas únicas es "+str(lt.getElement(answer, 1)))
    for elemento in lt.iterator(lt.getElement(answer, 2)):
        print(elemento)
    print("")
    print("")


def firstreq(answer, characteristic):
    print("De la característica "+characteristic+" hay "+str(answer[1])+" reproducciones de "+str(answer[0])+" diferentes artistas.")

def infoloadeddata(three, one, two, four, five):
    print("Se han cargado "+str(three)+" reproducciones con "+str(two)+" pistas unicas y "+str(one)+" artistas únicos.")
    for element in lt.iterator(four):
        print(element)
    print("")
    for element in lt.iterator(five):
        print(element)
    print("")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = iniciarCatalog()
        loadedvideos = controller.loadVideos(catalog)
        one = lt.size(mp.keySet(catalog["author"]))
        two = lt.size(mp.keySet(catalog["tracks"]))
        three = lt.size(catalog["list"])
        four = lt.subList(catalog["list"], 1, 5)
        five = lt.subList(catalog["list"], -5, -1)
        infoloadeddata(three, one, two, four, five)
    elif int(inputs[0]) == 2:
        characteristic = input("Ingrese la característica a evaluar: ")
        minval = float(input("ingrese el mínimo valor: "))
        maxval = float(input("Ingrese el maximo valor: "))
        answer = controller.firstreq(catalog, characteristic, minval, maxval)
        firstreq(answer[0], characteristic)
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    elif int(inputs[0]) == 3:
        val_1 = float(input("Ingrese el valor mínimo de energy: "))
        val_2 = float(input("Ingrese el valor máximo para energy: "))
        val_3 = float(input("Ingrese el valor minimo de danceability: "))
        val_4 = float(input("Ingrese el valor máximo para danceability: "))
        answer = controller.secondreq(catalog, val_1, val_2, val_3, val_4)
        secondreq(answer[0])
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    elif int(inputs[0]) == 4:
        val_1 = float(input("Ingrese el valor mínimo de instrumentalness: "))
        val_2 = float(input("Ingrese el valor máximo para instrumentalness: "))
        val_3 = float(input("Ingrese el valor minimo de tempo: "))
        val_4 = float(input("Ingrese el valor máximo para tempo: "))
        answer = controller.thirdreq(catalog, val_1, val_2, val_3, val_4)
        thirdreq(answer[0])
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    elif int(inputs[0]) == 5:
        info = input("¿Desea crear un nuevo género? (reponda si o no): ")
        if info == "si":
            name = input("Ingrese el nombre que quiere darle: ")
            mini = float(input("Ingrese el valor mímimo de tempo: "))
            maxi = float(input("Ingrese el valor máximo de tempo: "))
            controller.addfourthreq(catalog, name, mini, maxi)
            print("El elemento ha sido adicionado al catalogo.")
        elif info == "no":
            print("Entonces realice una busqueda de los generos ya existentes...")
            print("")
            information_list = input("Ingrese la lista de generos de los que desea saber separados por una coma (,): ")
            answer = controller.fourthreq(catalog, information_list)
            reqcuatro(answer[0])
        else:
            print("Eleccion inválida")
        print("Tiempo [ms]: ", f"{answer[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[2]:.3f}")
    elif int(input[0]) == 6:
        input("Ingrese la hora de incio: ")
        input("Ingrese la hora final: ")
        
    else:
        sys.exit(0)
sys.exit(0)
