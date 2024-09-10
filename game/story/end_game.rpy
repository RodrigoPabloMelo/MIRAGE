# Placeholder for the end of the game
label end_game:
    show a at center
    with dissolve

    a "Eu sei quem é o culpado!"
    a "O assassino é..."
    a "..."

    menu decisao_final:
        "Anthony" if culpado == t:
            a "Anthony!"
            a "Você é o assassino!"
            a "Você matou o Miguel!"

    return