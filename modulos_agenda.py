# contato terá nome, telefone, email, favorito

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato de {nome} salvo com sucesso")
    return

def visualizar_contatos():
    pass

def marcar_desmarcar_favorito():
    pass

def visualizar_favoritos():
    pass

def apagar_contato():
    pass
