def leer_archivos(ruta):
    with open(ruta, "r") as archivo:
        primera_linea = archivo.readline()
        if not primera_linea.startswith("#"):
            arreglo = [int(n) for n in primera_linea.split(";")]
        else: 
            numeros = archivo.readline()
            arreglo = [int(n) for n in numeros.split(";")]
        return arreglo