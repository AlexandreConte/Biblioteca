class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = (None, numero)[isinstance(numero, int)]
        self.__titulo = (None, titulo)[isinstance(titulo, str)]

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
