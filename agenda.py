AGENDA = {}

def show_all_contacts():
    if len(AGENDA) > 0:
        for contatos in AGENDA:
            print("---------------------------------------")
            unique_contact(contatos)
            print("---------------------------------------")
    else:
        print()
        print("Nenhum contato existente")
        print()
        
def unique_contact(contato):
    try:
        print()
        print("Nome: ", AGENDA[contato]["nome"])
        print("Telefone: ", AGENDA[contato]["tel"])
        print("Email: ", AGENDA[contato]["email"])
        print("Endereço: ", AGENDA[contato]["endereco"])
        print()
    except Exception as error:
        print()
        print("This contact don't exist")
        print(error)
        print()


def add_contacts(contato,tel,email,endereco):
    AGENDA[contato] = {
        "nome": contato,
        "tel": tel,
        "email": email,
        "endereco": endereco
    }
    print()
    print("Contato adicionado com sucesso")
    salvar()
    unique_contact(contato)
    print()


def edit_contacts(contato,valor,informacao):
    print("---------------------------------------")
    AGENDA[contato][valor] = informacao
    print("Alteração do {} realizada com sucesso".format(valor))
    salvar()
    print("---------------------------------------")

def delet_contacts(contact):
    try:
        AGENDA.pop(contact)
        print()
        print("Contato {} excluido com sucesso".format(contact))
        print()
        salvar()
    except:
        print("This contact don't exist")


def menu():
    print("*******************************")
    print("1 - Mostrar contatos")
    print("2 - Adicionar contato")
    print("3 - Excluir contato")
    print("4 - Editar contato")
    print("5 - Buscar contato")
    print("6 - Exportar agenda")
    print("7 - Importar contatos")
    print("0 - Sair da agenda")
    print("*******************************")


def exportar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "w") as file:
            for contatos in AGENDA:
                nome = AGENDA[contatos]["nome"]
                telefone = AGENDA[contatos]["tel"]
                email = AGENDA[contatos]["email"]
                endereco = AGENDA[contatos]["endereco"]
                file.write("{}, {}, {}, {},\n".format(nome, telefone, email, endereco)) 
        print("Agenda exportada com sucesso")
        salvar()
    except Exception as e:
        print("Ocorreu um erro inesperado") 


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo) as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                contato = detalhes[0]
               
                if contato in AGENDA:
                    print("Contato já existe")
                else:
                    nome = contato
                    tel = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]
                    add_contacts(nome, tel, email, endereco)
                    salvar()
    except Exception as erros:
        print("Ocorreu um erro inesperado")
        print(erros)


def salvar():
    try:
        with open("database.csv", "w") as file:
            for contatos in AGENDA:
                nome = AGENDA[contatos]["nome"]
                telefone = AGENDA[contatos]["tel"]
                email = AGENDA[contatos]["email"]
                endereco = AGENDA[contatos]["endereco"]
                file.write("{}, {}, {}, {},\n".format(nome, telefone, email, endereco)) 
    except Exception as e:
        print("Ocorreu um erro inesperado") 


def carregar():
    try:
        if len("database.csv") > 0:
            with open("database.csv") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    detalhes = linha.strip().split(',')
                    contato = detalhes[0]
                    tel = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]
                    AGENDA[contato] = {
                            "nome": contato,
                            "tel": tel,
                            "email": email,
                            "endereco": endereco
                    }
        else:
            pass
    except FileNotFoundError:
        pass
    except Exception as erros:
        print("Ocorreu um erro inesperado")
        print(erros)


carregar()
while True:
    
    print("Bem vindo a sua agenda. Abaixo você terá seu menu de opções.")
    print("**************************************************************")
    menu()
    print("**************************************************************")
    opcao = input("O que gostaria de fazer? Escolha um numero: ")

    if opcao == "1":
        show_all_contacts()

    elif opcao == "2":
        contato = input("Informe o nome do contato a ser adicionado: ")
        if contato in AGENDA:
            print("Contato já existe")
        else:
            tel = input("Informe o numero de telefone: ")
            endereco = input("Informe o endereço: ")
            email = input("informe o email: ")
            add_contacts(contato, tel, endereco, email)
            unique_contact(contato)


    elif opcao == "3":
        contato = input("Informe o nome do contato a ser excluido: ")
        delet_contacts(contato)


    elif opcao == "4":
        contato = input("Em qual usuario gostaria de fazer a alteração?: ")
        if contato in AGENDA:
            valor = input("Qual informação gostaria de alterar?: ")
            informacao = input("Insira a nova informacao: ")
            edit_contacts(contato, valor, informacao)
            unique_contact(contato)
          
        else: 
            print("Contato não existe")

    elif opcao == "5":
        contato = input("Informe qual o nome do contato que deseja buscar: ")
        unique_contact(contato)

    elif opcao == "6":
        nome_do_arquivo = input("Informe o nome do arquivo para ser exportado: ")
        exportar_agenda(nome_do_arquivo)
    
    elif opcao == "7":
        nome_do_arquivo = input("Informe o nome do arquivo a ser importado: ")
        print()
        importar_contatos(nome_do_arquivo)
        print()

    elif opcao == "0":
        print("Saindo da agenda. Obrigado")
        break

    else:
        print("Opção invalida")