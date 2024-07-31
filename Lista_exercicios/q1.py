class ItemBiblioteca:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano, num_pags):
        super().__init__(titulo, autor, ano)
        self.__num_pags = num_pags

class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, ano, edicao):
        super().__init__(titulo, autor, ano)
        self.__edicao = edicao 

class Dvd(ItemBiblioteca):
    def __init__(self, titulo, autor, ano, duracao):
        super().__init__(titulo, autor, ano)
        self.__duracao = duracao


livro1 = Livro("O Alquimista", "Paulo Coelho", 1998, 215)
