label sala_festa:
    scene main_hall
    with Fade(2.0, 1.0, 2.0)

    show text "Hall Principal do Cruzeiro, 11 de setembro, 17:00" with dissolve
    with Pause(2)

    hide text with dissolve

    window show
    with dissolve

    "Anna passa pelos seguranças e finalmente adentra o salão principal do cruzeiro."
    
    "O salão é vasto, com lustres de cristal pendendo do teto alto e uma decoração luxuosa que mistura o clássico com o moderno. Músicas suaves tocam ao fundo, enquanto os convidados, vestidos com trajes de gala, conversam e brindam com taças de champanhe."
    
    "Anna respira fundo, sentindo o ambiente sofisticado e, ao mesmo tempo, a tensão discreta entre as figuras poderosas ao redor. Ela observa as pessoas, tentando identificar rostos conhecidos."
    
    a "{i}É aqui que as verdadeiras histórias começam a surgir...{/i}"


    label explorar_festa:
        if see_actions == True:
            """
            Anna avista um {b}homem de terno preto, conversando com um grupo de convidados{/b}.
            Uma {b}mulher alta, loira e glamourosa, que parece ser conhecida por todos{/b}.
            """

        menu averiguar:
            "Observar o ambiente" if see_actions == False:
                $ see_actions = True
                jump explorar_festa

            "Investigar com o homem de terno" if not(falou_anthony) and see_actions == True:
                jump escolha_interagir_anthony
            
            "Investigar com a mulher loira" if not(falou_veronica) and see_actions == True:
                jump escolha_interagir_veronica
        
        return

    
    
    return