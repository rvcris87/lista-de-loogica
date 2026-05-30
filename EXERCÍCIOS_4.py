soma_temperaturas = 0
quantidade_temperaturas = 0
dias_frios = 0
dias_agradaveis = 0
dias_quentes = 0
temperatura = float(input("Digite a temperatura ou 999 para encerrar: "))

while temperatura != 999:
    soma_temperaturas += temperatura
    quantidade_temperaturas += 1

    if temperatura < 15:
        dias_frios += 1
    elif temperatura <= 30:
        dias_agradaveis += 1
    else:
        dias_quentes += 1

    temperatura = float(input("Digite a temperatura ou 999 para encerrar: "))

print("\n--- Resultado Final ---")

if quantidade_temperaturas > 0:
    media = soma_temperaturas / quantidade_temperaturas
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("Nenhuma temperatura foi informada.")

print(f"Dias frios: {dias_frios}")
print(f"Dias agradáveis: {dias_agradaveis}")
print(f"Dias quentes: {dias_quentes}")