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
from DISClib.Algorithms.Sorting import mergesort as mr
assert cf


def newAnalyzer():
    catalog = {'UFOS': None,
                "cities":None,
                "durations": None
                }

    #analyzer['UFOS'] = om.newMap(omaptype="RBT")
    catalog['cities'] = mp.newMap(1000, 
                                    maptype="CHAINING", 
                                    loadfactor=4.0)
    catalog['durations'] = om.newMap(omaptype="RBT")
    catalog["datetimes"] = om.newMap(omaptype="RBT")  
    catalog["coords"] = om.newMap(omaptype="RBT")                            
  
    return catalog


def addUFOS(catalog, ufos):
    addCities(catalog, ufos)
    addDurationB(catalog, ufos)
    addDate(catalog, ufos)
    addCoord(catalog, ufos)

def addCities(catalog, ufos):
    exist = mp.contains (catalog["cities"], ufos["city"])
    if exist:
        x = mp.get(catalog["cities"], ufos["city"])
        value = me.getValue(x)
        om.put(value, ufos["datetime"], ufos)
    else:
        arb = om.newMap(omaptype="RBT")
        om.put(arb, ufos["datetime"], ufos)
        mp.put(catalog["cities"], ufos["city"], arb)
    return catalog


def addDuration(catalog, ufos):
    exist = om.contains(catalog["durations"], float(ufos["duration (seconds)"]))
    if exist:
        x = om.get(catalog["durations"], float(ufos["duration (seconds)"]))
        value = me.getValue(x)
        lt.addLast(value, ufos)
    else:
        list = lt.newList()
        lt.addLast(list, ufos)
        om.put(catalog["durations"], float(ufos["duration (seconds)"]), list)
    return catalog

def addDurationB(catalog, ufos):
    cc = ufos["city"], "-", ufos["country"]
    exist = om.contains(catalog["durations"], float(ufos["duration (seconds)"]))
    if exist:
        x = om.get(catalog["durations"], float(ufos["duration (seconds)"]))
        value = me.getValue(x)
        if om.contains(value, cc):
            y = om.get(value, cc)
            ccvalue = me.getValue(y)
            lt.addLast(ccvalue, ufos)
        else:
            cclist = lt.newList()
            lt.addLast(cclist, ufos)
            om.put(value, cc, cclist)
    else:
        arb = om.newMap(omaptype="RBT")
        list = lt.newList()
        lt.addLast(list, ufos)
        om.put(arb, cc, list)
        om.put(catalog["durations"], float(ufos["duration (seconds)"]), arb)
    return catalog

def addDate(catalog, ufos):
    exist = om.contains(catalog["datetimes"], ufos["datetime"][:10])
    if exist:
        x = om.get(catalog["datetimes"], ufos["datetime"][:10])
        value = me.getValue(x)
        om.put(value, ufos["datetime"], ufos)
    else:
        arb = om.newMap(omaptype="RBT")
        om.put(arb, ufos["datetime"], ufos)
        om.put(catalog["datetimes"], ufos["datetime"][:10], arb)
    return catalog

def addCoord(catalog, ufos):
    exist = om.contains(catalog["coords"], round(float(ufos["longitude"]), 2))
    if exist:
        x = om.get(catalog["coords"], round(float(ufos["longitude"]), 2))
        value = me.getValue(x)
        if om.contains(value, round(float(ufos["latitude"]), 2)):
            y = om.get(value, round(float(ufos["latitude"]), 2))
            latvalue = me.getValue(y)
            lt.addLast(latvalue, ufos)
        else:
            latlist = lt.newList()
            lt.addLast(latlist, ufos)
            om.put(value, round(float(ufos["latitude"]), 2), latlist)
    else:
        arb = om.newMap(omaptype="RBT")
        list = lt.newList()
        lt.addLast(list, ufos)
        om.put(arb, round(float(ufos["latitude"]), 2), list)
        om.put(catalog["coords"], round(float(ufos["longitude"]), 2), arb)
    return catalog

def ByDate(catalog, d0, dF):
    dt = catalog["datetimes"]
    keys = om.keys(dt, d0, dF)
    list = lt.newList()
    for key in lt.iterator(keys):
        x = om.get(dt, key)
        value = me.getValue(x)
        values = om.valueSet(value)
        for sight in lt.iterator(values):
            lt.addLast(list, sight)
    return list


def ByCoord(catalog, lon0, lonF, lat0, latF):
    cs = catalog["coords"]
    if lonF < lon0:
        Lkeys = om.keys(cs, lonF, lon0)
    else:
        Lkeys = om.keys(cs, lon0, lonF)
    list = lt.newList()
    for key in lt.iterator(Lkeys):
        x = om.get(cs, key)
        value = me.getValue(x)
        Akeys = om.keys(value, lat0, latF)
        for xkey in lt.iterator(Akeys):
            y = om.get(value, xkey)
            yvalues = me.getValue(y)
            for yvalue in lt.iterator(yvalues):
                lt.addLast(list, yvalue)
    return list

def rankDurations(catalog, d0, dF):
    ds = catalog["durations"]
    keys = om.keys(ds, float(d0), float(dF))
    list = lt.newList()
    for key in lt.iterator(keys):
        x = om.get(ds, key)
        value = me.getValue(x)
        if key == lt.getElement(keys, 1) or key == lt.getElement(keys, lt.size(keys)):
            value = mr.sort(value, cmpCityCountry)
        for sight in lt.iterator(value):
            lt.addLast(list, sight)
    return list

def rankDurationsB(catalog, d0, dF):
    ds = catalog["durations"]
    keys = om.keys(ds, float(d0), float(dF))
    list = lt.newList()
    for key in lt.iterator(keys):
        x = om.get(ds, key)
        value = me.getValue(x)
        Akeys = om.keySet(value)
        for xkey in lt.iterator(Akeys):
            y = om.get(value, xkey)
            yvalues = me.getValue(y)
            for yvalue in lt.iterator(yvalues):
                lt.addLast(list, yvalue)
    return list
    
def SbyCity(catalog, ciudad):
    return mp.get(catalog["cities"], ciudad)

def ufosSize(catalog):
    return om.size(catalog['UFOS'])


def indexHeight(catalog):
    return om.height(catalog['UFOS'])


def cmpCityCountry (s1, s2):
    s1cc = s1["city"], "-", s1["country"]
    s2cc = s2["city"], "-", s2["country"]
    return s1cc<s2cc

def sortCoord(list):
    return mr.sort(list, cmpLatitude)

def cmpLatitude(l1, l2):
    return l1["latitude"]<l2["latitude"]







