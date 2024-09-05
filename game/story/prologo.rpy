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
    a "Que artigo infernal! Eu não consigo escrever nada!"

    a "Preciso de uma pausa."

    """
    \"Pessoas desabrigadas, expulsas de suas casas para a construção de hotéis de luxo\", a matéria dizia.

    \"O governo prometeu investigar o caso, mas até agora nada foi feito.\"
    """

    a "Eu preciso de um café. "
    extend "Não... "
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

    Com o envelope em mãos, um selo dourado ostenta o símbolo de uma {b}bússola estilizada{/b}.
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

        "Investigar mais sobre a ATLAS Tour.":
            call investigar_atlas
    
    a "Hm..."
    a "Parece que vai ser uma viajem interessante."
    jump chapter_1
    return
    
label investigar_atlas:
    "Anna vai até o computador e pesquisa:"
    $ quest.atlas_tour_computador.available == True
    menu atlas_computador:
        "[quest.atlas_tour_computador.name]" if not(quest.atlas_tour_computador.completed) and quest.atlas_tour_computador.available:
            $ investigou_atlas == True
            a "Certo... "

            # call screen tela_pesquisa_atlas

            pass
        "\"Primeiro cruzeiro transatlântico de luxo do mundo\"":
            pass
        "11/07...":
            pass


label ligar_editor:
    $ ligou_editor == True
