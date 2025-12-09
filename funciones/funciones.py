import csv

def leerPartidos() -> list:
    """
    Función que lee el archivo liga.csv y lo devuelve como
    una lista de diccionarios
    
    :return: El contenido del archivo en una lista de diccionarios
    :rtype: list[dict]
    """
    with open('liga.csv', 'r', encoding="utf-8",) as fCSV:
        content = list(csv.DictReader(fCSV))
    fCSV.close()
    return content

def impClasificacionLiga(liga) -> None:
    equipos(liga)


def equipos(datosliga) -> set:
    """
    Función que recibe la lista de diccionarios con los datos 
    de la liga y devuelve un conjunto con los equipos de la liga.
    
    :param datosliga: Le pasamos los datos extraidos del csv
    :return: Retorna los equipos
    :rtype: set
    """
    equipos = set()
    for partido in datosliga:
        equipos.add(partido["Team 1"])
        equipos.add(partido["Team 2"])
    return equipos

def infoEquipos (datosLiga: list,equipos: set) -> list[tuple]:
    return list() 

def quienGana(resultado) -> int:
    return 0

def puntos(info: list) -> int:
    return 0

def clasificacion(datos: list) -> list:
    return list() 

#---------------------------------------------

datosliga = leerPartidos()
impClasificacionLiga(datosliga)