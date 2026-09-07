# Entrada de dados
nome_do_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho, em watts: "))
tempo_de_uso = float(input("Digite o tempo médio de uso diário, em horas: "))

# Processamento
consumo_mensal = (potencia * tempo_de_uso * 30) / 1000
custo_estimado = consumo_mensal * 0.75

# Saída
print(f"Aparelho: {nome_do_aparelho}")
print(f"O consumo mensal é de {consumo_mensal: .2f} kWh/mês.")
print(f"O custo mensal estimado é de R$ {custo_estimado: .2f}.")
