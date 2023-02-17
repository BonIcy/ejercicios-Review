""" 4. Una empresa tiene 3 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general. """

# Definimos una constante para el número de almacenes
NUM_ALMACENES = 1

# Creamos un diccionario para almacenar la información de ventas de cada almacén
ventas_almacenes = {}

# Pedimos al usuario que ingrese la información de ventas de cada almacén
for i in range(1, NUM_ALMACENES + 1):
    print("Ingrese información de ventas para el almacén", i)
    nombre_almacen = input("Nombre del almacén: ")
    ventas = {}
    for j in range(1, 6):
        tipo_articulo = input("Tipo de artículo vendido: ")
        unidades_vendidas = int(input("Número de unidades vendidas: "))
        ventas[tipo_articulo] = unidades_vendidas
    ventas_almacenes[nombre_almacen] = ventas

# Determinamos el almacén que más vendió y el artículo más vendido de ese almacén
max_ventas_almacen = None
max_ventas_articulo_almacen = None
max_ventas_total = 0
max_ventas_articulo_total = None

for nombre_almacen, ventas in ventas_almacenes.items():
    total_ventas_almacen = sum(ventas.values())
    if total_ventas_almacen > max_ventas_total:
        max_ventas_total = total_ventas_almacen
        max_ventas_almacen = nombre_almacen
        max_ventas_articulo_almacen = max(ventas, key=ventas.get)
    max_ventas_articulo = max(ventas, key=ventas.get)
    if max_ventas_articulo_total is None or ventas[max_ventas_articulo] > ventas[max_ventas_articulo_total]:
        max_ventas_articulo_total = max_ventas_articulo

# Mostramos los resultados
print("El almacén que más vendió fue:", max_ventas_almacen)
print("El artículo más vendido en ese almacén fue:", max_ventas_articulo_almacen)
print("El artículo más vendido en general fue:", max_ventas_articulo_total)