def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    if "@" not in contato["email"]:
        print("]nEmail deve seguir o padrão xxxx@xxxx.com.br. Tente novamente")
    else:
        contatos.append(contato)
        print(f"\nContato de {nome} salvo com sucesso")
    return

def visualizar_contatos(contatos):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✩" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{favorito}] {nome} - {telefone} - {email}")
    return

def marcar_desmarcar_favorito(contatos):
    visualizar_contatos(contatos)
    try:
        indice_contato_favoritar = int(input("\nInforme o contato para favoritar ou desfavoritar: ")) - 1
        if indice_contato_favoritar >= 0 and indice_contato_favoritar < len(contatos):
            contato = contatos[indice_contato_favoritar]
            contato["favorito"] = False if contato["favorito"] else True
            mensagem = f"Contato {indice_contato_favoritar + 1} marcado como favorito" \
                if contato["favorito"] else \
                    f"Contato {indice_contato_favoritar + 1} desmarcado como favorito"
            print(mensagem)
        else:
            print("\nContato inexistente")
    except ValueError as e:
        print(f"Ocorreu o erro: {e}. \nDigite um numero inteiro")
    finally:
        return

def visualizar_favoritos(contatos):
    print("\nLista de contatos favoritos: ")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✩"
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        if contato["favorito"]:
            print(f"{indice}. [{favorito}] {nome} - {telefone} - {email}")
    return

def apagar_contato(contatos):
    visualizar_contatos(contatos)
    try:
        contato_apagar = int(input("\nInforme qual contato deseja apagar: ")) - 1
        if contato_apagar >= 0 and contato_apagar < len(contatos):
            del contatos[contato_apagar]
            print(f"\nContato {contato_apagar + 1} apagado com sucesso")
        else:
            print("\nContato inexistente")
    except ValueError as e:
        print(f"Ocorreu o erro: {e}. \nDigite um numero inteiro")
    finally:
        return