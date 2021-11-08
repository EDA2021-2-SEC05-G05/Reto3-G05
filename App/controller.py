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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def init():
    analyzer = model.newAnalyzer()
    return analyzer

ufosfile= 'UFOS/UFOS-utf8-small.csv'
def loadData(analyzer, ufosfile):
    ufosfile = cf.data_dir + ufosfile
    input_file = csv.DictReader(open(ufosfile, encoding="utf-8"),
                                delimiter=",")
    for ufos in input_file:
        model.addUFOS(analyzer, ufos)
    return analyzer

def getrankDurations(catalog, dF, d0):
    return model.rankDurations(catalog, dF, d0)

def getSbyCity(catalog, ciudad):
    return model.SbyCity(catalog, ciudad)

def getByDate(catalog, d0, dF):
    return model.ByDate(catalog, d0, dF)

def getByCoord(catalog, lon0, lonF, lat0, latF):
    return model.ByCoord(catalog, lon0, lonF, lat0, latF)

def ufosSize(catalog):
    return model.ufosSize(catalog)


def indexHeight(catalog):
    return model.indexHeight(catalog)







