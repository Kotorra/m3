num=int(input("Ingresa un número: "))
resultado=1
for i in range(num+1):
	if (i == 0):
		continue
	resultado=resultado*i

print(resultado)

