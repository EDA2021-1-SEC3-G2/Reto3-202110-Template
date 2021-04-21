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
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def initCatalog():

    catalog = {'context': None, "list": None}
    catalog["list"] = lt.newList("SINGLE_LINKED")
    catalog['context'] = mp.newMap(13, maptype="PROBING", loadfactor=0.5)
    mp.put(catalog["context"], "instrumentalness", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "liveness", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "speechiness", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "danceability", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "valence", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "loudness", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "tempo", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "acousticness", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "energy", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "mode", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    mp.put(catalog["context"], "key", om.newMap(omaptype="RBT", comparefunction=cmpValue))
    return catalog
# Funciones para agregar informacion al catalogo
def addplaylist(catalog, reproduccion):
    print(reproduccion)
    # print(catalog)
    lt.addLast(catalog["list"], reproduccion)
    return catalog
    # caracteristics = mp.keySet(catalog["context"])
    # for element in lt.iterator(caracteristics):
        
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpValue(value1, value2):
    """
    Compara dos fechas
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
