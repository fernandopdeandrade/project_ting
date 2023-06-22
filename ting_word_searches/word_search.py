from ting_file_management.file_process import process
from ting_file_management.queue import Queue

import os

PWD = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PWD)
arq = f"{BASE_DIR}/statics/arquivo_teste.txt"
arq2 = f"{BASE_DIR}/statics/novo_paradigma_globalizado.txt"
arq3 = f"{BASE_DIR}/statics/novo_paradigma_globalizado-min.txt"


occurrences = list()
dir_file = list()


def check_word(word):
    if word == "":
        raise ValueError("Precisa ser informado uma palavra para a busca")


def aux_word(word, instance):
    check_word(word)
    result_search_list = list()

    for element in range(0, (instance.__len__())):
        search_element = instance.search(element)
        res = list()

        for element in range(0, search_element["qtd_linhas"]):
            text_line = search_element["linhas_do_arquivo"][element]

            if word.lower() in text_line.lower():
                res.append({"linha": (element + 1)})
                occurrences.append(
                    {"linha": (element + 1), "conteudo": text_line}
                )

        if len(res) > 0:
            dir_file.append(search_element["nome_do_arquivo"])

            new_info_list = {
                "palavra": word,
                "arquivo": search_element["nome_do_arquivo"],
                "ocorrencias": res,
            }

            result_search_list.append(new_info_list)

    return result_search_list


def exists_word(word, instance):
    check_word(word)
    result_aux = aux_word(word, instance)

    return result_aux


def search_by_word(word, instance):
    check_word(word)
    result_aux = aux_word(word, instance)

    return result_aux


if __name__ == "__main__":
    project = Queue()
    process(arq, project)

    yes_or_no_exists = exists_word("de", project)
    print(f"O resultado da busca exists_word é: {yes_or_no_exists}")

    yes_or_no_search = search_by_word("de", project)
    print(f"O resultado da busca search_by_word é: {yes_or_no_search}")

    print(f"Ocorrencias: {occurrences}")
    print(f"Arquivo: {dir_file[0]}")
