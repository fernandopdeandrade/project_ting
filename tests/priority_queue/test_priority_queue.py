import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()

    assert len(queue) == 0

    insert = [
        {"qtd_linhas": 4, "nome_do_arquivo": "file1.txt"},
        {"qtd_linhas": 5, "nome_do_arquivo": "file2.txt"},
        {"qtd_linhas": 6, "nome_do_arquivo": "file3.txt"},
    ]

    for item in insert:
        queue.enqueue(item)

    assert len(queue) == 3

    assert queue.search(0) == insert[0]
    assert queue.search(1) == insert[1]
    assert queue.search(2) == insert[2]

    assert queue.dequeue() == insert[0]
    assert queue.dequeue() == insert[1]
    assert len(queue) == 1

    assert queue.is_priority(insert[0]) is True
    assert queue.is_priority(insert[2]) is False
    assert queue.is_priority(insert[1]) is False

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(7)
