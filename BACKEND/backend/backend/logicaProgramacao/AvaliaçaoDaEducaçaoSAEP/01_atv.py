<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Kanban de Tarefas - SENAI</title>
    <link rel="stylesheet" href="simulado.css"
</head>
<body>

    <h1>Kanban de Tarefas - SENAI</h1>

    <form id="taskForm">
        <h2>Cadastrar Tarefa</h2>
        
        <label for="usuario">Nome do Usuário:</label>
        <input type="text" id="usuario" required>

        <label for="nomeTarefa">Nome da Tarefa:</label>
        <input type="text" id="nomeTarefa" required>

        <label for="setor">Setor:</label>
        <input type="text" id="setor" required>

        <label for="prioridade">Prioridade:</label>
        <select id="prioridade" required>
            <option value="">Selecione</option>
            <option value="Baixa">Baixa</option>
            <option value="Média">Média</option>
            <option value="Alta">Alta</option>
        </select>

        <label for="data">Data:</label>
        <input type="date" id="data" required>

        <label for="status">Status:</label>
        <select id="status" required>
            <option value="aFazer">A Fazer</option>
            <option value="fazendo">Fazendo</option>
            <option value="pronto">Pronto</option>
        </select>

        <button type="submit">Adicionar Tarefa</button>
    </form>

    <div class="kanban-board">
        <div class="column" id="aFazer">
            <h3>A Fazer</h3>
        </div>
        <div class="column" id="fazendo">
            <h3>Fazendo</h3>
        </div>
        <div class="column" id="pronto">
            <h3>Pronto</h3>
        </div>
    </div>

    <script src="simulado.js"></script> <!-- Link para o JS externo -->

</body>
</html>