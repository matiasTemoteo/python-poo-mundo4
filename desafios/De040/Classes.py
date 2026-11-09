from functools import singledispatchmethod
import xml.etree.ElementTree as ET
import json


class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class JSON:

    def __init__(self):
        pass


    def exportar(self, d_list: list[Aluno]|list[Usuario]):

        lista = []

        for elemento in d_list:

            lista.append(elemento.__dict__)

        resultado = json.dumps(
            lista,
            sort_keys=False,
            ensure_ascii=False,
            indent=2
        )

        return resultado


class XML:

    def __init__(self):
        pass


    def exportar(self, d_list: list[Aluno]|list[Usuario]):

        nome = d_list[0].__class__.__name__.lower()
        root = ET.Element('dados')

        for item in d_list:
            sub_1 = ET.SubElement(root, nome)
            for chave, valor in item.__dict__.items():
                sub_2 = ET.SubElement(sub_1, chave)
                sub_2.text = str(valor)

        ET.indent(root, space="\t")
        tree = ET.tostring(root, encoding='unicode', xml_declaration=True)

        return tree


def exportar_dados(export: JSON|XML, data: list):
    try:
        resultado = export.exportar(data)
        print(resultado)
    except:
        print("Erro ao exportar os dados")
