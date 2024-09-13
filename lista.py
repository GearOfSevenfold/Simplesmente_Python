# Um exemplo de como criar listas em Python.
# A lista é ordenada, logo ao printar seus valores, serão apresentados na ordem em que foram incluidas.
# É possivel alterar o valor impudado na lista

minha_lista = ["Azul","Vermelho","Amarelo","Verde"]

#Adicionando um novo item a lista
minha_lista.append("Roxo")

#todo o valor da lista:
print(minha_lista)

# Removendo um item da lista
minha_lista.remove("Vermelho")
print(minha_lista)

#selecionando um valor da lista
print(minha_lista[1])

#selecionando mais de uma valor da lista
print(minha_lista[1:3])

#outras atribuições
minha_lista.append("roxo")