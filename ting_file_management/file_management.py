import sys

""" import os

PWD = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PWD)
arq = f"{BASE_DIR}/statics/arquivo_teste.txt"
arq2 = f"{BASE_DIR}/statics/novo_paradigma_globalizado.txt"
arq3 = f"{BASE_DIR}/statics/novo_paradigma_globalizado-min.txt" """


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                return file.read().split("\n")

        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print("Formato inválido", file=sys.stderr)


""" if __name__ == "__main__":
    print(txt_importer(arq))
    print(txt_importer(arq2))
    print(txt_importer(arq3)) """
