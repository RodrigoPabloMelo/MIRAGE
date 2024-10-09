label ato2_parte1:
    window hide
    with dissolve
    scene black
    with fade

    play audio "sfx/veronica_grito.mp3" volume 0.3

    window show
    with dissolve

    "..."

    a "O que foi isso?!"

    "..."
    
    quem """
    Atenção, todos os tripulantes.

    Dirijam-se para o salão principal imediatamente.

    Isto não é um pedido, é uma ordem. Repito.

    Dirijam-se para o salão principal imediatamente.

    Todos os passageiros devem se apresentar e identificar-se no salão principal agora.
    """

    "Outra pessoa parece tomar posse dos auto-falantes"

    quem """
    Acabamos de ser informados de um homicídio nas instalações do cruzeiro, em virtudes das circustâncias, o cruzeiro entrará em estado de quarentena até conseguirmos contato com alguma autoriade.

    Exijo a compreensão e cooperação de todos para que possamos resolver este problema da melhor forma possível.

    A tripulação se desculpa pelo transtorno. Sigam as instruções dos seguranças e mantenham a calma em todo momento.

    Logo mais, mudaremos a rota do cruzeiro e informaremos sobre o que acontecerá a seguir.

    Por hora, todos os passageiros devem se apresentar e identificar-se no salão principal agora.
    """

    a "Oi?!"

    "Anna se levanta, confusa e preocupada."

    a "O que está acontecendo?!"

    scene corredor
    with fade

    "Anna sai do quarto e se depara com um corredor vazio e silencioso."

    a "Onde está todo mundo?"

    "Ela caminha pelo corredor, mas não encontra ninguém."

    a "Será que é verdade? Um homicídio?"

    "Anna sente um arrepio percorrer sua espinha."

    a "Preciso descobrir o que está acontecendo."

    "Ela se apressa em direção ao salão principal."

    scene main_hall
    show t at center
    show s at left
    show v at right
    with dissolve

    a "Todos estão aqui"

    "Anna entra no salão principal e vê todos os passageiros reunidos."

    a "No que eu fui me meter?"

    "Verônica está sentada em um canto do salão, aos prantos, conversando com os seguranças."

    "Anthony está suando frio, perto da escada"

    "Sophie está com uma expressão de choque, olhando para o chão e respirando fundo."

    jump escolha_salao_ato2

    label escolha_salao_ato2:
        if falou_anthony_ato2 == True and falou_sophie_ato2 == True and falou_veronica_ato2 == True:
            $ all_actions_ato2 = True
        
        if all_actions_ato2 == True:
            jump ato_2_parte_2
        else:
            menu:
                "Falar com Verônica" if not(falou_veronica_ato2):
                    $ falou_veronica_ato2 = True
                    jump falar_veronica_ato2

                "Falar com Anthony" if not(falou_anthony_ato2):
                    $ falou_anthony_ato2 = True
                    jump falar_anthony_ato2

                "Falar com Sophie" if not(falou_sophie_ato2):
                    $ falou_sophie_ato2 = True
                    jump falar_sophie_ato2

label falar_veronica_ato2:
    a "Verônica...?"

    "Verônica parece estar em estado de choque absoluto."
    "Ela não responde, parece não escutar nada do que está acontecendo ao seu redor."

    jump escolha_salao_ato2

label falar_anthony_ato2:
    a "Senhor Anthony...?"

    t "Ah, oi... "
    extend "O que você quer?"

    a "Nada, só queria saber se você está bem."

    "Anthony olha para Anna, surpreso."

    t "Eu... não sei. Acho que sim."
    t "Por que eu não estaria?"

    a "Você parece nervoso."
    a "... e acabamos de ficar sabendo de um homicídio no cruzeiro."

    "Anthony parece um pouco dissociado"

    t "Sim, eu ouvi. É... é horrível."

    "Ele parece saber mais do que está dizendo."

    a "Você conhecia bem o senhor Duvall, não?"

    t "Eu diria que tínhamos uma relação cordial, negócios, eventos... coisas dessa natureza."
    t "Mas como todos, temos nossas vidas separadas. O que acontece nos bastidores não cabe a mim especular."

    "Anthony desvia o olhar por um momento, claramente tentando controlar a narrativa e garantir que Anna não o pressione demais."

    a "O ruim é que coisas assim podem afetar a reputação da ATLAS Corporation."
    a "E, por consequência, a sua."

    t "hm?"

    a "Coisas assim abalam a confiança dos investidores, não é?"

    "Anthony parece desconfortável com a pergunta."

    a "Acho que todos têm algo a perder em uma situação dessas."

    t "Sim, alguns mais do que outros."

    "Anthony parece querer encerrar a conversa."

    jump escolha_salao_ato2

label falar_sophie_ato2:
    a "Senhorita Sophie..."

    s "Ah oi... "

    if use_new_name == True:
        s "[new_name], né?"
    else:
        s "Anna, né?"

    a "Sim, como você está?"

    s "...  Não sei, perplexa, eu acho"

    menu:
        "Sinto muito":
            a "Sinto muito pelo que aconteceu. Você está bem?"

            "Ela não parece ouvir a pergunta, está absorta em seus próprios pensamentos."

            jump escolha_salao_ato2
            
        "Ele era seu amigo não era?" if sophie_amigavel == True:
            a "Ele era seu amigo, não era? Deve estar sendo doloroso"

            "Sophie olha para Anna, surpresa."

            s "Como você sabe disso?"

            a "Nós conversamos antes, lembra?"

            "Sophie parece confusa, mas logo recupera a compostura."

            s "Ele era muito mais do que um amigo..."
            s "Nós tinhamos uma conexão, sabe?"
            s "Ele confiava em mim..."

            a "Eu sinto muito, Sophie."

            "Sophie suspira, e parece se acalmar um pouco."

            if use_new_name == True:
                s "Obrigada, [new_name]."
                pass
            else:
                s "Obrigada, Anna."
                pass

            "Ela parece não querer falar mais sobre o assunto."

            jump escolha_salao_ato2
