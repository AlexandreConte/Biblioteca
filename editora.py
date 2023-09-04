class Editora:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = (None, codigo)[isinstance(codigo, int)]
        self.__nome = (None, nome)[isinstance(nome, str)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
