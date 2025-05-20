# 01 - Questão ====================================================
# Durante uma eleição estudantil, três candidatos disputaram a presidência do grêmio da escola:
# Ana, Bruno e Fernando. Peça ao usuário para digitar a quantidade de votos recebidos por cada um.

Ana = int(input("Qual foi a quantidade de votos recebidos por Ana? "))
Bruno = int(input("Qual foi a quantidade de votos recebidos por Bruno? "))
Fernando = int(input("Qual foi a quantidade de votos recebidos por Fernando? "))

# Usamos max() para descobrir qual foi o maior número de votos entre os três.
maior_voto = max(Ana, Bruno, Fernando)

# Criamos uma lista vazia para armazenar os nomes de quem alcançou esse maior número.
vencedores = []

# Se o número de votos de Ana for igual ao maior número, adicionamos "Ana" na lista.
if Ana == maior_voto:
    vencedores.append("Ana")

# Se o número de votos de Bruno for igual ao maior número, adicionamos "Bruno" na lista.
if Bruno == maior_voto:
    vencedores.append("Bruno")

# Se o número de votos de Fernando for igual ao maior número, adicionamos "Fernando" na lista.
if Fernando == maior_voto:
    vencedores.append("Fernando")

# Agora verificamos quantos nomes estão na lista "vencedores"
if len(vencedores) == 1:
    # Há apenas um nome → temos um único vencedor.
    print(f"{vencedores[0]} venceu a eleição estudantil com mais votos.")

elif len(vencedores) == 2:
    # Dois nomes na lista → houve empate entre dois candidatos.
    print(f"{vencedores[0]} e {vencedores[1]} empataram com a mesma quantidade de votos!")

else:
    # Três nomes na lista → todos empataram (mesmo número de votos).
    print("Todos os três candidatos empataram com a mesma quantidade de votos. Será necessário uma nova eleição.")
