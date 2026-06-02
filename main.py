import gerenciador
import menu

def main():
    g = gerenciador.Gerenciamento()
    while True:
        escolha = menu.opcoes()
        if escolha == "1":
            descricao = input("Descrição da tarefa: ")
            g.adicionar_tarefa(descricao)
        elif escolha == "2":
            g.listar_tarefas()
        elif escolha == "3":
            indice = int(input("Número da tarefa concluída: "))
            g.concluir_tarefa(indice)
        elif escolha == "4":
            indice = int(input("Número da tarefa que deseja excluir: "))
            g.excluir_tarefa(indice)
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()