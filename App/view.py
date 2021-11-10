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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
import time

ufosfile = 'UFOS/UFOS-utf8-large.csv'

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


def printResults (values, max):
    i = 1
    while i<=max:
        sig = lt.getElement(values, i)
        print("Fecha y hora: ", sig["datetime"], 
        " | Ciudad, País: ", sig["city"], ", ", sig["country"], 
        " | Duración (s): ", sig["duration (seconds)"], 
        " | Forma del objeto: ", sig["shape"], " | Longitud: ", 
        sig["longitude"], " | Latitud: ", sig["latitude"], "\n")
        i+=1
    print("- \n"*3)
    n = max-1
    while n >=0:
        sig = lt.getElement(values, lt.size(values)-n)
        print("Fecha y hora: ", sig["datetime"], 
        " | Ciudad, País: ", sig["city"], ", ", sig["country"], 
        " | Duración (s): ", sig["duration (seconds)"], 
        " | Forma del objeto: ", sig["shape"], " | Longitud: ", 
        sig["longitude"], " | Latitud: ", sig["latitude"], "\n")
        n-=1

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
        ciudad = input("Ingrese el nombre de la ciudad: \n")
        start_time = time.process_time()
        r = controller.getSbyCity(catalog, ciudad)
        values = om.valueSet(me.getValue(r))
        printResults(values, 3)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)
        print(elapsed_time_mseg)
    elif int(inputs[0]) == 4:
        dF = input("Limite inferior en segundos: ")
        d0 = input("Limite superior en segundos: ")
        start_time = time.process_time()
        rDurations = controller.getrankDurations(catalog, dF, d0)
        printResults(rDurations, 3)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
    elif int(inputs[0]) == 5:
        print("\nContando avistamientos por hora/minutos del dia.... ")
        inferior = input("Limite inferior en formato (HH: MM): ")
        superior  = input("Limite superior en formato (HH: MM): ")
        #Total = controller.
        #print("\nTotal avistamientos por hora/minutos: " + str(Total))

    elif int(inputs[0]) == 6:
        print("\nContando avistamientos en un rango de fechas.... ")
        d0 = input("Limite inferior en formato (AAAA-MM-DD): ")
        dF  = input("Limite superior en formato (AAAA-MM-DD): ")
        start_time = time.process_time()
        rDate = controller.getByDate(catalog, d0, dF)
        printResults(rDate, 3)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
    elif int(inputs[0]) == 7:
        print("Digite las longitudes y latitudes con dos cifras \n")
        lon0 = input("Ingrese la longitud mínima: ")
        lonF = input("Ingrese la longitud máxima: ")
        lat0 = input("Ingrese la latitud mínima: ")
        latF = input("Ingrese la latitud máxima: ")
        start_time = time.process_time()
        rCoord = controller.getByCoord(catalog, float(lon0), float(lonF), float(lat0), float(latF))
        SortrCoord = controller.getSortCoord(rCoord)
        printResults(SortrCoord, 5)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
    else:
        sys.exit(0)
sys.exit(0)
