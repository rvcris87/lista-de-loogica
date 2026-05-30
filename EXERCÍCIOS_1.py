total_vendido = 0
quantidade_vendas = 0
vendas_baixas = 0
vendas_medias = 0
vendas_altas = 0

venda = float(input("Digite o valor da venda ou 0 para encerrar: "))

while venda != 0:
    total_vendido += venda
    quantidade_vendas += 1

    if venda <= 100:
        vendas_baixas += 1
    elif venda <= 500:
        vendas_medias += 1
    else:
        vendas_altas += 1

    venda = float(input("Digite o valor da venda ou 0 para encerrar: "))

print("\n--- Resultado Final ---")
print(f"Total vendido: R$ {total_vendido:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Vendas baixas: {vendas_baixas}")
print(f"Vendas médias: {vendas_medias}")
print(f"Vendas altas: {vendas_altas}")