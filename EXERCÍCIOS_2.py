soma_notas = 0
quantidade_alunos = 0
aprovados = 0
recuperacao = 0
reprovados = 0
nota = float(input("Digite a nota do aluno ou -1 para encerrar: "))

while nota != -1:
    soma_notas += nota
    quantidade_alunos += 1

    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovados += 1

    nota = float(input("Digite a nota do aluno ou -1 para encerrar: "))

print("\n--- Resultado Final ---")

if quantidade_alunos > 0:
    media = soma_notas / quantidade_alunos
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")

print(f"Quantidade de alunos: {quantidade_alunos}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")