# ENTRADAS
# carpeta - texto (ruta de la carpeta donde se realizará la búsqueda)
# nombre_buscado - texto (nombre o parte del nombre del archivo)

# PROCESO
# FUNCION buscar_archivos(carpeta, nombre_buscado)
# 1. Inicio
# 2. DEFINIR resultados = lista vacia
# 3. DEFINIR total_encontrados = 0
# 4. DEFINIR total_archivos_revisados = 0
# 5. PARA CADA carpeta y subcarpeta DENTRO DE carpeta
#    5.1. PARA CADA archivo DENTRO DE la carpeta actual
#         5.1.1. SUMAR 1 a total_archivos_revisados
#         5.1.2. SI nombre_buscado ESTA CONTENIDO en el nombre del archivo ENTONCES
#                5.1.2.1. GUARDAR ruta completa del archivo en resultados
#                5.1.2.2. SUMAR 1 a total_encontrados
# 6. CALCULAR porcentaje_coincidencia = (total_encontrados * 100) / total_archivos_revisados
# 7. RETORNAR resultados, total_encontrados, porcentaje_coincidencia
# FIN FUNCION
#
# FUNCION principal()
# 1. Inicio
# 2. PEDIR carpeta al usuario
# 3. PEDIR nombre_buscado al usuario
# 4. LLAMAR A buscar_archivos(carpeta, nombre_buscado)
# 5. GUARDAR resultado en resultados, total_encontrados, porcentaje_coincidencia
# 6. SI total_encontrados = 0 ENTONCES
#    6.1. MOSTRAR "No se encontraron archivos"
# 7. SINO
#    7.1. MOSTRAR total_encontrados
#    7.2. MOSTRAR cada ruta contenida en resultados
#    7.3. MOSTRAR porcentaje_coincidencia
# 8. Fin
# FIN FUNCION
#
# LLAMAR A principal()

# SALIDAS
# total_encontrados - número entero
# resultados - lista de texto (rutas completas de los archivos encontrados)
# porcentaje_coincidencia - número decimal (% de archivos que coincidieron respecto al total revisado)