label ato_2_parte_2:
    """
    Há um clima esquisito no salão.

    As pessoas estão agitadas e conversam em voz baixa.

    Um homem morreu.

    Mas não foi qualquer homem.

    Não foi um acidente.
    """

    a "{i}Eu {b}preciso{/b} falar com Verônica, ela não está contando alguma coisa{/i}."

    a "Na verdade... "
    extend "eu posso dar uma olhada nos quartos."

    menu:
        "Falar com Verônica":
            jump falar_veronica_ato2p2
        "Investigar os quartos":
            jump investigar_quartos_ato2

label falar_veronica_ato2p2:

    "Anna decide ir até Verônica."
    "Foi um momento oportuno, os seguranças se ocuparam com outras coisas."

    show a at left
    show veronica at right
    with dissolve

    a "Verônica, precisamos conversar."

    v "..."

    "Verônica não responde."

    a "Senhorita Duvall... "
    
    v "Por favor, me deixe sozinha."

    menu:
        "Insistir":
            $ veronica_brava = True
            $ veronica_confortada = False

            a "Por favor, eu só quero-"
            
            v """
            Você é surda?

            Eu disse para me deixar sozinha!

            Me deixe em paz!
            """

            "As pessoas ao redor olham para Anna com olhares de julgamento, cochichando entre si."
            "Claramente descontentes com a situação e a insensibilidade dela."

            a "{i}Bom trabalho, Anna...{/i}"
            pass
        "Deixá-la sozinha":
            pass
        "Confortar Verônica":
            $ veronica_confortada = True
            $ veronica_brava = False
            pass