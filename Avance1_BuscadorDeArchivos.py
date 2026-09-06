# ENTRADAS
# carpeta - texto (ruta de la carpeta donde se realizará la búsqueda)
# nombre_buscado - texto (nombre o parte del nombre del archivo)

# PROCESO 
# Inicio
# PEDIR carpeta al usuario
# PEDIR nombre_buscado al usuario
# DEFINIR resultados = lista vacia
# DEFINIR total_encontrados = 0
# DEFINIR total_archivos_revisados = 0
# RECORRER todas las carpetas y subcarpetas de carpeta
#       a. RECORRER todods los archivos de la carpeta actual 
#             1. SUMAR 1 a total_archivos_revisados
#             2. Si nombree:buscado ESTA CONTENIDO en el nombre del archivo ENTONCES
#                   - GUARDAR ruta completa del archivo en resultados
#                   - SUMAR 1 a total_encontrados
# CALCULAR porcentaje_coincidencia = (total_encontrados * 100) / total_archivos_revisados
# SI total_encontrados = 0 ENTONCES
#   a. MOSTRAR "No se encontraron archivos"
# SINO 
#   a. MOSTRAR total_encontrados
#   b. MOSTRAR cada ruta contenida en resultados
#   c. MOSTRAR porcentaje_coincidencia
# FIN

# SALIDAS
# total_encontrados - número entero
# resultados - lista de texto (rutas completas de los archivos encontrados)
# porcentaje_coincidencia - número decimal (% de archivos que coincidieron respecto al total revisado)