def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada, visse!")
    else:
        print("\nTarefas cadastradas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✅" if tarefa['concluida'] else "❌"
            print(f"{i}. {tarefa['descricao']} - {status}")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({'descricao': descricao, 'concluida': False})
    print("Tarefa adicionada com sucesso!")

def concluir_tarefa(tarefas):
    exibir_tarefas(tarefas)
    try:
        numero = int(input("Digite o número da tarefa concluída: "))
        tarefas[numero - 1]['concluida'] = True
        print("Tarefa marcada como concluída! Parabéns, cabra trabalhador!")
    except (ValueError, IndexError):
        print("Ôxe, número inválido, visse?")

def gerenciador_tarefas():
    tarefas = []

    while True:
        print("\n===== MENU =====")
        print("1. Exibir tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            print("Oxente, saindo do programa... Até mais, cabra arretado!")
            break
        else:
            print("Eita! Opção inválida, tente de novo.")

gerenciador_tarefas()
