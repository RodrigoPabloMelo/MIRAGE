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

    narrator """
        Olá Anna!
        Você deseja fazer parte da história?

        Você está convidada para o primeiro cruzeiro transatlântico de luxo do mundo.

        Acomode-se, relaxe e embarque nessa viajem com tudo incluso no pacote completo
        para tirar o melhor proveito da experiência!

        Responda à esta carta até o dia 11/07,
        nos enviando uma confirmação da sua presença.
        Contamos com você!

        Ass. {b}ATLAS Tour{/b}
        """

    nvl clear
    nvl hide

    $ inventario.add_item(carta_convite)

    a """
    Hm...
    
    Me parece uma boa ideia...
    """

    jump chapter_1

    if culpado == "Patrícia":
        $ p_culpada == True