idade = 0
quantidade = 0
idadeMaisVelho = 0
idadeMaisNovo = 0
prefCachorro = 0
prefGato = 0
prefCoelho = 0
velhoPrefCachorro = 0
velhoPrefGato = 0
velhoPrefCoelho = 0
novoPrefCachorro = 0
novoPrefGato = 0
novoPrefCoelho = 0
HPrefCachorro = 0
HPrefGato = 0
HPrefCoelho = 0
MPrefCachorro = 0
MPrefGato = 0
MPrefCoelho = 0


while (True):

    idade = int(input("Qual é a sua idade?"))
    sexo = int(input("Qual o seu sexo?(1-M, 2-F)"))
    animalpref = int(input("Qual o seu animal preferido?(1-Cachorro, 2-Gato, 3-Coelho)"))

    quantidade += 1

    if  animalpref == 1:
        prefCachorro += 1
    if  animalpref == 2:
        prefGato += 1
    if  animalpref == 3:
        prefCoelho += 1


    if (idade > velhoPrefCachorro) and (animalpref == 1):
        velhoPrefCachorro = idade
    if (idade > velhoPrefGato) and (animalpref == 2):
        velhoPrefGato = idade
    if (idade > velhoPrefCoelho) and (animalpref == 3):
        velhoPrefCoelho = idade
    

    if (animalpref == 1) and (idade < novoPrefCachorro) or (novoPrefCachorro == 0):
        novoPrefCachorro = idade
    if (animalpref == 2) and (idade < novoPrefGato) or (novoPrefGato == 0):
        novoPrefGato = idade
    if (animalpref == 3) and (idade < novoPrefCoelho) or (novoPrefCoelho == 0):
        novoPrefCoelho = idade


    if (animalpref == 1) and (sexo == 1):
        HPrefCachorro += 1
    if (animalpref == 2) and (sexo == 1):
        HPrefGato += 1
    if (animalpref == 3) and (sexo == 1):
        HPrefCoelho += 1


    if (animalpref == 1) and (sexo == 2):
        MPrefCachorro += 1
    if (animalpref == 2) and (sexo == 2):
        MPrefGato += 1
    if (animalpref == 3) and (sexo == 2):
        MPrefCoelho += 1


    continua = int(input("Você deseja continuar?(1-Sim, 2-Não)"))
    if continua == 2:
        break

print("Quantidade de respondentes:", quantidade)
print("Porcentagem de pessoas que preferem cachorro:", (prefCachorro/quantidade)*100)
print("Porcentagem de pessoas que preferem gato:", (prefGato/quantidade)*100)
print("Porcentagem de pessoas que preferem coelho:", (prefCoelho/quantidade)*100)
print("A idade do mais velho que prefere cachorro é:", velhoPrefCachorro)
print("A idade do mais velho que prefere Gato é:", velhoPrefGato)
print("A idade do mais velho que prefere Coelho é:", velhoPrefCoelho)
print("A idade do mais novo que prefere cachorro é:", novoPrefCachorro)
print("A idade do mais novo que prefere Gato é:", novoPrefGato)
print("A idade do mais novo que prefere Coelho é:", novoPrefCoelho)
print("A Quantidade de homens que preferem cachorro é:", HPrefCachorro)
print("A Quantidade de homens que preferem gato é:", HPrefGato)
print("A Quantidade de homens que preferem coelho é:", HPrefCoelho)
print("A Quantidade de mulheres que preferem cachorro é:", MPrefCachorro)
print("A Quantidade de mulheres que preferem gato é:", MPrefGato)
print("A Quantidade de mulheres que preferem coelho é:", MPrefCoelho)







