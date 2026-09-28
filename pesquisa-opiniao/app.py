# Entrada e processamento
excelentes = 0
ruins = 0
for i in range(50):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    opinião = input("Dê sua opinião sobre nosso atendimento, sendo 1 para excelente, 2 para bom e 3 para ruim: ")
    if opinião == "1":
        excelentes = excelentes + 1
    elif opinião == "3":
        ruins = ruins + 1

# Saída
print(f"Quantidade de opiniões excelentes: {excelentes}")
print(f"Quantidade de opiniões ruins: {ruins}")