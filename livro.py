from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(
            self,
            codigo: int,
            titulo: str,
            ano: int,
            editora: Editora,
            autor: Autor,
            numero_capitulo: int,
            titulo_capitulo: str
    ):
        self.__codigo = (None, codigo)[isinstance(codigo, int)]
        self.__titulo = (None, titulo)[isinstance(titulo, str)]
        self.__ano = (None, ano)[isinstance(ano, int)]
        self.__editora = (None, editora)[isinstance(editora, Editora)]
        self.__autores = []
        self.__capitulos = []

        if isinstance(
            numero_capitulo,
            int
        ) and isinstance(
            titulo_capitulo,
            str
        ):
            capitulo = Capitulo(numero_capitulo, titulo_capitulo)
            self.__capitulos.append(capitulo)
        if isinstance(autor, Autor):
            self.__autores.append(autor)

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = Editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        if isinstance(numero, int) and isinstance(titulo, str):
            if not self.find_capitulo_by_titulo(titulo):
                self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str):
        if isinstance(titulo, str):
            capitulo = self.find_capitulo_by_titulo(titulo)
            if isinstance(capitulo, Capitulo):
                self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
