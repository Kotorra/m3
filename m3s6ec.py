n=int(input("Ingrese un número entero: "))
print("................................")

if n>0:
	if n%2==0:
		print(f"El número '{n}' es un número positivo y par.")
	else:
		print(f"El número '{n}' es un número positivo e impar.")
elif n<0:
	if n%2==0:
		print(f"El número '{n}' es un número negativo y par.")
	else:
		print(f"El número '{n}' es un número negativo e impar.")
else:
	print(f"El número es cero, es un número neutral, entero y par.")
