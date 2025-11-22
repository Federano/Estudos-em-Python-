# Shift + Alt + A = A MELHOR FUNÇÃO DO MOMENTO. 

""" 
Tive que pôr a função float para garantir que o programa entenda como um número. A função input está ali como uma pergunta para registrar o dado colocado. 
"""
primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

if primeiro_valor > segundo_valor: 
    """
     - if seria a primeira chance de fazer algo para o contexto que eu estou colocando.

     - Sempre tenho que colocar os dois pontos para o código entender que eu terminei de pôr a condição; logo, sempre preciso pôr os dois pontos. 

     - Esse f serve para puxar a informação do user para o campo que eu quero; só preciso pôr ele no começo do print.  

     """ 
    print(f'O primeiro valor: ({primeiro_valor:}) é maior que o segundo valor ({segundo_valor:}).')  

elif segundo_valor > primeiro_valor:
    """
     elif seria a segunda chance de fazer algo para o contexto que eu estou colocando.
    """
    print(f'O segundo valor: ({segundo_valor:}) é maior que o primeiro valor: ({primeiro_valor:}).')

elif primeiro_valor == segundo_valor:
    print(f'O primeiro valor: ({primeiro_valor:}) é igual ao segundo valor: ({segundo_valor:}) por favor, tente novamente com um outro valor.')   

