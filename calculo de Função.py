#Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso, que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina.
#Ao analisar o código do programa deles, porém, você descobre que a senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha
#se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120).
#Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio.
#ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial.
#Ele deve obrigatoriamente utilizar loop. (condição do exércicio)


#Print para situar o cliente da situação
print("Sua senha está presa dentro de um calculo fatorial, para podermos gerar uma senha precisamos fazer o calculo do o minuto atual!")

#Agora pediremos os minutos atuais da máquina para fazer o calculo fatorial.
minuto_atual = int(input("Insira os minuto atual de sua máquina: "))

#nosso contador será o minuto que o cliente digitar, então vamos criar uma variável que será o número fatorial
contador = minuto_atual
multiplicacao = 1
print("calculando {}! = ".format(contador), end="")

#Para começar pensamos em uma estrutura com o loop WHILE.
#Este loop pega o minuto_atual e faz uam subtração de menos 1 criando assim um loop fatorial.
while contador > 0:
    print("{}".format(contador),end="") #print com o formato end="" para os números não pularem linha
    print(" x " if contador > 1 else " = ", end="")#print para reproduzir o sinal de igual após p loop apresentar os números
    multiplicacao = multiplicacao * contador
    contador -= 1
#por fim a formatação com os resultados da ação fatorial.
print("{}." .format(multiplicacao))
print("A sua senha de liberação será LIBERDADE{}".format(multiplicacao))

