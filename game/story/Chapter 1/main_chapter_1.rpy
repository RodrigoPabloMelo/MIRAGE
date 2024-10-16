label chapter_1:
    show screen hud
    scene main_hall
    with Fade(2.0, 1.0, 2.0)

    show text "Hall Principal do Cruzeiro, 11 de setembro, 15:50" with dissolve
    with Pause(2)

    hide text with dissolve

    window show
    with dissolve

    se "Boa noite, senhora. Posso ver o seu convite, por favor?"

    show a at left
    with moveinleft
    
    a "Claro. Sou Anna, repórter da Revista {b}Timez{/b} Fui convidada para cobrir a inauguração."

    "Anna entrega o convite para o segurança."
    "O segurança dá uma olhada no convite e depois rapidamente para Anna."
    "Ele parece um pouco mais atento agora..."

    se "\'Repórter\', é? Não vejo muitos {i}desse tipo{/i} por aqui... " 
    extend "Quem a convidou?"

    menu segurança_atlas_inauguracao:
        "Miguel Duvall" if investigou_atlas == True:
            $ segurança_confia = True
            a """
            Recebi o convite diretamente de {b}Miguel Duval{/b}. 
                
            Achei que uma repórter com o meu perfil poderia captar algo além da festa...
                
            Talvez explorar o lado mais humano por trás desse empreendimento.

            {i}Bem que estão precisando...{/i}
            """

            "O segurança parece satisfeito com a resposta de Anna."
            "Ele relaxa levemente ao ouvir o nome de Miguel"

            se "Ah, entendi."
            se "Se veio a pedido do senhor Duval, é bem-vinda."

            "Ele devolve o convite e inclina a cabeça com um gesto cordial."

            se "Se precisar de algo, sinta-se à vontade para perguntar."
            se "Mas, um aviso: {i}algumas pessoas aqui não gostam muito de perguntas...{/i}"

            a "É... "
            extend "Entendi."
            a "Obrigada pelo aviso."
            a "Vou ter cuidado."

            se "Aproveite a festa, senhora."

            jump sala_festa

        "ATLAS Corporation":
            $ segurança_confia = False
            a "Foi um convite pessoal, da ATLAS Corporation."

            "O segurança parece desconfiado."
            "Ele olha para o convite novamente e depois para Anna."

            s "Hmm... "
            extend "Isso é um pouco esquisito"

            a "O que? Por quê?"
            a "Foi um convite pessoal, a ATLAS Corporation me convidou para cobrir o evento."

            "O segurança parece ainda mais desconfiado."
            "Ele olha para Anna com um olhar penetrante."

            se "Bem... "
            extend "Vou ter que pedir que me acompanhe até a sala de segurança."

            "O segurança faz um gesto para um colega e se aproxima de Anna."

            se "Por favor, me acompanhe."

            "Anna é levada para a sala de segurança."

            jump sala_segurança
            
        "ATLAS Tour":
            $ segurança_confia = True
            a """
            Fui convidada pela {b}ATLAS Tour{/b}.

            Achei que uma repórter com o meu perfil poderia captar algo além da festa...
                
            Talvez explorar o lado mais humano por trás desse empreendimento.

            {i}Bem que estão precisando...{/i}
            """

            "O segurança apenas acena."

            se "Ah, entendi."
            se "Seja bem-vinda Senhorita."

            "Ele devolve o convite e apenas deixa Anna passar."

            jump sala_festa

    return
    