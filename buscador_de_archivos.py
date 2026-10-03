import os

def buscar_archivos(carpeta, nombre_buscado):
    """Esta funcion busca archivos igual al nombre buscado"""
    resultados = []
    total_encontrados = 0
    total_archivos_revisados = 0

    # Recorre capetas y subcarpetas con os.walk
    # (Python Software Foundation, s. f.)
    #PARA CADA carpeta y subcarpeta DENTRO DE carpeta
    for ruta_actual, subcarpetas, archivos in os.walk(carpeta):
        #PARA CADA archivo DENTRO DE la carpeta actual
        for archivo in archivos:
            total_archivos_revisados = total_archivos_revisados + 1
        #SI nombre_buscado ESTA CONTENIDO en el nombre del archivo ENTONCES
        if nombre_buscado.lower() in archivo.lower():
            #GUARDAR ruta completa del archivo en resultados
            resultados.append(os.path.join(ruta_actual, archivo))
            total_encontrados = total_encontrados + 1
    
    #EVITAR DIVISION ENTRE CERO SI NO SE REVISO NINGUN ARCHIVO
    if total_archivos_revisados == 0:
        porcentaje_coincidencia = 0
    else:
        porcentaje_coincidencia = (
            total_encontrados * 100) / total_archivos_revisados
    
    return resultados, total_encontrados, porcentaje_coincidencia

def principal():
    """Esta funcion pide los datos al ususario y muestra los resultados"""
    carpeta = input("Introduce la ruta de la carpeta:")
    nombre_buscado = input("Introduce el archivo:")
    
    
    resultados, total_encontrados, porcentaje_coincidencia = \
        buscar_archivos(carpeta, nombre_buscado)
    
    if total_encontrados == 0:
        print("No se encontraron archivos")
    else:
        print("total encontrados:", total_encontrados)
        for ruta in resultados:
            print(ruta)

        print(f"porcentaje de coincidencia: {porcentaje_coincidencia:.2f}%")

principal()