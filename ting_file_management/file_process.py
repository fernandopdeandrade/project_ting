import sys
from ting_file_management.file_management import txt_importer as ti


def process(path_file, instance):
    info_instance = ti(path_file)

    if instance.__len__() != 0:
        for i in range(0, (instance.__len__())):
            if instance.search(i)["nome_do_arquivo"] == path_file:
                return

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(info_instance),
        "linhas_do_arquivo": info_instance,
    }

    instance.enqueue(new_dict)

    return print(new_dict, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        message = "Não há elementos"
        return print(message, file=sys.stdout)

    FIFO = instance.search(0)
    path_file = FIFO["nome_do_arquivo"]
    message = f"Arquivo {path_file} removido com sucesso"
    instance.dequeue()

    return print(message, file=sys.stdout)


def file_metadata(instance, position):
    message_position = "Posição inválida"

    try:
        index_file = instance.search(position)
        return print(index_file, file=sys.stdout)

    except IndexError:
        message_position

        return print(message_position, file=sys.stderr)
