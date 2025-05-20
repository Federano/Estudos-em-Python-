# 01 - Questão ==========================================================================================================================#
    #Em uma barraca de frutas, são vendidas maçãs e bananas. No final do dia, o vendedor deseja saber qual das duas frutas teve a maior quantidade de vendas
    # Quantidade_de_maca_vendidas = int(input("Qual foi a quantidade de maçãs vendidas:"))

Quantidade_de_bananas_vendidas = int(input("Qual foi a quantidade de bananas vendidas:"))

if Quantidade_de_maca_vendidas > Quantidade_de_bananas_vendidas:
    print('Hoje a fruta mais vendida foi a maçã.')

elif Quantidade_de_maca_vendidas < Quantidade_de_bananas_vendidas:
    print('Hoje a fruta mais vendida foi a banana.')

else:
    print('As maçãs e as bananas foram vendidas na mesma quantidade.')
    
# 02 - Questão ==========================================================================================================================#
    #Uma escola está fazendo uma pesquisa entre os alunos para saber qual bebida eles preferem: suco ou refrigerante.   

Alunos_que_preferem_suco = int(input("Qual foi a quantidade de alunos que preferiram suco?"))

Alunos_que_preferem_refrigerante = int(input("Qual foi a quantidade de alunos que preferiram refrigerante?"))

if Alunos_que_preferem_suco > Alunos_que_preferem_refrigerante:
    print("A maioria dos alunos preferem suco do que refrigerante!")

elif Alunos_que_preferem_refrigerante < Alunos_que_preferem_suco:
    print("A maioria dos alunos preferem refrigerante do que suco!")

