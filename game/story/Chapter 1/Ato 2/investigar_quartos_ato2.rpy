label investigar_quartos_ato2:

    if all_rooms == True or (quarto_anthony == True):
        a "Certo..."
        jump quarto_anna
    else:
        if first_room == True:
            a "Certo..."
            a "Como eu começo?"
        else:
            a "E agora?"

        menu:
            "Quarto de Miguel" if quarto_miguel == False:
                $ first_room = False
                $ quartos_miguel = True
                jump quarto_miguel
            "Quarto de Sophie" if quarto_sophie == False:
                $ quarto_sophie = True
                $ inventario.add_item(teste_gravidez)
                $ first_room = False
                jump quarto_sophie
            "Quarto de Anthony" if quarto_anthony == False:
                $ quarto_anthony = True
                $ inventario.add_item(frasco_de_vidro)
                $ first_room = False
                jump quarto_anthony
            "Voltar" if quarto_miguel == False and quarto_sophie == False and quarto_anthony == False:
                jump falar_veronica_ato2p2
            "Investigar no quarto de Anna" if all_rooms == True or quarto_anthony == True:
                jump quarto_anna

label quarto_miguel:
    a "Vamos ver o quarto de Miguel."
    a "Com certeza tem algo lá que pode me ajudar."

    "Anna vai até o quarto de Miguel."
    scene corredor

    "Na porta do quarto de Miguel, Anna percebe que a porta está entreaberta."
    "Mas os seguranças estão lá dentro."

    a "{i}Como eu vou entrar?{/i}"
    a "{i}Preciso de uma distração...{/i}"
    a "{i}Mas não tenho tempo, vou tentar de novo depois.{/i}"

    jump investigar_quartos_ato2

label quarto_sophie:
    a "Vamos ver o quarto de Sophie."
    a "Com certeza tem algo lá que pode me ajudar."

    "Anna vai até o quarto de Sophie."
    scene corredor

    "A porta do quarto de Sophie está destrancada."
    "Anna entra no quarto e começa a procurar por alguma pista."
    scene quarto_suite
    with dissolve
    a "{i}O que eu posso encontrar aqui?{/i}"
    a "Ah, o que é isso?"

    "Anna encontra um teste de gravidez no lixo."

    menu:
        "Pegar":
            a "Isso pode ser útil."
            jump investigar_quartos_ato2
        "Deixar":
            jump investigar_quartos_ato2
        "Verificar":
            a "{i}É um teste positivo de gravidez...{/i}"
            a "{i}Sophie está grávida?{/i}"
            jump investigar_quartos_ato2

    jump investigar_quartos_ato2

label quarto_anthony:
    a "Vamos ver o quarto de Anthony."
    a "Com certeza tem algo lá que pode me ajudar."

    "Anna vai até o quarto de Anthony."
    scene corredor
    with dissolve

    "A porta do quarto de Anthony está destrancada."
    "Anna entra no quarto e começa a procurar por alguma pista."
    scene quarto_suite
    with dissolve

    "Ela encontra um frasco de vidro sobre a mesa de cabeceira."

    a "{i}O que é isso?{/i}"

    menu:
        "Pegar":
            a "Isso pode ser útil."
            pass
        "Deixar":
            a "Isso não parece ser importante."
            pass
        "Verificar":
            a "{i}Um frasco de vidro...{/i}"
            pass
    
    "Anna só pode ficar mais alguns minutos no quarto de Anthony."
    "O que Anna deve fazer?"

    menu:
        "Verificar gavetas":
            $ inventario.add_item(nota_fiscal)
            a "Vamos ver o que tem nas gavetas."
            "Ela encontra uma nota fiscal amassada."
            pass
        "Verificar armário":
            a "Vamos ver o que tem no armário."
            "O armário só tem algumas roupas chiques e ternos pretos."
            "Também tem uma coleção de gravatas."
            pass
        "Verificar cama":
            a "Vamos ver o que tem embaixo da cama."
            "Anna não encontra nada de interessante."
            pass
        "Verificar banheiro":
            a "Vamos ver o que tem no banheiro."
            "O banheiro está limpo e organizado."
            a "Não tem nada de interessante..."
            pass

    jump investigar_quartos_ato2

label quarto_anna:
    a "Preciso de um tempo para pensar."
    a "Vou para o meu quarto."

    scene quarto_suite
    with fade

    "Anna entra no quarto e fecha a porta."
    "Ela se joga na cama e tenta organizar seus pensamentos."

    a "{i}O que eu faço agora?{/i}"
    a "{i}Será que eu devo contar para alguém?{/i}"

    "Anna toma um tempo e se prepara."

    a "Já sei o que fazer."

    "Ela separa um tempo para imprimir as fotos dos suspeitos."
    "Anna decide montar um mapa mental na sua parede com as fotos e alguns post-its."

    a "{i}Agora eu posso ver tudo de uma vez{/i}"

    "Anna passa a noite organizando as informações que conseguiu."

    "No dia seguinte, ela está pronta para continuar a investigação."