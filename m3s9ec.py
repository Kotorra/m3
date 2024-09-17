#Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo.
#Validar que ambos sean números positivos

def area(base,altura):
	area=base*altura
	return area

print("#### Calculadora de área de un rectángulo #####\n")

while True:
	base=int(input("Ingrese la longitud de la base del rectángulo: "))
	altura=int(input("Ingrese la longitud de la altura del rectángulo: "))
	if base>0 and altura>0:
		break

area=area(base,altura)
print(f"El área del rectángulo es: {area} unidades cuadradas.")