"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf


def newAnalyzer():
    analyzer = {'UFOS': None
                }

    analyzer['UFOS'] = om.newMap(omaptype="RBT")
  
    return analyzer


def addUFOS(analyzer, ufos):
    exist = om.contains (analyzer["UFOS"], ufos["city"])
    if exist:
        x = om.get(analyzer["UFOS"], ufos["city"])
        value = me.getValue(x)
        lt.addLast(value, ufos)
    else:
        list = lt.newList()
        lt.addLast(list, ufos)
        om.put(analyzer["UFOS"], ufos["city"], list)
    return analyzer

def ufosSize(analyzer):
    return om.size(analyzer['UFOS'])


def indexHeight(analyzer):
    return om.height(analyzer['UFOS'])











