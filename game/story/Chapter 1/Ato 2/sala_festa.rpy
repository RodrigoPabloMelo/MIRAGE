label sala_festa:
    scene main_hall
    with Fade(2.0, 1.0, 2.0)

    show text "Hall Principal do Cruzeiro, 11 de setembro, 17:00" with dissolve
    with Pause(2)

    hide text with dissolve

    window show
    with dissolve



    label explorar_festa:
        menu averiguar:
            "Observar o ambiente":
                $ see_actions = True
                jump explorar_festa

            "Falar com o homem de terno" if not(falou_anthony) and see_actions == True:
                jump escolha_interagir_anthony
        
        return

    
    
    return