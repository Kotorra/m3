numeros=list(range(10))
for i in range(len(numeros)):
	if numeros[i]==0:
		print(f"El número de la lista en la posición {i}, es cero y par. N°={numeros[i]}")
	elif numeros[i]%2==0:
		print(f"El número de la lista en la posición {i} es par. N°={numeros[i]}")
	else:
		print(f"El número de la lista en la posición {i} es impar. N°={numeros[i]}")
