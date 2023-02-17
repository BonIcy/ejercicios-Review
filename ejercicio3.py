""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """ 

valorKm= int(input("Inserta el sueldo basico por cada kilometro (km)recorrido"))
kmRecorrido= int(input("Inserta el total de kilometros(km) recorridos durante la vuelta a España"))
camLider = input("Durante la vuelta portó la camisa de lider (Y/N")

valorKmLider = 0
totalKm = 0
total= 0

if(camLider == "Y"):
    kmLider = int(input(f"¿De los {kmRecorrido}km cuantos se hicieron con la camisa de lider puesta?"))
    if(kmLider > 1800):
        kmLider = kmLider - 1800
        recargoEspecial = (valorKm * 0.25) + valorKm
        valorKmLider = kmLider * recargoEspecial
        totalKm = (kmRecorrido * valorKm)
        total = totalKm + valorKmLider
        print(f"Se le asignara un pago de ${totalKm} por recorrer {kmRecorrido} en la vuelta a España")
        print(f"Ademas de obetener ${valorKmLider} por tener mas de 1800km con la camisa de lider puesta")
        print(f"Entonces, el total de pago recibido de tu parte es de ${total}")

else:
    totalKm = (kmRecorrido * valorKm)
    print(f"Se le asignara un pago de ${totalKm} por recorrer {kmRecorrido} en la vuelta a España")