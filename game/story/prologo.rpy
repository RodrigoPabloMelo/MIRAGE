# Apresentação
label splashscreen:
    scene black
    with Pause(1)

    show text "Emily, Júlia e Rodrigo apresenta..." with dissolve
    with Pause(2)

    hide text with dissolve

    show text "Visual Novel de Investigação" with dissolve
    with Pause(2)

    hide text with dissolve

    return

# O Jogo Começa Aqui
label start:
    $ culpado = renpy.random.choice(suspeitos)
    window hide

    scene anna_quarto
    with fade

    show text "Apartamento de Anna, Rio de Janeiro - Sexta-feira, 08:30 AM" with dissolve
    with Pause(2)

    hide text with dissolve

    window show
    with dissolve

    """
    O cheiro do café fresco e pão torrado preenchia o apartamento de Anna.

    O sol da manhã entra pelas janelas, iluminando o quarto. As fotos das suas viagens e dos amigos estão espalhadas pela parede.

    Em sua mesa, ela se sente estagnada...
    """

    show a at center with dissolve
    a "Que artigo infernal! Eu não consigo escrever nada!"

    a "Que desastre..."

    """
    \"Pessoas desabrigadas, expulsas de suas casas para a construção de hotéis de luxo\", a matéria dizia.

    \"O governo prometeu investigar o caso, mas até agora nada foi feito.\"
    """

    a "Eu preciso de um café... "
    extend "não... "
    extend "dois cafés."

    "*{i}Bling blong{/i}*" 

    a "Hm?"

    "A campainha toca."
    extend " Anna não estava esperando ninguém."

    scene anna_entrada
    with dissolve

    "Ela se levanta e vai até a porta."

    scene anna_fora
    with dissolve
    
    quem "Bom dia, senhorita Anna! Tenho uma entrega para você."

    a "{i}Entrega?{/i} "
    extend "{i}Essa hora?{/i}"

    menu resposta_entregador:
        "Obrigada?":
            a "Ah... "
            extend "é... "
            extend "Obrigada."
            quem "De nada, senhorita. Tenha um bom dia!"
            pass
        "Quem enviou?":
            a "Quem me enviou isto?"
            pass
        "O que é?":
            a "O que é isso?"
            pass
        "Não pedi nada.":
            a "Mas eu... "
            extend "não pedi nada."
            pass
    
    """
    O entregador apenas sorri e se retira.

    Anna fecha a porta e se retira.

    Com o envelope em mãos, um selo dourado ostenta o símbolo de um {b}barco estilizado{/b}.
    """

    scene anna_quarto
    with dissolve

    a "Hm... "
    extend "certo."

    "Ela rasga cuidadosamente o envelope... "
    extend "é uma carta."
    "Impresso em papel de alta qualidade."

    window hide
    nvl show
    nvl_nar """
    Olá Anna!

    Você deseja fazer parte da história?

    Você está convidada para o primeiro cruzeiro transatlântico de luxo do mundo.

    Acomode-se, relaxe e embarque nessa viagem com tudo incluso no pacote completo
    para tirar o melhor proveito da experiência!

    Responda a esta carta até o dia 11/07,
    nos enviando uma confirmação da sua presença.
    Contamos com você!

    Ass. {b}ATLAS Tour{/b}
    """
    nvl clear
    nvl hide

    $ inventario.add_item(carta_convite)

    show text "{i}Inventário Atualizado: Carta de Convite da ATLAS Tour{/i}" with dissolve
    with Pause(1)
    
    hide text with dissolve

    window show

    "{i}O que Anna deve fazer?{/i}"

    menu primeira_acao:
        "Ligar para o editor.":
            call ligar_editor
            pass

        "Investigar mais sobre a ATLAS Tour.":
            call investigar_atlas
    
    if [investigou_atlas == True]:
        a "Eu preciso de mais informações."
        "Uma ligação interrompe Anna."

        show a at center with vpunch
        chefe "Anna! "
        extend "Está atrasadíssima!"

        "Dava pra ouvir o chefe de Anna gritando do outro lado do apartamento."

        a "É... "
        a "CHEFE!?"

        "Anna olha o relógio: 10:50... "
        extend "Ela está {b}MUITO{/b} ferrada..."

    else:
        a "É... "
        a "Vai ser uma viagem interessante."

    jump chapter_1
    return

# Anna investiga a ATLAS Tour ####################################################################
label investigar_atlas:
    $ atlas_tour_computador.available = True
    "Anna vai até o computador e pesquisa:"
    menu atlas_computador:
        "[atlas_tour_computador.name]" if atlas_tour_computador.available and not(atlas_tour_computador.completed):
            $ investigou_atlas == True
            a "Certo... "

            "Anna encontra algumas informações sobre a empresa..."
            
            a "ATLAS Tour..."
            a "aqui diz: \'{i}Nossa missão é proporcionar experiências únicas, levando nossos passageiros a destinos extraordinários com um nível de luxo e conforto incomparáveis.{/i}\'"

            a "Hm... "
            extend "parece interessante."
            a "Mas, isso ainda não me diz muito."

            "Ela continua a pesquisar."

            a "Ah, aqui está!"
            a "O site diz que a ATLAS Tour é uma filiada."
            a "Eles são uma empresa  especializada no ramo de luxo."

            window hide
            nvl show
            nvl_nar """
            A ATLAS Tour é uma empresa fundada em 2010, especializada em viagens de luxo.
            Pela empresa já se passou nomes como Lucien Girard, antigo CEO da empresa, e recente ex-sócio do atual CEO: {b}Miguel Duvall{/b}.

            Filiada da {b}ATLAS Corporation{/b}, a empresa é conhecida por ser pioneira no ramo de turismo sob as àguas.
            a {b}ATLAS Corporation{/b} é uma empresa multinacional que atua em diversos setores, como turismo, entretenimento e outros serviços.

            Apesar disso, a empresa vem sendo alvo de críticas por conta de suas práticas de negócio.
            A fundação de mais de 400 hotéis de luxo em áreas de preservação ambiental e a expulsão de comunidades locais para a construção de resorts são algumas das acusações.

            No entanto a empresa nega que tenha cometido qualquer irregularidade, dizendo ter autorização dos governos locais para a construção dos hotéis.
            """
            nvl clear
            nvl hide
            window show

            a "Isso... "
            extend "é bem esquisito."

            

            menu pesquisa_nome:
                "Miguel Duvall":
                    a "Miguel Duvall?"
                    "\"Miguel Duvall, 30 anos, atual CEO da ATLAS Tour.\""
                    "\"Nascido e criado em São Paulo, Duvall é conhecido pelo seu carisma, ser firme, e por ser um homem de negócios bem-sucedido.\""
                    pass

                "Lucien Girard":
                    a "Lucien Girard?"
                    "\"Lucien Girard, 45 anos, ex-CEO da ATLAS Tour.\""
                    "\"Girard foi o fundador da ATLAS Tour e um dos pioneiros no ramo de turismo de luxo.\""
                    "\"Ele deixou a empresa em 2018, após uma crise nos negócios da ATLAS Tour, a empresa guarda-chuva ATLAS Corporation resolveu desconectá-lo completamente da empresa.\""
                    pass

                "ATLAS Corporation":
                    a "ATLAS Corporation?"
                    "\"ATLAS Corporation, empresa multinacional que atua em diversos setores, como turismo, entretenimento e outros serviços.\""
                    "\"Algumas das filiadas são: ATLAS Host, ATLAS Tour e Cine ATLAS.\""
                    pass
            
            "Hm..."

        "\"Primeiro cruzeiro transatlântico de luxo do mundo\"":
            pass
        "11/07...":
            pass
#################################################################################################

# Anna liga para o editor #######################################################################
label ligar_editor:
    $ ligou_editor == True



#################################################################################################