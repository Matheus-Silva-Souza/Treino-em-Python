print("Olá, Por favor insira o valor dos votos em seus respectivos dias da semana! ")

segunda = str(input("Segunda-feria: "))
terca = str(input("Terça-feira: "))
quarta = str(input("Quarta-feira: "))
quinta = str(input("Quinta-feira: "))
sexta = str(input("Sexta-feira: "))
print("=-=" * 10)

segunda = int(segunda)
terca = int(terca)
quarta = int(quarta)
quinta = int(quinta)
sexta = int(sexta)
print("=-=" * 10)


mais_votado = max(segunda,terca,quarta,quinta,sexta)
print("O dia que recebeu a maior quantidade de votos foi: {}! ".format(mais_votado))
if segunda == mais_votado:
    print("Segunda-feira foi o dia mais votado e será o novo dia das lives! ")
else:
    if terca == mais_votado:
        print("Terça-feira foi o dia mais votado e será o novo dia das lives! ")
    else:
        if quarta == mais_votado:
         print("Quarta-feira foi o dia mais votado, será o novo dia das lives! ")
        else:
            if quinta == mais_votado:
             print("Quinta-feira foi o dia mais votado, será o novo dia das lives! ")
            else:
                if sexta == mais_votado:
                 print("Sexta-feira foi o dia mais votado, será o novo dia das lives! ")














