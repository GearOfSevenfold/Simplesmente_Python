📅 Agenda Simples em Python

Bem-vindo ao projeto de Agenda Simples em Python! Este projeto é uma excelente oportunidade para praticar e entender conceitos básicos da programação em Python, incluindo dicionários, manipulação de arquivos e interações básicas com o usuário.
🚀 Sobre o Projeto

O projeto Agenda Simples é um sistema de gerenciamento de contatos que permite adicionar, visualizar, editar, excluir e importar/exportar contatos. Embora não seja um projeto avançado, é uma excelente ferramenta para aprender e praticar operações básicas com Python.
📋 Funcionalidades

    Mostrar Todos os Contatos: Exibe todos os contatos armazenados na agenda.
    Adicionar Contato: Permite adicionar novos contatos à agenda com informações básicas.
    Excluir Contato: Remove contatos existentes da agenda.
    Editar Contato: Atualiza informações de um contato existente.
    Buscar Contato: Encontra e exibe detalhes de um contato específico.
    Exportar Agenda: Salva a agenda atual em um arquivo CSV.
    Importar Contatos: Carrega contatos de um arquivo CSV para a agenda.

💻 Código Principal

Aqui estão os principais trechos do código que fazem o sistema funcionar:
Inicialização

python

AGENDA = {}

Mostrar Todos os Contatos

python

def show_all_contacts():
    if len(AGENDA) > 0:
        for contatos in AGENDA:
            print("---------------------------------------")
            unique_contact(contatos)
            print("---------------------------------------")
    else:
        print("\nNenhum contato existente\n")

Adicionar Contato

python

def add_contacts(contato, tel, email, endereco):
    AGENDA[contato] = {
        "nome": contato,
        "tel": tel,
        "email": email,
        "endereco": endereco
    }
    print("\nContato adicionado com sucesso")
    salvar()
    unique_contact(contato)
    print()

Editar Contato

python

def edit_contacts(contato, valor, informacao):
    print("---------------------------------------")
    AGENDA[contato][valor] = informacao
    print(f"Alteração do {valor} realizada com sucesso")
    salvar()
    print("---------------------------------------")

Excluir Contato

python

def delet_contacts(contact):
    try:
        AGENDA.pop(contact)
        print(f"\nContato {contact} excluído com sucesso\n")
        salvar()
    except:
        print("Este contato não existe")

Exportar Agenda

python

def exportar_agenda(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "w") as file:
            for contatos in AGENDA:
                nome = AGENDA[contatos]["nome"]
                telefone = AGENDA[contatos]["tel"]
                email = AGENDA[contatos]["email"]
                endereco = AGENDA[contatos]["endereco"]
                file.write(f"{nome}, {telefone}, {email}, {endereco},\n")
        print("Agenda exportada com sucesso")
        salvar()
    except Exception as e:
        print("Ocorreu um erro inesperado")

Importar Contatos

python

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

Carregar Dados

python

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
    except FileNotFoundError:
        pass
    except Exception as erros:
        print("Ocorreu um erro inesperado")
        print(erros)

🛠 Como Rodar o Projeto

    Clone o Repositório:

    bash

git clone https://github.com/seu-usuario/agenda-simples-python.git

Navegue até o Diretório do Projeto:

bash

cd agenda-simples-python

Execute o Script Principal:

bash

    python agenda.py

📌 Menu de Opções

Ao executar o script, você verá o menu abaixo para interagir com a agenda:

1 - Mostrar contatos
2 - Adicionar contato
3 - Excluir contato
4 - Editar contato
5 - Buscar contato
6 - Exportar agenda
7 - Importar contatos
0 - Sair da agenda

Escolha uma opção digitando o número correspondente e siga as instruções para gerenciar seus contatos.

🤔 Contribuições

Se você deseja melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Suas contribuições são bem-vindas!
