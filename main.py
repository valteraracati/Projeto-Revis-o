# Módulo

class Aluno:
    def __init__(self):
        self.__nome = ''
        self.__matricula = ''
        self.__telefone = ''

    def set_nome(self, novo_nome):
        if novo_nome != '':
            self.__nome = novo_nome
    
    def get_nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,matricula):
        if matricula.isalnum() and not matricula.isalpha() and not matricula.isnumeric():
            self.__matricula=matricula
        else:
            print("A matrícula deve ser alfanumérica, necessariamente...")
    
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    def descreva_aluno(self):
        return f'Nome: {self.__nome}\n\
            - Telefone: {self.__telefone}\n\
            - Matrícula: {self.__matricula}'

class AlunoExtensionista(Aluno):
    def __init__(self):
        super().__init__()
        self.__nome_curso = ''

    

aluno1 = Aluno()
aluno1.set_nome("Raimundo Valter")
aluno1.matricula = '123a'
aluno1.__telefone = '85 9999 11 22'
print(aluno1.descreva_aluno())

aluno2 = AlunoExtensionista()