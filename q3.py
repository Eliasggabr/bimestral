print("Soma pares e ímpares")
lista = []
par = []
impar = []
for i in range(10):
    numeros = int(input(f"Digite o {i + 1} número: "))
    lista.append(numeros)
print(f"A lista: {lista}")
for i in lista:
    if i %2 == 0:
        par.append(i)

    else:
        impar.append(i)
print(par)
print(impar)
soma_par = sum(par)
soma_impar = sum(impar)
print(f"A soma dos pares: {soma_par}")
print(f"A soma dos ímpares: {soma_impar}")