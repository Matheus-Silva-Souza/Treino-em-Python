#primeiro vamos solicitar os batimentos por minuto (BPM)
bpm = input("Por favor, informe os Batimentos aqui: ")
bpm = int(bpm)
opção = 0
#adicionando uma tabela de seleção para facilitar o cod
print('''[1] Até 2 anos
[2] De 8 anos até 17 anos
[3] Adultos sedentários
[4] Idosos''')
opção = int(input(">>>>>Qual é a sua idade ? Selecione a opção a cima: "))

#funcionalidades da opção 1, ou seja foi selecionado a idade e a mensagem sera dita de acordo com a tabela da saúde
if opção == 120:
#Fala sobre qual opção foi selecionada
    print("Seus batimentos estão dentro da faixa adequada.")

elif int(bpm) < 120:
    print("Seus batimentos estão abaixo da faixa adequada.")

elif int(bpm) > 140:
    print("Seus batimentos esão acima da faixa adequada.")

#funcionalidades da opção 2, ou seja foi selecionado a idade e a mensagem sera dita de acordo com a tabela da saúde
elif opção == 2:
#Fala sobre qual opção foi selecionada
    print("De 8 anos á 17 anos selecionado")
#começando um novo if(condição) para o progama escolher entre qual opção de faixa vc está
elif int(bpm) == 80:
    print("Seus batimentos estão dentro da faixa adequada.")

elif int(bpm) < 80:
    print("Seus batimentos estão abaixo da faixa adequada.")

elif int(bpm) > 10:
    print("Seus batimentos estão acima da faixa adequada.")

#funcionalidades da opção 3, ou seja foi selecionado a idade e a mensagem sera dita de acordo com a tabela da saúde
elif opção == 3:
#Fala sobre qual opção foi selecionada
    print("Adulto Sendetario selecionado")
#começando um novo if(condição) para o progama escolher entre qual opção de faixa vc está
elif int(bpm) == 70:
    print("Seus batimentos estão dentro da faixa adequada.")

elif int(bpm) < 70:
    print("Seus batimentos estão abaixo da faixa adequada.")

elif int(bpm) > 80:
    print("Seus batimentos estão acima da faixa adequada.")

#funcionalidades da opção 4, ou seja foi selecionado a idade e a mensagem sera dita de acordo com a tabela da saúde
elif opção == 4:
#Fala sobre qual opção foi selecionada
    print("Idoso selecionado")
#começando um novo if(condição) para o progama escolher entre qual opção de faixa vc está
elif int(bpm) == 50:
    print("Seus batimentos estão dentro da faixa adequada.")

elif int(bpm) < 50:
    print("Seus batimentos estão abaixo da faixa adequada.")

elif int(bpm) > 60:
    print("Seus batimentos estão acima da faixa adequada.")
























