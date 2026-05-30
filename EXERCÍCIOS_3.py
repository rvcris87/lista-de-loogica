estoque = int(input("Digite a quantidade inicial em estoque: "))
total_retirado = 0
quantidade_vendas = 0
retirada = int(input("Digite a quantidade retirada ou 0 para encerrar: "))

while retirada != 0:
    if retirada > estoque:
        print("Não há estoque suficiente para essa retirada.")
    else:
        estoque -= retirada
        total_retirado += retirada
        quantidade_vendas += 1

        if estoque == 0:
            print("Estoque esgotado.")
            break
        elif estoque < 10:
            print("Estoque baixo.")

    retirada = int(input("Digite a quantidade retirada ou 0 para encerrar: "))

print("\n--- Resultado Final ---")
print(f"Estoque restante: {estoque}")
print(f"Total retirado: {total_retirado}")
print(f"Quantidade de vendas: {quantidade_vendas}")