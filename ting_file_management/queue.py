from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []
        self._len = 0

    def __len__(self):
        return self._len

    def enqueue(self, value):
        self._data.append(value)
        self._len += 1

    def dequeue(self):
        if self._len > 0:
            self._len -= 1
            return self._data.pop(0)
        raise IndexError("Fila Vazia")

    def search(self, index):
        if index < 0 or index >= self._len:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]


""" if __name__ == "__main__":
    result = Queue()

    print(f"O tamanho da fila é: {len(result)}")
    print("----------------------------------")
    print("Adicionando elementos na fila...")
    result.enqueue(1)
    result.enqueue(2)
    result.enqueue(3)
    result.enqueue(4)
    result.enqueue(5)
    print("----------------------------------")
    print(f"O tamanho da fila é: {len(result)}")
    print("----------------------------------")
    print("Pesquisando por elementos da fila...")
    print(result.search(3))
    print("----------------------------------")
    print("Removendo elementos da fila...")
    result.dequeue()
    print("----------------------------------")
    print(f"O tamanho da fila é: {len(result)}")
    print("----------------------------------")
    print("Pesquisando por elementos da fila...")
    print(result.search(3))
    print("----------------------------------")
    print("Removendo elementos da fila...")
    result.dequeue()
    print("----------------------------------")
    print(f"O tamanho da fila é: {len(result)}")
    print("----------------------------------")
    print("Pesquisando por elementos da fila que não existem...")
    print(result.search(10))
    print("----------------------------------") """
