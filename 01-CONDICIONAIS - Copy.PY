print('Olá Mundo, como não nasci rico, preciso estudar, então, mão na massa Fernando!')

# Aula 01 - Condicionais no Python
# - As condicionais no Python são comandos que me permitem executar diferentes blocos de código, de acordo com uma condição que pode ser verdadeira ou falsa.

# Condicional if: 
# - A condicional if (expressão): indica ao código que siga esse caminho como primeira opção, sendo o caminho VERDADEIRO que eu quero que o usuário siga, conforme o código abaixo.

# Condicional elif:
# - Esse comando é usado quando tenho mais de uma possibilidade além da principal, ele deve ser usado antes do comando else e serve como um caminho intermediário.

# Condicional else: 
# - É a última opção, o "plano B". Ela será executada se nenhuma das condições anteriores for verdadeira é o caminho para qualquer outra situação que não tenha sido tratada antes.

# Vamos lá, vou fazer o exemplo aqui para ver se eu entendi.
#============================================================================================================================================

nome = input('Digite seu nome: ')  # Aqui estou dizendo ao código que toda vez que aparecer "nome" é por que eu quero o nome Fernando ou Alexandre, detalhe para o comando input que permite a entrada de dados do utilizador num programa

if nome == 'Fernando':  # Estou dizendo ao código que a primeira opção de nome é Fernando.
    print('Olá Fernando, até aqui parece estar tudo bem com o código!')

elif nome == 'Alexandre':  # Aqui estou dizendo ao código que, se não for Fernando mas for Alexandre, ele deve seguir esse caminho.
    print('Eu sei que você colocou Alexandre só para me irritar, mas até aqui, como segunda opção de comando, o código está operando bem!')

else:  # Finalmente a última opção, que será a mensagem de erro para qualquer nome que não seja Fernando ou Alexandre.
    print('Olha, não sei como você conseguiu isso, mas errou o nome!')
