import atividade
class Gerenciamento():
    def __init__(self):
        self.tarefas = []

    
    def adicionar_tarefa(self, descricao):
        nova_tarefa = atividade.Tarefa(descricao)
        self.tarefas.append(nova_tarefa)


    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. {tarefa.__str__()}")


    def concluir_tarefa(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1].concluir()
        else:
            print("Tarefa inexistente na lista, tente novamente.")

    
    def excluir_tarefa(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas.pop(indice - 1)
        else:
            print("Tarefa inexistente na lista, tente novamente.")
