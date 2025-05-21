# Durante a Semana da Ciência e Tecnologia, uma escola organizou uma competição entre quatro projetos estudantis: Robótica, Astronomia, Biologia e Química. Cada projeto foi avaliado por um júri, recebendo uma nota inteira de 0 a 10.

a_danca = int(input('Qual nota você daria à apresentação de Dança? '))
a_musica = int(input('Qual nota você daria à apresentação de Música? '))
o_teatro = int(input('Qual nota você daria à apresentação de Teatro? '))

maior_voto = max(a_danca, a_musica, o_teatro)
vencedor = []

if a_danca == maior_voto:
    vencedor.append('Dança')
if a_musica == maior_voto:
    vencedor.append('Música')
if o_teatro == maior_voto:
    vencedor.append('Teatro')

if len(vencedor) == 1:
    print(f"A apresentação favorita do público foi {vencedor[0]}! Uma salva de palmas para a vencedora!")

elif len(vencedor) == 2:
    print(f"Houve um empate técnico! As apresentações de {vencedor[0]} e {vencedor[1]} foram as favoritas do público!")

else:
    print("Isso é inesperado, porém todas as apresentações empataram com a mesma quantidade de votos!")
