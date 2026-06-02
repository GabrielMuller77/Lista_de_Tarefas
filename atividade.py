class Tarefa():

    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False


    def concluir(self):
        self.concluida = True

    
    def __str__(self):
            if self.concluida == True:
                status = f'[X] {self.descricao}'
            else:
                status = f'[ ] {self.descricao}'
            return status