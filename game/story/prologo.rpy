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

    play audio "sfx/campainha.mp3"
    "*{i}Bling blong{/i}*" 

    a "Hm?"

    "A campainha toca."
    extend " Anna não estava esperando ninguém."

    play audio "sfx/porta_bater.mp3"
    scene anna_entrada
    with dissolve
    
    "Ela se levanta e vai até a porta."

    play audio "sfx/porta_abrir.mp3"
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
    O entregador apenas sorri e sai.

    Anna fecha a porta em confusão.

    Com o envelope em mãos, um selo dourado ostenta o símbolo de um {b}barco estilizado{/b}.
    """

    scene anna_quarto
    with dissolve

    a "Hm... "
    extend "certo."

    "Ela rasga cuidadosamente o envelope... "
    extend "é uma carta."
    "Impresso em papel de alta qualidade."

    show carta_convite at center 
    with moveinbottom
    with Pause(90)

    hide carta_convite with moveintop

#    window hide
#    nvl show
#    nvl_nar """
#    Olá Anna!
#
#    Você deseja fazer parte da história?
#
#    Você está convidada para o primeiro cruzeiro transatlântico de luxo do mundo.
#
#    Acomode-se, relaxe e embarque nessa viagem com tudo incluso no pacote completo
#    para tirar o melhor proveito da experiência!
#
#    Responda a esta carta até o dia 11/09,
#    nos enviando uma confirmação da sua presença.
#    Contamos com você!
#
#    Ass. {b}ATLAS Tour{/b}
#    """
#    nvl clear
#    nvl hide

    $ inventario.add_item(carta_convite)

    a "Bem... "
    extend "certo."

    show text "{i}Inventário Atualizado: Carta de Convite da ATLAS Tour{/i}" with dissolve
    with Pause(1)
    
    hide text with dissolve

    window show

    a "Essa é uma boa oportunidade para eu entregar um artigo de sucesso..."
    a "Se me chamaram, tenho certeza que algo querem esconder... "
    extend "ou mostrar."

    "{i}O que Anna deve fazer?{/i}"

    menu primeira_acao:
        "Ligar para o editor.":
            call ligar_editor

        "Investigar mais sobre a ATLAS Tour.":
            call investigar_atlas
    
    if investigou_atlas == True:
        a "Eu preciso de mais informações."
        play audio "sfx/telefone_toque.mp3"
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
    centered "Resolva o quebra cabeça para acessar o computador."
    menu puzzle_atlas:
        "Resolvido!":
            "Anna procura em diversos sites de notícias e blogs sobre a ATLAS Tour."
            "Após algumas horas de pesquisa, ela encontra algumas informações sobre a empresa."
            pass
        "Voltar":
            $ atlas_tour_computador.available = False
            $ investigou_atlas = False
            jump investigar_atlas

    $ atlas_tour_computador.available = True

    "Anna vai até o computador e pesquisa:"
    menu atlas_computador:
        "[atlas_tour_computador.name]" if atlas_tour_computador.available and not(atlas_tour_computador.completed):
            $ investigou_atlas = True
            a "Certo... "
            a "ATLAS Tour..."

            a "Ah, aqui está!"

            window hide
            nvl show
            nvl_nar """
            A ATLAS Tour é uma empresa fundada em 2010, especializada em viagens de luxo.
            Pela empresa já se passou nomes como Lucien Girard, antigo CEO da empresa, e recente ex-sócio do atual CEO: {b}Miguel Duvall{/b}.

            Filiada da multinacional {b}ATLAS Corporation{/b}, a empresa é conhecida por ser pioneira no ramo de turismo sob as àguas.
            Atuando também em diversos setores, como turismo, entretenimento e outros serviços.
            """
            nvl clear

            "Pesquisar afundo sobre..."
            menu escandalos:
                "Escândalo Interno":
                    a "Algo rolava enquanto Girard mantinha a postura..."

                    nvl_nar """
                    Lucien Girard.
                        
                    o homem que já foi o braço direito de Miguel Duval. Era o fundador da ATLAS Tour e um dos pioneiros no ramo de turismo de luxo.

                    No entanto, em 2018, após uma crise nos negócios da ATLAS Tour, a empresa guarda-chuva ATLAS Corporation resolveu desconectá-lo completamente da empresa.
                    """
                "Acusações Ilegais":
                    nvl_nar """
                    A empresa vem sendo alvo de críticas por conta de suas práticas de negócios.
                    A Abertura de mais de 400 hotéis de luxo em áreas de preservação ambiental e a expulsão de comunidades locais para a construção de resorts são algumas das acusações.

                    No entanto a empresa nega que tenha cometido qualquer irregularidade.
                    """

            nvl hide
            window show

            a "Isso... "
            extend "é bem esquisito."

            

#           menu pesquisa_nome:
#               "Miguel Duvall":
#                   a "Miguel Duvall?"
#                   "\"Miguel Duvall, 30 anos, atual CEO da ATLAS Tour.\""
#                   "\"Nascido e criado em São Paulo, Duvall é conhecido pelo seu carisma, ser firme, e por ser um homem de negócios bem-sucedido.\""
#                   pass
#
#               "Lucien Girard":
#                   a "Lucien Girard?"
#                   "\"Lucien Girard, 45 anos, ex-CEO da ATLAS Tour.\""
#                   "\"Girard foi o fundador da ATLAS Tour e um dos pioneiros no ramo de turismo de luxo.\""
#                   "\"Ele deixou a empresa em 2018, após uma crise nos negócios da ATLAS Tour, a empresa guarda-chuva ATLAS Corporation resolveu desconectá-lo completamente da empresa.\""
#                   pass
#
#               "ATLAS Corporation":
#                   a "ATLAS Corporation?"
#                   "\"ATLAS Corporation, empresa multinacional que atua em diversos setores, como turismo, entretenimento e outros serviços.\""
#                   "\"Algumas das filiadas são: ATLAS Host, ATLAS Tour e Cine ATLAS.\""
#                   pass
            
            "Hm..."
            return

        "\"Primeiro cruzeiro transatlântico de luxo do mundo\"":
            a "Ah, o primeiro cruzeiro transatlântico de luxo da ATLAS Tour... deve ser algo grandioso."

            nvl show
            nvl_nar """
            O primeiro cruzeiro transatlântico de luxo da ATLAS Tour, o {b}MIRAGE{/b}. Este evento marcará um ponto de virada na indústria de turismo de luxo, oferecendo uma experiência sem precedentes para os viajantes.

            MIRAGE foi projetado com a mais alta tecnologia e com uma atenção meticulosa aos detalhes de luxo. Com uma capacidade para poucos passageiros, cada cabine será uma suíte com vista panorâmica, e o navio oferece uma gama de amenities exclusivas, como restaurantes gourmet, um spa de classe mundial e atividades de entretenimento sofisticadas.

            O MIRAGE tem causado um movimento no meio de luxo e tem sido sinônimo de elegância e inovação, alguns especialistas dizem que estabelecerá um novo padrão para os cruzeiros de luxo em todo o mundo.
            """
            nvl clear

            a "Isso é realmente impressionante... parece que a ATLAS Tour se estabeleceu de vez no mercado de luxo com esse lançamento."

            return
        "11/07...":
            return
#################################################################################################

# Anna liga para o editor #######################################################################
label ligar_editor:
    $ ligou_editor == True

    show a at center with dissolve
    a "Eu deveria falar com o editor sobre isso... Pode ser uma grande oportunidade."

    "Anna pega seu telefone e rapidamente disca o número de seu editor."

    play audio "sfx/telefone_toque.mp3"
    a "Espero que ele não esteja de mau humor hoje..."

    play audio "sfx/telefone_toque.mp3"
    "O telefone toca uma, duas vezes, antes de ser atendido."

    e "Anna? Já está com a matéria pronta, certo?"

    menu editor_conversa_materia:
        "Bloqueio criativo":
            $ editor_acao = 1

            a "Então... "
            extend "sobre a matéria, estou com um pequeno bloqueio criativo."
            a "Mas, eu recebi uma coisa que pode render algo muito maior."

            e "Bloqueio criativo, Anna?"
            e "Você sabe que eu preciso daquele artigo hoje, certo? "
            extend "Não posso adiar o prazo."

            a "Eu sei... "
            extend "Mas me ouça."
            a "Isso que eu recebi pode ser uma oportunidade única."
            a "Estou falando de uma grande matéria."

            e "Eu espero que seja mesmo, porque sua última foi... "
            extend "no mínimo... "
            extend "mediana."
            pass
        "ATLAS Tour":
            $ editor_acao = 2
            a "O que você sabe sobre a ATLAS Tour?"

            e "ATLAS Tour?"

            a "Eu acabei de receber um convite deles."
            a "Dizem eles que estão lançando o \"primeiro cruzeiro transatlântico de luxo do mundo\"."

            e "E o que tem de tão especial nisso?"

            a "Bem... "
            extend "Acho que pode ser uma grande oportunidade."

            e "Hm... "
            extend "Entendo."
            e "E o que você pretende fazer?"

            a "Eu estava pensando em..."
            menu cobrir_investigar:
                "Cobrir o evento":
                    $ editor_acao = 1 #cobrir
                    a "Eu poderia cobrir o evento."
                    pass
                "Investigar a empresa":
                    $ editor_acao = 2 #investigar
                    a "Investigar a empresa."
                    pass
            
            e "Entendi."
            e "Só lembre que precisamos de algo mais impactante para a próxima edição."
            pass
    
    a "Uma coisa é certa... "
    extend "Vai ser uma viagem interessante."

    a "Mas a questão é: {b}por que me convidariam?{/b} Eu sou uma repórter independente, não sou conhecida por cobrir eventos desse tipo."

    e "Hm... então você acha que há algo por trás desse convite?"

    a "Isso."

    a "Eles parecem querer que eu escreva uma matéria \'polida\', sem levantar questões difíceis..."
    a "Já ouvimos histórias de outras empresas fazendo isso."

    e "{b}ATLAS Tour{/b}, hein? Eles têm se metido em tudo ultimamente. Hotéis, resorts, e agora cruzeiros de luxo... Parece algo grande, sim, mas qual o ângulo? Um artigo sobre um cruzeiro de luxo? Isso vai parecer um press release disfarçado de reportagem."
    
    a "Exatamente. E eu estou pensando que este cruzeiro pode ser a fachada perfeita para eles tentarem mudar a imagem pública. O fato de convidarem jornalistas pode ser uma tentativa de controlar a narrativa. E, se formos espertos, podemos expor algo grande."

    e "Mas o que a gente ganha com isso?"

    menu editor_ganhar:
        "Exclusividade":
            $ editor_ganha = 1
            a "Exclusividade."
            pass
        "Reputação":
            $ editor_ganha = 2
            a "Reputação."
            pass
        "Visibilidade":
            $ editor_ganha = 3
            a "Visibilidade."
            pass
    
    e "hm... "
    extend "A gente vai conversando."

    "A ligação termina, e Anna se prepara para a próxima etapa."

    play audio "sfx/telefone_off.mp3"
    "Anna desliga o telefone, sentindo a adrenalina correr. Ela não só conseguiu a aprovação do editor, mas também sentiu que estava prestes a descobrir algo maior do que imaginava."
    queue audio "sfx/woman_sigh.mp3"
    return

    


#################################################################################################