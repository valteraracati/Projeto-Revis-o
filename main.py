# Módulo

class Aluno:
    def __init__(self):
        self._nome = ''
        self._matricula = ''
        self._telefone = ''

    def set_nome(self, novo_nome):
        if novo_nome != '':
            self._nome = novo_nome
    
    def get_nome(self):
        return self._nome
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self,matricula):
        if matricula.isalnum() and not matricula.isalpha() and not matricula.isnumeric():
            self._matricula=matricula
        else:
            print("A matrícula deve ser alfanumérica, necessariamente...")
    
    def descreva_aluno(self):
        return f'Nome: {self._nome}\n\
            - Telefone: {self._telefone}\n\
            - Matrícula: {self._matricula}'
    

aluno1 = Aluno()
aluno1.set_nome("Raimundo Valter")
aluno1.matricula = '123a'
print(aluno1.descreva_aluno())