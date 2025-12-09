def equipos(datosliga) -> set:

    """
    Función que recibe la lista de diccionarios con 
    los datos de la liga y devuelve un conjunto con los equipos de la liga.
    
    :param datosliga: Le pasamos los datos extraidos del csv
    :return: Retorna los equipos
    :rtype: set
    """

    equipos = set()
    for partido in datosliga:
        equipos.add(partido["Team 1"])
        equipos.add(partido["Team 2"])
    return equipos


