from unittest import case

from exercícios.ex019.crud import *

lista_acoes = {
    "1": "Cadastrar pessoa",
    "2": "Listar pessoas",
    "3": "Atualizar pessoa",
    "4": "Excluir pessoa",
    "5": "Busca por nome",
    "0": "Sair"
}


def exibir_menu():
    print("\n" + '=' * 30)
    print("{:^30}".format(" SISTEMA DE CADASTRO "))
    print("=" * 30)
    for acao in lista_acoes:
        print(" " + acao + " - " + lista_acoes[acao])
    print("=" * 30)


def main():

    if not criar_banco():
        print("Algum problema aconteceu ao criar o banco")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                if not cadastrar_pessoa():
                    print("[ERRO] Não foi possível cadastrar a pessoa")

            case "2":
                if not listar_pessoas():
                    print("[ERRO] Não foi possível mostrar a listagem de pessoas")

            case "3":
                if not atualizar_pessoa():
                    print("[ERRO] Não foi possível atualizar o cadastro")

            case "4":
                if not excluir_pessoa():
                    print("[ERRO] Não foi possível excluir a pessoa")

            case "5":
                if not buscar_pessoa_por_nome():
                    print("[ERRO] Não foi possível buscar os dados")

            case "0":
                print("\nEncerrando o sistema...")
                break

            case _:
                print("\n[ERRO] Opção inválida! Escolha um valor entre 0 e 5!")

        input("Pressione ENTER para continuar...")



if __name__ == '__main__':
    main()
