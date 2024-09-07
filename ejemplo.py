xd="xdd11"
numero="1234"
print(xd.isdigit())
print(numero.isdigit())
while True:
	while True:
		entrada = input("Escribe un numero entero positivo: ")
		try:
			entrada = int(entrada)
			break
		except ValueError:
			pass

	if entrada>0:
		break
	else:
		print("La entrada es incorrecta: escribe un numero entero positivo")

