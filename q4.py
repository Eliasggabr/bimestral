lista_de_nomes = []
for i in range(5):
    nomes = input(f"Digite o {i + 1} nome: ")
    lista_de_nomes.append(nomes)
busca = input("Digite o nome que você quer procurar: ")
if busca in lista_de_nomes:
    print("Convidado confirmado!")
else:
    print("Convidado não encontrado!")