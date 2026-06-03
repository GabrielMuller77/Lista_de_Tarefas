import json
import atividade
def salvar_tarefas(tarefas, nome_arquivo="tarefas.json"):
    dados = []
    for tarefa in tarefas:
        dados.append({
            "descricao": tarefa.descricao,
            "concluida": tarefa.concluida,
            "data": tarefa.data
        })
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_tarefas(nome_arquivo="tarefas.json"):
    tarefas = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for item in dados:
                tarefa = atividade.Tarefa(item["descricao"])
                tarefa.concluida = item["concluida"]
                tarefa.data = item["data"]
                tarefas.append(tarefa)
            return tarefas
    except FileNotFoundError:
        return []