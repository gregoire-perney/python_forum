from abc import ABC


class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        pass
