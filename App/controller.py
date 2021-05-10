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
import sys
import config as cf
import model
import csv
import time
import tracemalloc
from DISClib.ADT import list as lt
default_limit = 1000
sys.setrecursionlimit(default_limit*10)





"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.init_Catalog()
    return catalog

# Funciones para la carga de datos
def loadVideos(catalog):
    videosfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for reproduccion in input_file:
        model.addplaylist(catalog, reproduccion)
        # model.addauthor(catalog, reproduccion)
    
    


def loadhashtags(catalog):
    hashtagfile = cf.data_dir + "user_track_hashtag_timestamp-small.csv"
    imputfile = csv.DictReader(open(hashtagfile, encoding="utf-8"))
    for hashtag in imputfile:
        model.addhashtag(catalog, hashtag)
    

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def firstreq(catalog, characteristic, minval, maxval):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    answer = model.characterizebyreproductions(catalog, characteristic, minval, maxval)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory


def secondreq(catalog, val_1, val_2, val_3, val_4):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    answer = model.partymusic(catalog, val_1, val_2, val_3, val_4)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory


def thirdreq(catalog, val_1, val_2, val_3, val_4):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    answer = model.studymusic(catalog, val_1, val_2, val_3, val_4)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory

def fourthreq(catalog, user_list):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    answer = model.musicalgenres(catalog, user_list)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory

def addfourthreq(catalog, name, mini, maxi):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    answer = model.addfourthreq(catalog, name, mini, maxi)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return answer, delta_time, delta_memory
    
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory