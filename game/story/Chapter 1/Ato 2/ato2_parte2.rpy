label ato_2_parte_2:
    hide a
    hide v
    hide s
    hide t
    hide screen hud
    with dissolve
    """
    Há um clima esquisito no salão.

    As pessoas estão agitadas e conversam em voz baixa.

    Um homem morreu.

    Mas não foi qualquer homem.

    Não foi um acidente.
    """

    show a at center
    with dissolve

    a "{i}Eu {b}preciso{/b} falar com Verônica, ela não está contando alguma coisa{/i}."

    a "Na verdade... "
    extend "eu posso dar uma olhada nos quartos."

    menu:
        "Falar com Verônica":
            jump falar_veronica_ato2p2
        "Investigar os quartos":
            jump investigar_quartos_ato2

label falar_veronica_ato2p2:
    show a at right
    with moveinright

    show v at left
    with moveinleft

    "Anna decide ir até Verônica."
    "Foi um momento oportuno, os seguranças se ocuparam com outras coisas."

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

            show v at right
            with vpunch
            
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
            a "Sinto muito..."

            v "Só vá embora."

            "Anna pensa em insistir, mas Verônica parece assustada com tudo."
            "Talvez seja melhor deixá-la sozinha."

            pass
        "Confortar Verônica":
            $ veronica_confortada = True
            $ veronica_brava = False

            """
            Anna se move antes de pensar. Sem dizer uma palavra.

            Ela gentilmente pressiona as mãos nos ombros de Verônica.

            Verônica leva o lenço que estava segurando até o rosto e começa a chorar sutilmente.

            Um choro silencioso...

            Ela talvez não quisesse que ninguém visse, mas Anna estava ali.

            E ela não estava sozinha.

            Anna não sabia o que dizer, mas sabia que Verônica precisava de alguém.
            """

            v "Foi tudo tão rápido..."
            v "Eu tentei acordar ele, mas a pele dele estava fria..."
            v "pálido, sem vida..."

            a "Ele estava bem ontem?"

            v "Sim... "
            extend "Ele não estavas doente, não parecia estar sofrendo de nada."

            a "O que você estava passando pela sua cabeça?"

            v "Eu... eu não sei."
            v "Eu só queria que ele acordasse."

            v "Eu nem queria estar aqui"
            v "O meu..."
            v "Marido... "
            extend "ele se foi."

            a "Eu sinto muito, Verônica."

            v "Olha, eu... "
            extend "gostaria de ficar sozinha."

            a "Claro, estou aqui se precisar de algo."
            pass
    
    a "Eu preciso de mais informações se quiser saber o que {b}realmente{/b} aconteceu aqui."