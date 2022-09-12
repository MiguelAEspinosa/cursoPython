#ActividadBucleGrupo
#Cada compañero dirá un número. Los guardarás en un diccionario, junto con el nombre de tu pareja.
dic = {"Miguel" : 18 , "Juan" : 23, "Julio" : 12 , "Mariana": 78 , "Carlos": -2}

#Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
for k,v in dic.items():
    print (k,v)

# Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.
mayor = dic[max(dic,key=dic.get)]
menor = dic[min(dic,key=dic.get)]
print("El numero mas grande es: ", mayor)
print("El numoer mas pequeño es: ", menor)
