def sum():
	a=int(input("Ingrese un número a sumar: "))
	b=int(input("Ingrese otro número a sumar: "))
	a=a+b
	return a

sum=sum()
print(f"El resultado de la suma es: {sum}\n")

def resta():
	a=int(input("Ingrese un número a restar: "))
	b=int(input("Ingrese otro número a restar: "))
	a=a-b
	return a
resta=resta()
print(f"El resultado de la resta es: {resta}.\n")

def mult():
	a=int(input("Ingrese un número a multiplicar: "))
	b=int(input("Ingrese otro número a multiplicar: "))
	a=a*b
	return a
mult=mult()
print(f"El resultado de la multiplicación es: {mult}\n")

def div():
	a=float(input("Ingrese un número a dividir: "))
	b=float(input("Ingrese otro número a dividir: "))
	a=(a/b)
	return a
div=div()
print(f"El resultado de la multiplicación es: {div}\n")


a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
def operador(a,b):
	c=float(a)
	d=float(b)
	return ((a+b),(a-b),(a*b),(round((c/d),2)))
operador=operador(a,b)
diccionario={"Suma":operador[0],"Resta":operador[1],"Multiplicación":operador[2],"División":operador[3]}
print(diccionario)
