
#ejerccio 1

a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))

resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)


print("El resultado es: ",resultado)


#ejercicio 2

a = float(input("a: "))
b = float(input("b: "))

resultado = ((3+5*8)<3 and (-6/3*4)+2<=2) or (a>=b)
 
print(f"El resultado es: {resultado}")


#ejercicio 3

a = input("a: ")
b = input("b: ")

a , b = b , a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")


#ejercicio 4

radio = float(input("radio: "))

area = 3.14 * radio**2
longitud= 2 * 3.14 * radio

print(f"El area del circulo es: {area:.2f}")
print(f"La longitud  de la circunferencia es: {longitud:.2f}")

#ejercicio  5

precio = float(input("Digite el precio: "))

descuento = precio * 0.15
precio_final = precio - descuento
print(f"El precio final a pagar es: {precio_final}")

