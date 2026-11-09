import sqlite3
from datetime import date


def calcular_idade(data):
    hoje = date.today()

    corretor = 0 if (hoje.month, hoje.day) >= (data.month, data.day) else -1
    return (int(hoje.year) - int(data.year)) + corretor


while True:
    busca = input("Qual amigo deseja procurar? (X para fechar)").strip()

    try:
        with sqlite3.connect('meubanco.db') as conexao:

            conexao.row_factory = sqlite3.Row

            cursor = conexao.cursor()
            cursor.execute(
                '''SELECT * FROM amigo WHERE NOME LIKE ?;''',
                (f"%{busca}%",)
            )

            total = 0
            resultados = []

            for total, item in enumerate(cursor, start=1):
                txt_nasc = item['nascimento']
                data_nasc_iso = ""
                info_nasc = "Sem data de nascimento"
                idade_info = "."

                if txt_nasc:
                    try:
                        data_nasc_iso = date.fromisoformat(str(item['nascimento']))
                        info_nasc = f"nasceu em {data_nasc_iso:%d/%m/%Y}"

                        idade_info = f"hoje tem {calcular_idade(data_nasc_iso)} anos"

                    except ValueError:
                        print(f"Erro ao converter datas...")

                texto = f"{item['nome']} {info_nasc}, {idade_info}"
                resultados.append(texto)

            if (total != 0):

                singular = "Apenas 1 amigo foi encontrado"
                plural = f"Ao todo {total} amigos foram encontrados"
                texto = plural if total > 1 else singular
                print(f"\n{texto} com a busca: [ {busca} ]")

                print("\nResultados:\n")

                print("-" * 30)

                for item in resultados:
                    print(item)

                print("-"*30, "\n")

            else:
                print(f"Nenhum amigo foi encontrado com a busca: [ {busca} ]!")

    except sqlite3.Error as erro:
        print(f"Falha no Banco de dados: {erro}")

    except Exception as error:
        print(f"Algo deu errado: {error}")

    if busca == "x":
        break


print("Fim da execução de Banco de Dados")
