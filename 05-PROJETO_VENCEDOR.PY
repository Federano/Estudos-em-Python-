# Durante a Semana da Ciência e Tecnologia, uma escola organizou uma competição entre quatro projetos estudantis: robótica, astronomia, biologia e química. Cada projeto foi avaliado por um júri, recebendo uma nota inteira de 0 a 10.

robotica = int(input('Qual nota o júri dará à equipe de robótica? '))
astronomia = int(input('Qual nota o júri dará à equipe de astronomia? '))
biologia = int(input('Qual nota o júri dará à equipe de biologia? '))
quimica = int(input('Qual nota o júri dará à equipe de química? '))

maior_voto = max(robotica, astronomia, biologia, quimica)
maior_nota = []

if robotica == maior_voto:
    maior_nota.append('robótica')
if astronomia == maior_voto:
    maior_nota.append('astronomia')
if biologia == maior_voto:
    maior_nota.append('biologia')
if quimica == maior_voto:
    maior_nota.append('química')        

if len(maior_nota) == 1:
    print(f"O projeto ganhador da competição foi o de {maior_nota[0]}!")

elif len(maior_nota) == 2:
    print(f"Houve um empate técnico nos projetos, os vencedores são as apresentações de {maior_nota[0]} e {maior_nota[1]}, que foram as favoritas do júri!")

else:
    print("Isso é inesperado, porém todas as apresentações empataram com a mesma quantidade de votos!")
