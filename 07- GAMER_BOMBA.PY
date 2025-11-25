import time 

print("Para desativar a bomba, você precisa cortar o fio da cor correta.")

# Variáveis - São as informações que eu guardo dentro do programa. 
Cores_erradas = ["Azul", "Rosa" , "Verde"]   
Cor_correta = "Vermelho"
Codigo_de_cancelamento_errado = ["Alfa", "Omega", "Grego"]
Codigo_de_cancelamento_correto = "Delta" 

print("Qual dessas cores na engrenagem da bomba é a cor correta?")
print("""A cor correta para desamar a bomba seria a cor: 
- Azul
- Rosa
- Verde
- Vermelho""") 
tentativa_da_cor = input("Digite a sua resposta: ").strip().title()

if tentativa_da_cor == Cor_correta:
    print(f'O fio cortato foi o fio de cor {(Cor_correta)}, o timer parou temporariamente...')
    time.sleep(3)

    print('Agora que você acertou o fio da cor correta é preciso por o codigo correto no painel da bomba para terminar de desamar a bomba.')
    print("""Qual dos codigo abaixo é o codigo correto para desamar a bomba: 
- Alfa
- Delta
- Omega
- Grego""")
    tentativa_do_codigo = input("Digite a sua resposta: ").strip().title()

    if tentativa_do_codigo == Codigo_de_cancelamento_correto:
        print('BOMBA DESATIVADA. VOCÊ SALVOU O DIA!"')
        time.sleep(2)
        print('AGORA VÁ PARA O BAR BEBER UMA CERVEJA!')
        time.sleep(3)
        print("""
            ( ( (
            ( ( ( ( (
            ( ( ( ( ( (
            ( ( ( ( ( ( (
            ( ( ( ( ( ( ( (
            |^^^^^^^^^^^^^^^^|
            | CERVEJA        |
            |                |  
            |                | 
            |                | 
            |                | 
            |                | 
            |________________|
""")
        time.sleep(2)
        print('A cerveja era ITAIPAVA,talvez fosse melhor ter explodido com a bomba!')
    else:
        print('CÓDIGO INCORRETO! MESMO ACERTANDO O SISTEMA ENTROU EM COLAPSO!')
        time.sleep(1)
        print('A bomba vai explodir em...')
        for contagem in range (1):
            print('Contagem de 5...')
            time.sleep(1)
            print('Contagem de 4...')
            time.sleep(1)
            print('Contagem de 3...')
            time.sleep(1)
            print('Contagem de 2...')
            time.sleep(1)
            print('Contagem de 1...')
            time.sleep(1)
        print("""
    KABUM  KABUM  KABUM
     _._  _ , _ ._ ._    
    (_ ' ( `  )_  .__)   
  ( (  (    )   `)  ) _) 
 (__ (_   (_ . _) _) ,__)
     `~~`\ ' . /`~~`     
          ;   ;          
          /   \          
_________/_ __ \_________
          
    KABUM  KABUM  KABU 
          """)
        time.sleep(1)
        print('Hoje não tem cerveja para você... Você Morreu!')
# TUDO OKAY ATE AQUI

elif tentativa_da_cor in Cores_erradas:
    print(f'O fio cortato foi o fio de cor {tentativa_da_cor},  o timer não parou, pelo contrario, cortou o tempo pela metade!')
    time.sleep(1)
    print('SISTEMA ENTROU EM COLAPSO!NÃO FIQUE PARADO, CORRAR!')
    time.sleep(1)
    print('A bomba vai explodir em...')
    for contagem in range (1):
            print('Contagem de 5...')
            time.sleep(1)
            print('Contagem de 4...')
            time.sleep(1)
            print('Contagem de 3...')
            time.sleep(1)
            print('Contagem de 2...')
            time.sleep(1)
            print('Contagem de 1...')
            time.sleep(1)
            print("""
    KABUM  KABUM  KABUM
     _._  _ , _ ._ ._    
    (_ ' ( `  )_  .__)   
  ( (  (    )   `)  ) _) 
 (__ (_   (_ . _) _) ,__)
     `~~`\ ' . /`~~`     
          ;   ;          
          /   \          
_________/_ __ \_________
          
    KABUM  KABUM  KABU 
          """)
            time.sleep(1)
            print('Hoje não tem cerveja para você... Você Morreu!')

else:
    print("Você tremeu a mão e não cortou fio nenhum...")
    print('A bomba vai explodir em...')
    for contagem in range (1):
            print('Contagem de 5...')
            time.sleep(1)
            print('Contagem de 4...')
            time.sleep(1)
            print('Contagem de 3...')
            time.sleep(1)
            print('Contagem de 2...')
            time.sleep(1)
            print('Contagem de 1...')
            time.sleep(1)
            print("""
    KABUM  KABUM  KABUM
     _._  _ , _ ._ ._    
    (_ ' ( `  )_  .__)   
  ( (  (    )   `)  ) _) 
 (__ (_   (_ . _) _) ,__)
     `~~`\ ' . /`~~`     
          ;   ;          
          /   \          
_________/_ __ \_________
          
    KABUM  KABUM  KABU 
          """)
            time.sleep(1)
            print('Hoje não tem cerveja para você... Você Morreu!')