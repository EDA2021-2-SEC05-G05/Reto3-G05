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

import config as cf
import sys
import controller
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om


ufosfile = 'UFOS/UFOS-utf8-small.csv'
#cont = None

def printMenu():
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información")
    print("3- Total avistamientos en una ciudad")
    print("4- Total avistamientos por duracion")
    print("5- Total avistamientos por hora/minutos del dia")
    print("6- Total avistamientos en un rango de fechas")
    print("7- Total avistamientos de una zona geografica")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información....")
        controller.loadData(catalog, ufosfile)

    elif int(inputs[0]) == 3:
        print("\nContando cantidad total de avistamientos en una ciudad....")
        print('Número de elementos: ' + str(controller.ufosSize(catalog)))
        print('Altura del arbol: ' + str(controller.indexHeight(catalog)))
        #a = om.get(catalog["UFOS"], "lake wales")
        #print(me.getValue(a))
        #ciudad = input("Ingrese el nombre de la ciudad: ")
        #total = controller.
        #print("\nTotal de avistamientos de la ciudad: " + str(total))

    elif int(inputs[0]) == 4:
        print("\nContando avistamientos por duracion....")
        maximo = input("Limite inferior en segundos: ")
        minimo = input("Limite superior en segundos: ")
        #total = controller.
        #print("\nTotal de avistamientos segun su duracion: " + str(total))

    elif int(inputs[0]) == 5:
        print("\nContando avistamientos por hora/minutos del dia.... ")
        inferior = input("Limite inferior en formato (HH: MM): ")
        superior  = input("Limite superior en formato (HH: MM): ")
        #Total = controller.
        #print("\nTotal avistamientos por hora/minutos: " + str(Total))

    elif int(inputs[0]) == 6:
        print("\nContando avistamientos en un rango de fechas.... ")
        inferior = input("Limite inferior en formato (AAAA-MM-DD): ")
        superior  = input("Limite superior en formato (AAAA-MM-DD): ")
        #Total = controller.
        #print("\nTotal avistamientos por rango de fechas: " + str(Total))

    else:
        sys.exit(0)
sys.exit(0)
