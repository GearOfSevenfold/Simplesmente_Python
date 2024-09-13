agenda = {
"Enio": {
    "Tel": "11-99876-1111",
    "Email": "teste@teste.com.br",
    "Endereco": "Av. Teste 1"
},
"Andrea": {
    "Tel": "11-99876-2222",
    "Email": "andrea@teste.com.br",
    "Endereco": "Av. Teste 2"
},
"Nestor": {
    "Tel": "11-99876-3333",
    "Email": "nestor@teste.com.br",
    "Endereco": "Av. Teste 3"
}
 }

agenda['pedro'] = {
    "Tel": "12 99920-5654",
    "Email": "pedro@teste.com.br",
    "Endereco": "Rua: Testando apenas, 2425"
    #adicionando mais um valor ao dicionario, no caso o usuario pedro e suas respectivas informações
}

agenda['Enio']['Endereco'] = "Rua, anapolis, 2024" # Alterando o valor de endereço de uma chave criada, no caso Enio

agenda.pop("Nestor") # remove um valor do dicionario

for i in agenda:
    print(i)