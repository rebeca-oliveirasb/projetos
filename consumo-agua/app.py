# Consumo de água
# Entrada de dados
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ")
consumo_agua = float(input("Digite o consumo mensal de água em metros cúbicos (m³): "))

#Processamento e saída de dados
match tipo_imovel:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")
    case "apartamento" if consumo_agua < 10:
        print("Consumo econômico - excelente consumo de água!")
    case "apartamento" | "casa" if 10 < consumo_agua <= 25:
        print("Consumo moderado - dentro do padrão residencial.")
    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")