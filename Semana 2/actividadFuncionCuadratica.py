#Crea una función en la cual recibas como argumentos los parámetros reales de una función cuadrática, y te regrese x1 y x2.
import cmath


a=float(input("Escriba el valor del primer parametro: "))
b=float(input("Escriba el valor del segundo parametro: "))
c=float(input("Escriba el valor del tercer parametro: "))

def discriminante(a,b,c):
    return (b**2)-(4*a*c)


dis = discriminante(a,b,c)
x1 = (-b+cmath.sqrt(dis))/(2*a)
x2 = (-b-cmath.sqrt(dis))/(2*a)

print("El conjunto de soluciones es {0} , {1}".format(x1,x2))