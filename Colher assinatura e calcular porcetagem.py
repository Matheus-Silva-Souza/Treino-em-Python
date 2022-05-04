#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente
#O faturamento anual dele
#E que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
#A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
#Nível Porcentagem sobre o faturamento
#Basic 30%
#Silver 20%
#Gold 10%
#Platinum 5%

print("Selecione uma opção abaixo que corresponde a assinatura do cliente !")

#tabela de seleção para receber o tipo de assinatura do cliente
print('''[1] Platinum
[2] Gold
[3] Silver
[4] Basic''')
op = int(input(">>>>>Por favor selecione a assinatura do cliente: "))

#4 opções de plano para selecionar o cliente deve escolher qual o plano dele.
#um print para dizer qual foi selecionada, em sequência o faturamento anual e o cliente após digitalo sairá o resultado.

if op == 1:
    print("Assinatura Platinum selecionada !")
    f_anual = float(input("Por favor, insira o seu faturamento anual R$: "))
    bonus = f_anual * 5 / 100
    print("O valor bônus que o cliente deverá pagar é de R$: {:.2f} ".format(bonus))

elif op == 2:
    print("Assinatura gold selecionada! ")
    f_anual = float(input("Por favor, insira o seu faturamento anual R$: "))
    bonus = f_anual * 10 / 100
    print("O valor bônus que o cliente deverá pagar é de R$: {:.2f}".format(bonus))

elif op == 3:
    print("Assinatura Silver selecionada !")
    f_anual = float(input("Por favor, insira o seu faturamento anual R$: "))
    bonus = f_anual * 20 / 100
    print("O valor bônus que o cliente deverá pagar é de R$: {:.2f}".format(bonus))

elif op == 4:
    print("Assinatura Basic selecionada !")
    f_anual = float(input("Por favor, insira o seu faturamento anual R$: "))
    bonus = f_anual * 30 / 100
    print("O valor bônus que o cliente deverá pagar é de R$: {:.2f}".format(bonus))

#o progama repete a formula para todos os planos alterando apenas o valor de porcentagem.

