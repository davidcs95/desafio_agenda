from modulos_agenda import *

contatos = []
while True:
    print("\nO que deseja fazer?")
    print("1. Adicionar contato")
    print("2. Ver lista de contatos")
    print("3. Marcar/Desmarcar contato como favorito")
    print("4. Ver contatos favoritos")
    print("5. Apagar contato")
    print("6. Sair")

    escolha = input("Digite uma opção: ")
    if escolha == "1":
        adicionar_contato(contatos)
    elif escolha == "2":
        pass
    elif escolha == "3":
        pass
    elif escolha == "4":
        pass
    elif escolha == "5":
        pass
    elif escolha == "6":
        break

print("Programa finalizado")
