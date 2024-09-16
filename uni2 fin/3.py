tarefas = []

def criar_tarefa(titulo, descricao, prioridade, status):
    global tarefas
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo:
              tarefa['descricao'] = descricao
              tarefa['prioridade'] = prioridade
              tarefa['status'] = status
              return

    tarefas.append(
        {
            'titulo': titulo,
            'descricao': descricao,
            'prioridade': prioridade,
            'status':status
        }
    )


def remover_tarefa(titulos):
    global tarefas

    def remover(titulo):
        global tarefas
        for i, tarefa in enumerate(tarefas):
            if tarefa['titulo'] == titulo:
                tarefas.pop(i)
                return True
        return False


    if not titulos:
        return
    titulo = titulos[0]
    if not remover(titulo):
        print(f"Tarefa '{titulo}' não encontrada.")
    remover_tarefa(titulos[1:])

def atualizar_tarefa(titulo, novo_status=None, nova_prioridade=None):
    global tarefas
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo:
            if novo_status is not None:
               tarefa['status'] = novo_status
            if nova_prioridade is not None:
               tarefa['prioridade'] = nova_prioridade
               return
            print("Tarefa não encontrada")

def buscar_tarefa(titulo):
    global tarefas
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo:
            return tarefa
    print("Tarefa Não encontrada")
    return False

def buscar_tarefa_por_prioridade(prioridade=None):
    global tarefas
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            return tarefa

    print("Não encontrada tarefa com essa prioridade")
    return False



criar_tarefa('Estudar Python', 'Revisar conceitos básicos', 1, 'pendente')
criar_tarefa('Fazer exercícios', 'Completar exercícios do livro', 2, 'em andamento')
criar_tarefa('Comprar groceries', 'Comprar leite e pão', 3, 'pendente')
print("Antes da remoção:", tarefas)
remover_tarefa(['Estudar Python', 'Comprar groceries'])
print("Depois da remoção:", tarefas)
