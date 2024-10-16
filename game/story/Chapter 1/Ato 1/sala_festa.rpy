label sala_festa:
    stop audio fadeout 2.0

    play music "audio/jazz_hall.mp3" loop volume 0.2
    play audio "sfx/crowd_talks.mp3" volume 0.1

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
        stop audio fadeout 2.0
        stop music fadeout 2.0

        hide a
        hide t
        hide s
        hide v
        with dissolve

        if falou_anthony == True and falou_sophie == True and falou_veronica == True:
            hide t
            hide s
            hide v
            with dissolve

            show a at center with dissolve

            jump continuar_festa
        else:
            if see_actions == True:

                "Anna avista:"

                if not(falou_anthony):
                    "Um {b}homem de terno preto, conversando com um grupo de convidados{/b}."
                else:
                    pass
            
                if not(falou_veronica):
                    "Uma {b}mulher alta, loira e glamourosa, que parece ser conhecida por todos{/b}."
                else:
                    pass

                if not(falou_sophie):
                    "Uma {b}mulher de cabelos negros, com um vestido vermelho luxuoso{/b}."
                else:
                    pass
            
                show sophie_neutral at right
                show veronica_neutral at center
                show t at left
                with dissolve

            menu averiguar:
                "Observar o ambiente" if see_actions == False:
                    $ see_actions = True
                    jump explorar_festa

                "Investigar o homem de terno" if not(falou_anthony) and see_actions == True:
                    jump escolha_interagir_anthony
            
                "Investigar a mulher loira" if not(falou_veronica) and see_actions == True:
                    jump escolha_interagir_veronica
            
                "Investigar a mulher de vermelho" if not(falou_sophie) and see_actions == True:
                    jump escolha_interagir_sophie
        
            return
        return
    return

label continuar_festa:
    hide t
    hide s
    hide v
    with dissolve

    a "Acho que já vi o suficiente por aqui."
    a "Preciso descansar um pouco, esse navio me dá náusea... as pessoas então, nem se fala."

    jump ato2_parte1
