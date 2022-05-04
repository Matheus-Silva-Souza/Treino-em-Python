#solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
#o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49)
#depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
#O sistema deve calcular e exibir a média de cada uma das metades da sala e
#informar, ao final, qual delas teve a maior nota.

#Introdução ao progama!
print("Olá, por favor comece inserindo as notas dos alunos ímpares abaixo!!")
print("=-=" * 30)


#Criar um input para cada aluno de número ímpar
aluno1 = float(input("Por favor insira a nota do aluno de número 1: "))
print("Nota do aluno 1 foi de {}".format(aluno1))

aluno3 = float(input("Por favor insira a nota do aluno de número 3: "))
print("Nota do aluno 3 foi de {}".format(aluno3))

aluno5 = float(input("Por favor insira a nota do aluno de número 5: "))
print("Nota do aluno 5 foi de {}".format(aluno5))

aluno7 = float(input("Por favor insira a nota do aluno de número 7: "))
print("Nota do aluno 7 foi de {}".format(aluno7))

aluno9 = float(input("Por favor insira a nota do aluno de número 9: "))
print("Nota do aluno 9 foi de {}".format(aluno9))

aluno11 = float(input("Por favor insira a nota do aluno de número 11: "))
print("Nota do aluno 11 foi de {}".format(aluno11))

aluno13 = float(input("Por favor insira a nota do aluno de número 13: "))
print("Nota do aluno 13 foi de {}".format(aluno13))

aluno15 = float(input("Por favor insira a nota do aluno de número 15: "))
print("Nota do aluno 15 foi de {}".format(aluno15))

aluno17 = float(input("Por favor insira a nota do aluno de número 17: "))
print("Nota do aluno 17 foi de {}".format(aluno17))

aluno19 = float(input("Por favor insira a nota do aluno de número 19: "))
print("Nota do aluno 19 foi de {}".format(aluno19))

aluno21 = float(input("Por favor insira a nota do aluno de número 21: "))
print("Nota do aluno 21 foi de {}".format(aluno21))

aluno23 = float(input("Por favor insira a nota do aluno de número 23: "))
print("Nota do aluno 23 foi de {}".format(aluno23))

aluno25 = float(input("Por favor insira a nota do aluno de número 25: "))
print("Nota do aluno 25 foi de {}".format(aluno25))

aluno27 = float(input("Por favor insira a nota do aluno de número 27: "))
print("Nota do aluno 27 foi de {}".format(aluno27))

aluno29 = float(input("Por favor insira a nota do aluno de número 29: "))
print("Nota do aluno 29 foi de {}".format(aluno29))

aluno31 = float(input("Por favor insira a nota do aluno de número 31: "))
print("Nota do aluno 31 foi de {}".format(aluno31))

aluno33 = float(input("Por favor insira a nota do aluno de número 33: "))
print("Nota do aluno 33 foi de {}".format(aluno33))

aluno35 = float(input("Por favor insira a nota do aluno de número 35: "))
print("Nota do aluno 35 foi de {}".format(aluno35))

aluno37 = float(input("Por favor insira a nota do aluno de número 37: "))
print("Nota do aluno 37 foi de {}".format(aluno37))

aluno39 = float(input("Por favor insira a nota do aluno de número 39: "))
print("Nota do aluno 39 foi de {}".format(aluno39))

aluno41 = float(input("Por favor insira a nota do aluno de número 41: "))
print("Nota do aluno 41 foi de {}".format(aluno41))

aluno43 = float(input("Por favor insira a nota do aluno de número 43: "))
print("Nota do aluno 43 foi de {}".format(aluno43))

aluno45 = float(input("Por favor insira a nota do aluno de número 45: "))
print("Nota do aluno 45 foi de {}".format(aluno45))

aluno47 = float(input("Por favor insira a nota do aluno de número 47: "))
print("Nota do aluno 47 foi de {}".format(aluno47))

aluno49 = float(input("Por favor insira a nota do aluno de número 49: "))
print("Nota do aluno 49 foi de {}".format(aluno49))

print("=-=" * 20)

#agora criar uma soma de média para todos os alunos ímpares.
total_impares = (float(aluno1) + float(aluno3) + float(aluno5) + float(aluno7) + float(aluno9) + float(aluno11) + float(aluno13) + float(aluno15) + float(aluno17) + float(aluno19) + float(aluno21) + float(aluno23) + float(aluno25) + float(aluno27) + float(aluno29) + float(aluno31) + float(aluno33) + float(aluno35) + float(aluno37) + float(aluno39) + float(aluno41) + float(aluno43) + float(aluno45) + float(aluno47) + float(aluno49))
print("O total de notas dos alunos ímpares é de {:.1f}" .format(total_impares))
media_impares = total_impares / 2
print("A média dos alunos ímpares é de {:.1f}".format(media_impares))

print("=-=" * 30)



#agora devemos criar um sistema para contabilizar nota dos alunos pares!
print("Muito bem! Agora por favor insira a nota dos alunos de número par abaixo!!")

print("=-=" * 30)


aluno2 = float(input("Por favor insira a nota do aluno de número 2: "))
print("Nota do aluno 2 foi de {}".format(aluno2))

aluno4 = float(input("Por favor insira a nota do aluno de número 4: "))
print("Nota do aluno 4 foi de {}".format(aluno4))

aluno6 = float(input("Por favor insira a nota do aluno de número 6: "))
print("Nota do aluno 6 foi de {}".format(aluno6))

aluno8 = float(input("Por favor insira a nota do aluno de número 8: "))
print("Nota do aluno 8 foi de {}".format(aluno8))

aluno10 = float(input("Por favor insira a nota do aluno de número 10: "))
print("Nota do aluno 10 foi de {}".format(aluno10))

aluno12 = float(input("Por favor insira a nota do aluno de número 12: "))
print("Nota do aluno 12 foi de {}".format(aluno12))

aluno14 = float(input("Por favor insira a nota do aluno de número 14: "))
print("Nota do aluno 14 foi de {}".format(aluno14))

aluno16 = float(input("Por favor insira a nota do aluno de número 16: "))
print("Nota do aluno 16 foi de {}".format(aluno16))

aluno18 = float(input("Por favor insira a nota do aluno de número 18: "))
print("Nota do aluno 18 foi de {}".format(aluno18))

aluno20 = float(input("Por favor insira a nota do aluno de número 20: "))
print("Nota do aluno 20 foi de {}".format(aluno20))

aluno22 = float(input("Por favor insira a nota do aluno de número 22: "))
print("Nota do aluno 22 foi de {}".format(aluno22))

aluno24 = float(input("Por favor insira a nota do aluno de número 24: "))
print("Nota do aluno 24 foi de {}".format(aluno24))

aluno26 = float(input("Por favor insira a nota do aluno de número 25: "))
print("Nota do aluno 25 foi de {}".format(aluno26))

aluno28 = float(input("Por favor insira a nota do aluno de número 28: "))
print("Nota do aluno 28 foi de {}".format(aluno28))

aluno30 = float(input("Por favor insira a nota do aluno de número 30: "))
print("Nota do aluno 30 foi de {}".format(aluno30))

aluno32 = float(input("Por favor insira a nota do aluno de número 32: "))
print("Nota do aluno 32 foi de {}".format(aluno32))

aluno34 = float(input("Por favor insira a nota do aluno de número 34: "))
print("Nota do aluno 34 foi de {}".format(aluno34))

aluno36 = float(input("Por favor insira a nota do aluno de número 36: "))
print("Nota do aluno 36 foi de {}".format(aluno36))

aluno38 = float(input("Por favor insira a nota do aluno de número 38: "))
print("Nota do aluno 38 foi de {}".format(aluno38))

aluno40 = float(input("Por favor insira a nota do aluno de número 40: "))
print("Nota do aluno 40 foi de {}".format(aluno39))

aluno42 = float(input("Por favor insira a nota do aluno de número 42: "))
print("Nota do aluno 42 foi de {}".format(aluno43))

aluno44 = float(input("Por favor insira a nota do aluno de número 44: "))
print("Nota do aluno 44 foi de {}".format(aluno44))

aluno46 = float(input("Por favor insira a nota do aluno de número 46: "))
print("Nota do aluno 46 foi de {}".format(aluno46))

aluno48 = float(input("Por favor insira a nota do aluno de número 48: "))
print("Nota do aluno 48 foi de {}".format(aluno48))

aluno50 = float(input("Por favor insira a nota do aluno de número 50: "))
print("Nota do aluno 49 foi de {}".format(aluno50))

print("=-=" * 30)

#agora criar uma soma de média para todos os alunos pares.
total_pares = (float(aluno2) + float(aluno4) + float(aluno6) + float(aluno8) + float(aluno10) + float(aluno12) + float(aluno14) + float(aluno16) + float(aluno18) + float(aluno20) + float(aluno22) + float(aluno24) + float(aluno26) + float(aluno28) + float(aluno30) + float(aluno32) + float(aluno34) + float(aluno36) + float(aluno38) + float(aluno40) + float(aluno42) + float(aluno44) + float(aluno46) + float(aluno49) + float(aluno50))
print("O total de notas dos alunos pares é de {:.1f}" .format(total_impares))
media_pares = total_pares / 2
print("A média dos alunos ímpares é de {:.1f}".format(media_pares))

print("=-=" * 30)

print("Muito bem! Agora vamos ver qual foi a turma que teve a maior média.")

#agora criar o calculo de qual lado tem a média de notas maior.
media_total = max(media_pares,media_impares)
print("A turma que teve a maior média foi {} ".format(media_total))
if media_total == media_impares:
    print("A turma de números ímpares teve a maior média de: {} ".format(media_impares))
else:
    if media_total == media_pares:
        print("A turma de números pares teve a maior média de: {} ".format(media_pares))
5.5





