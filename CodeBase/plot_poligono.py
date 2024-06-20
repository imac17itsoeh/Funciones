import matplotlib.pyplot as plt
def generar_poligono_frecuencias(frecuencia_relativa, clases_sorted, marcas_clase):
    plt.figure(figsize = (12, 6)) # (ancho, alto) del grafico
    frecuencia = frecuencia_relativa # Datos del eje y
    

    # Ajuste a las listas para generar el poligono de frecuencias
    datos_x = [0] + marcas_clase + [len(clases_sorted)+1] 
    datos_y = [0] + frecuencia + [0] 
    
    #leyendas para las marcas de clase
    marcas_textos = clases_sorted
    
    # Poligono de frecuencias con:
    # - Estilo de linea punteado (lenestyle ":"). https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    # - Marcador con forma triangular (marker = "v"). https://matplotlib.org/stable/api/markers_api.html
    
    plt.plot(datos_x , datos_y, 
            linewidth = 5, color = "r", linestyle = ":",
            marker = "v", markersize = 15, markeredgecolor = "#FF33F9", markerfacecolor = "#33FFF3") 
    
    plt.xticks(marcas_clase , marcas_textos, fontsize = 15, rotation = 45) # Cambio de las marcas del eje x de numeros a texto
    plt.xlabel("Marcas de clase", fontsize = 25) # Etiqueta del eje x
    plt.ylabel("Frecuencia", fontsize = 25) # Etiqueta del eje y
    plt.title("Poligono de frecuencias", fontsize = 40) # Titulo
    plt.grid() # Se activa la cuadricula
    plt.show() # Se muestra el grafico en pantalla