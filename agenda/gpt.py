# Dicionário global para armazenar os contatos
AGENDA = {}

def add_contacts(contato, tel, email, endereco):
    AGENDA[contato] = {
        "nome": contato,
        "tel": tel,
        "email": email,
        "endereco": endereco
    }
    print("Contato adicionado com sucesso")
    salvar()

def alterar_contato(contato, campo, novo_valor):
    if contato in AGENDA:
        if campo in AGENDA[contato]:
            AGENDA[contato][campo] = novo_valor
            print(f"{campo.capitalize()} alterado com sucesso")
        else:
            print(f"Campo {campo} não encontrado")
    else:
        print("Contato não encontrado")
    salvar()

def salvar():
    # Função fictícia para salvar as alterações, implementar conforme necessário
    print("Alterações salvas")

# Exemplo de uso
add_contacts("João", "1234-5678", "joao@email.com", "Rua A")
print(AGENDA)

# Função para mostrar as opções de alteração
def menu_alterar():
    contato = input("Digite o nome do contato a ser alterado: ")
    if contato in AGENDA:
        print("Campos disponíveis para alteração: nome, tel, email, endereco")
        campo = input("Digite o campo que deseja alterar: ").strip().lower()
        novo_valor = input(f"Digite o novo valor para {campo}: ").strip()
        alterar_contato(contato, campo, novo_valor)
    else:
        print("Contato não encontrado")

# Chamando a função de menu para alterar o contato
menu_alterar()
print(AGENDA)
