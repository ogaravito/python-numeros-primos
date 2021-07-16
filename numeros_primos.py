#Genera listado de números primos

def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))

for i in range(2,numero+1):
	if(primo(i)):
		print(i)