minhas_tarefas = ["Estudar Python", "Fazer exercicios", "Ouvir Luan Santana", "Revisar matéria"]
print(f"Tarefas pendentes: {minhas_tarefas}")

minhas_tarefas.append("Assistir show do Luan")
print(f"Tarefa adicionada: {minhas_tarefas}")

minhas_tarefas.insert(1, "Cantar junto do Luan")
print(f"Tarefa inserida em posição especifica: {minhas_tarefas}")

minhas_tarefas.remove("Ouvir Luan Santana")
print(f"Tarefa 'Ouvir Luan Santana' removida: {minhas_tarefas}")

tarefa_removida = minhas_tarefas.pop() 
print(f"Ultima tarefa removida ('{tarefa_removida}'): {minhas_tarefas}")