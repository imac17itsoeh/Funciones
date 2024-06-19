def imptabla(clases_sorted, fa_sorted, fr_relativa, fr_acum):
 

  encabezados = ["Clases", "F absoluta", "F relativa", "F acumulada"]

  
  print("+".join(["-" * len(str(encabezado)) for encabezado in encabezados]) + "+")
  print("| " + " | ".join(encabezados) + " |")
  print("+".join(["-" * len(str(encabezado)) for encabezado in encabezados]) + "+")

  
  for i in range(len(clases_sorted)):
    fila = [clases_sorted[i], fa_sorted[i], fr_relativa[i], fr_acum[i]]
    print("|     " + "     |     ".join([str(dato) for dato in fila]) + "     |    ")

  
  print("+".join(["-" * len(str(encabezado)) for encabezado in encabezados]) + "+")