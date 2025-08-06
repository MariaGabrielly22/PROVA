lista = []
print(f"Lista inicial: {lista}")

lista.append("Me Desbloqueia Aí")
lista.append("MULHER SEGURA")
lista.append("Ilha")
lista.append("Amor Teimado")
lista.append("Solteirou")
lista.append("Deja Vu")
lista.append("Abalo Emocional")
lista.append("Ambição")
print(f"Lista com 8 registros: {lista}")

del lista[5]
lista.insert(1, "Coração Cigano")
lista.insert(3, "Erro Planejado")
print(f"Lista após adicionar em posições específicas: {lista}")

registro_removido = lista.pop(5)
print(f"Registro da posição 5 removido ('{registro_removido}'): {lista}")

ultimo_registro = lista.pop()
print(f"Último registro removido ('{ultimo_registro}'): {lista}")
