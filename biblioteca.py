from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            return
        for item in self.__livros:
            if item in self.__livros:
                break
        else:
            self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
