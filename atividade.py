from datetime import datetime

class Tarefa():

    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def concluir(self):
        self.concluida = True

    
    def __str__(self):
            if self.concluida == True:
                status = f'[X] {self.descricao}, adicionada em {self.data}'
            else:
                status = f'[ ] {self.descricao}, adicionada em {self.data}'
            return status