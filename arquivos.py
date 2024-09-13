# o .strip() remove todos os espaçoes em branco na hora de apresentar as informações.

try:
    with open("emails.doc") as arquivos:
        conteudo = arquivos.readlines()
        for linhas in conteudo:
            print(linhas.strip())
except FileNotFoundError:
    print("Arquivo não encontrado")
except: 
    print("Um erro inexperado aconteceu")