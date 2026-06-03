import gerenciador
import menu
import validacoes
def main():
    g = gerenciador.Gerenciamento()
    while True:
        escolha = menu.opcoes()
        if not validacoes.validar(escolha):
            print("Opção inválida, tente novamente.")
            continue
        if escolha == "1":
            descricao = input("Descrição da tarefa: ")
            g.adicionar_tarefa(descricao)
        elif escolha == "2":
            g.listar_tarefas()
        elif escolha == "3":
            indice = (input("Número da tarefa concluída: "))
            if not validacoes.validar_indice((indice), len(g.tarefas)):
                print("Índice inválido, tente novamente.")
                continue
            g.concluir_tarefa(int(indice))
        elif escolha == "4":
            indice = (input("Número da tarefa que deseja excluir: "))
            if not validacoes.validar_indice((indice), len(g.tarefas)):
                print("Índice inválido, tente novamente.")
                continue
            g.excluir_tarefa(int(indice))
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()