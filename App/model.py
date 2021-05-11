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
import random
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def init_Catalog():
    catalog = {'context': None, "list": None, "author": None}
    catalog["list"] = lt.newList("SINGLE_LINKED")
    catalog['context'] = mp.newMap(13, maptype="PROBING", loadfactor=0.5)
    catalog["author"] = mp.newMap(10000, maptype="CHAINING", loadfactor=5.0, comparefunction=compareArtistsByNameMap)
    catalog["tracks"] =  mp.newMap(10000, maptype="CHAINING", loadfactor=5.0, comparefunction=compareTracksByNameMap)
    catalog["genres"] = mp.newMap(11, maptype="PROBING", loadfactor=0.5)
    # comparando los repetidos...
    # catalog["auxiliar_list"] = lt.newList("SINGLE_LINKED", cmpfunction=cmpunique_id)
    # catalog["final_work_list"] = lt.newList("SINGLE_LINKED")
    mp.put(catalog["context"], "instrumentalness", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "liveness", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "speechiness", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "danceability", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "valence", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "loudness", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "tempo", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "acousticness", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "energy", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "mode", om.newMap(omaptype="RBT"))
    mp.put(catalog["context"], "key", om.newMap(omaptype="RBT"))
    return catalog


# intento de comparar por los parametros de user, artis, created y track 
"""def separate_event(catalog, reproduccion):
    unique_id = str(reproduccion["user_id"])+str(reproduccion["artist_id"])+str(reproduccion["created_at"])+str(reproduccion["track_id"])
    if lt.isPresent(catalog["auxiliar_list"], unique_id) == 0:
        lt.addLast(catalog["auxiliar_list"], unique_id)
        lt.addLast(catalog["final_work_list"], reproduccion)"""

# Funciones para agregar informacion al catalogo
def addplaylist(catalog, reproduccion):
    big_map = catalog["context"]
    lt.addLast(catalog["list"], reproduccion)
    characteristics = mp.keySet(catalog["context"])
    authors = unique_authors(catalog, reproduccion)
    for element in lt.iterator(characteristics):
        almost = mp.get(big_map, element)
        answer = me.getValue(almost)
        key = float(reproduccion[element])
        if om.contains(answer, key):
            addtolist = om.get(answer, key)
            listadd = me.getValue(addtolist)
            lt.addLast(listadd, reproduccion)
        else:
            value = lt.newList("SINGLE_LINKED")
            lt.addLast(value, reproduccion)
            om.put(answer, key, value)
    return catalog


def unique_authors(catalog, reproduccion):    
    if mp.contains(catalog["author"], reproduccion["artist_id"]) is False:
        mp.put(catalog["author"], reproduccion["artist_id"], reproduccion)
    if mp.contains(catalog["tracks"], reproduccion["track_id"]) is False:
        mp.put(catalog["tracks"], reproduccion["track_id"], reproduccion)
    
    
# Funciones para creacion de datos


# Funciones de consulta
def characterizebyreproductions(catalog, characteristic, minval, maxval):
    first = catalog["context"]
    second = mp.get(first, characteristic)
    third = me.getValue(second)
    four = om.values(third, minval, maxval)
    artist = lt.newList("ARRAY_LIST", cmpfunction=cmpAuthor)
    auxiliarlist = lt.newList("ARRAY_LIST")
    for element in lt.iterator(four):
        if lt.size(element) >= 1:
            for thing in lt.iterator(element):
                lt.addLast(auxiliarlist, thing)
    for element in lt.iterator(auxiliarlist):
        if lt.isPresent(artist, element["artist_id"]) == 0:
            lt.addLast(artist, element["artist_id"])
    counter = lt.size(artist)
    return counter, lt.size(auxiliarlist)


def partymusic(catalog, value_1, value_2, value_3, value_4):
    view_list = lt.newList("ARRAY_LIST")
    first = catalog["context"]
    second = mp.get(first, "energy")
    third = me.getValue(second)
    four = om.values(third, value_1, value_2)
    auxiliarlist = lt.newList("ARRAY_LIST")
    for element in lt.iterator(four):
        if lt.size(element) >= 1:
            for thing in lt.iterator(element):
                if float(thing["danceability"]) >= value_3 and float(thing["danceability"]) <= value_4:
                    lt.addLast(auxiliarlist, thing)
    unique_track_id = lt.newList("ARRAY_LIST", cmpfunction=cmpunique_id)
    for track in lt.iterator(auxiliarlist):
        if lt.isPresent(unique_track_id, track["track_id"]) == 0:
            lt.addLast(unique_track_id, track["track_id"])
    lt.addLast(view_list, lt.size(unique_track_id))
    mini_list = lt.newList("ARRAY_LIST")
    m = 0
    while m<=5:
        element = random.randint(1, lt.size(unique_track_id))
        lt.addLast(mini_list, lt.getElement(unique_track_id, element))
        m += 1
    lt.addLast(view_list, mini_list)
    return view_list


def studymusic(catalog, value_1, value_2, value_3, value_4):
    view_list = lt.newList("ARRAY_LIST")
    first = catalog["context"]
    second = mp.get(first, "instrumentalness")
    third = me.getValue(second)
    four = om.values(third, value_1, value_2)
    auxiliarlist = lt.newList("SINGLE_LINKED")
    for element in lt.iterator(four):
        if lt.size(element) >= 1:
            for thing in lt.iterator(element):
                if float(thing["tempo"]) >= value_3 and float(thing["tempo"]) <= value_4:
                    lt.addLast(auxiliarlist, thing)
    cantidad = lt.size(auxiliarlist)
    unique_track_id = lt.newList("SINGLE_LINKED", cmpfunction=cmpunique_id)
    for track in lt.iterator(auxiliarlist):
        if lt.isPresent(unique_track_id, track["track_id"]) == 0:
            lt.addLast(unique_track_id, track["track_id"])
    lt.addLast(view_list, lt.size(unique_track_id))
    mini_list = lt.newList("ARRAY_LIST")
    m = 0
    while m<=5:
        element = random.randint(1, lt.size(unique_track_id))
        lt.addLast(mini_list, lt.getElement(unique_track_id, element))
        m += 1
    lt.addLast(view_list, mini_list)
    return view_list
    # print(lt.size(auxiliarlist), counter)
    # print(cantidad, lt.size(unique_track_id))


def musicalgenres(catalog, user_list):
    sublist = user_list.split(",")
    view_list = lt.newList("ARRAY_LIST")
    for element in sublist:
        element_list = lt.newList("ARRAY_LIST")
        lt.addLast(element_list, element)
        ranges = values(catalog, element)
        min_val = lt.getElement(ranges, 1)
        max_val = lt.getElement(ranges, 2)
        first = catalog["context"]
        second = mp.get(first, "tempo")
        third = me.getValue(second)
        four = om.values(third, min_val, max_val)
        auxiliarlist = lt.newList("ARRAY_LIST")
        for element in lt.iterator(four):
            if lt.size(element) >= 1:
                for thing in lt.iterator(element):
                    lt.addLast(auxiliarlist, thing)
        lt.addLast(element_list, lt.size(auxiliarlist))
        unique_track_id = lt.newList("SINGLE_LINKED", cmpfunction=cmpunique_id)
        for track in lt.iterator(auxiliarlist):
            if lt.isPresent(unique_track_id, track["artist_id"]) == 0:
                lt.addLast(unique_track_id, track["artist_id"])
        lt.addLast(element_list, lt.size(unique_track_id))
        sub_lista = lt.subList(unique_track_id, 1, 10)
        lt.addLast(element_list, sub_lista)
        lt.addLast(view_list, element_list)
    return view_list


def values(catalog, characteristic):
    mini_catalog = catalog["genres"]
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 60)
    lt.addLast(value, 90)
    mp.put(mini_catalog, "reggae", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 70)
    lt.addLast(value, 100)
    mp.put(mini_catalog, "down-tempo", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 90)
    lt.addLast(value, 120)
    mp.put(mini_catalog, "chill-out", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 85)
    lt.addLast(value, 115)
    mp.put(mini_catalog, "hip-hop", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 120)
    lt.addLast(value, 125)
    mp.put(mini_catalog, "jazzandfunk", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 100)
    lt.addLast(value, 130)
    mp.put(mini_catalog, "pop", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 60)
    lt.addLast(value, 80)
    mp.put(mini_catalog, "ryb", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 110)
    lt.addLast(value, 140)
    mp.put(mini_catalog, "rock", value)
    value = lt.newList("ARRAY_LIST")
    lt.addLast(value, 100)
    lt.addLast(value, 160)
    mp.put(mini_catalog, "metal", value)
    thing = characteristic.lower().strip()
    real_value = mp.get(mini_catalog, thing)
    result = me.getValue(real_value)
    return result
    

def addfourthreq(catalog, name, mini, maxi):
    repository = catalog["genres"]
    mini_list = lt.newList("ARRAY_LIST")
    lt.addLast(mini_list, mini)
    lt.addLast(mini_list, maxi)
    name = name.lower().strip()
    mp.put(repository, name, mini_list)

def toprepsentimental(catalog, start_hour, final_hour):
    sublist = ["reggae","down-tempo","chill-out","hip-hop","jazzandfunk","pop","ryb","rock","metal"].split(",")
    view_list = lt.newList("ARRAY_LIST")
    for element in sublist:
        element_list = lt.newList("ARRAY_LIST")
        lt.addLast(element_list, element)
        ranges = values(catalog, element)
        min_val = lt.getElement(ranges, 1)
        max_val = lt.getElement(ranges, 2)
        first = catalog["context"]
        second = mp.get(first, "tempo")
        third = me.getValue(second)
        four = om.values(third, min_val, max_val)
        auxiliarlist = lt.newList("ARRAY_LIST")
        for element in lt.iterator(four):
            if lt.size(element) >= 1:
                for thing in lt.iterator(element):
                    lt.addLast(auxiliarlist, thing)
        lt.addLast(element_list, lt.size(auxiliarlist))

def newmaphour(catalog, reproduccion):
    auxiliar = reproduccion["created_at"]
    crimedate = datetime.datetime.strptime(auxiliar, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, crimedate.date())
    if entry is None:
        datentry = newDataEntry(crime)
        om.put(map, crimedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, crime)



# Funciones utilizadas para comparar elementos dentro de una lista


def cmpAuthor(pos1, pos2):
    if pos1 != pos2:
        return True
    return False


def cmpunique_id(pos1, pos2):
    if pos1 != pos2:
        return True
    return False

def compareArtistsByNameMap(keyname, artist):
    """
    Compara dos nombres de artistas. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(artist)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareTracksByNameMap(keyname, track):
    """
    Compara dos id de track. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(track)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
# Funciones de ordenamiento

