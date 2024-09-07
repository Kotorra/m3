print("Ingrese tres números enteros: \n")

n1=(int(input("Ingrese el primer N°: ")))
print("--------------------------------------")
n2=(int(input("Ingrese el segundo N°: ")))
print("--------------------------------------")
n3=(int(input("Ingrese el tercer N°: ")))
print("--------------------------------------")

if n1>n2 and n1>n3:
	if n2>n3:
		print(f"El orden de mayor a menor de los números es {n1},{n2},{n3}")
	else:
		print(f"El orden de mayor a menor de los números es {n1},{n3},{n2}")
elif n2>n1 and n2>n3:
	if n1>n3:
		print(f"El orden de mayor a menor de los números es {n2},{n1},{n3}")
	else:
		print(f"El orden de mayor a menor de los números es {n2},{n3},{n1}")

elif n3>n2 and n3>n1:
	if n2>n1:
		print(f"El orden de mayor a menor de los números es {n3},{n2},{n1}")
	else:
		print(f"El orden de mayor a menor de los números es {n3},{n1},{n2}")
elif n1==n2 and n1>n3:
	print(f"El número {n1} y {n2} son iguales. Su orden de mayor a menor es {n1},{n2},{n3}.")
elif n1==n3 and n1>n2:
	print(f"El número {n1} y {n3} son iguales. Su orden de mayor a menor es {n1},{n3},{n3}.")
elif n2==n3 and n2>n1:
	print(f"El número {n2} y {n3} son iguales. Su orden de mayor a menor es {n2},{n3},{n1}.")
else:
	print(f"Los números {n1},{n2} y {n3} son iguales.")

				

