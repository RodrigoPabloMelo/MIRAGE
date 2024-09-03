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
    "Ela se levanta e vai até a porta."
    quem "Bom dia, senhorita Anna! Tenho uma entrega para você."

    a "{i}Entrega?{/i} "
    extend "{i}Essa hora?{/i}"

    a "Ah... "
    extend "é... "
    extend "Obrigada."
    a "Quem enviou?"

    "O entregador apenas sorri e se retira."