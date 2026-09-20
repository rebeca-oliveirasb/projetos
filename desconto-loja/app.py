# Entrada de dados
valor_compra = float(input("Digite o valor total da compra: "))

# Processamento e saída de dados
""" O programa calcula o desconto com base no valor da compra inserido pelo usuário e o aplica a esse valor;
Na saída, exibe o desconto aplicado e o novo total a ser pago. """
if valor_compra < 200:
    desconto = 0.05 * valor_compra
    print(f"""
    Desconto de 5% aplicado ao valor da sua compra: R${desconto:.2f}
    Total a ser pago: R${valor_compra - desconto:.2f}""")
elif 200 <= valor_compra <300:
    desconto = 0.10 * valor_compra
    print(f"""
    Desconto de 10% aplicado ao valor da sua compra: R${desconto:.2f}
    Total a ser pago: R${valor_compra - desconto:.2f}""")
elif valor_compra >= 300:
    desconto = 0.15 * valor_compra
    print(f"""
    Desconto de 15% aplicado ao valor da sua compra: R${desconto:.2f}
    Total a ser pago: R${valor_compra - desconto:.2f}""")
