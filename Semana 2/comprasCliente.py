#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que se cargarán, que pueden cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingresa el monto 0.

#Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad. Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de $1000, se debe aplicar un 10% de descuento.

total = 0
oferta = 1000
costo = float(input("Ingrese el costo del producto:"))
while costo != 0:
    if costo > 0:
        total = total + costo
    costo = float(input("Ingrese el costo del producto:"))
if total > oferta:
    print("El total es : ", total*.90)
else:
    print("El total es :", total)