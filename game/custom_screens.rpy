screen hud():
    modal False

    imagebutton auto "bg_hud_inventory_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Inventario")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventario"), Hide("hud")
    
    imagebutton auto "bg_hud_map_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Mapa")
        unhovered SetVariable("screen_tooltip", "")
        action Show("mapa"), Hide("hud")

    imagebutton auto "bg_hud_autority_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Autoridade")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("end_game"), Hide("hud")

screen mapa():
    add "mapa_1_andar_idle.png"
    modal True

    imagebutton auto "mapa_botao_voltar_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Voltar")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Show("hud")
    
    imagebutton auto "mapa_1_quarto1_%s.png":
        focus_mask True
        xpos 923
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 1")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto1")
    
    imagebutton auto "mapa_1_quarto2_%s.png":
        focus_mask True
        xpos 923
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 2")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto2")
    
    imagebutton auto "mapa_1_quarto3_%s.png":
        focus_mask True
        xpos 831
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 3")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto3")
    
    imagebutton auto "mapa_1_quarto4_%s.png":
        focus_mask True
        xpos 831
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 4")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto4")

    imagebutton auto "mapa_1_quarto5_%s.png":
        focus_mask True
        xpos 742
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 5")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto5")

    imagebutton auto "mapa_1_quarto6_%s.png":
        focus_mask True
        xpos 742
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 6")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto6")

    imagebutton auto "mapa_1_quarto7_%s.png":
        focus_mask True
        xpos 650
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 7")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto7")
    
    imagebutton auto "mapa_1_quarto8_%s.png":
        focus_mask True
        xpos 650
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 8")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto8")

    imagebutton auto "mapa_1_quarto9_%s.png":
        focus_mask True
        xpos 562
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 9")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto9")

    imagebutton auto "mapa_1_quarto10_%s.png":
        focus_mask True
        xpos 562
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 10")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto10")
    
    imagebutton auto "mapa_1_quarto11_%s.png":
        focus_mask True
        xpos 469
        ypos 579
        hovered SetVariable("screen_tooltip", "Quarto 11")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto11")

    imagebutton auto "mapa_1_quarto12_%s.png":
        focus_mask True
        xpos 469
        ypos 319
        hovered SetVariable("screen_tooltip", "Quarto 12")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto12")
    
    imagebutton auto "mapa_1_quarto13_%s.png":
        focus_mask True
        xpos 330
        ypos 578
        hovered SetVariable("screen_tooltip", "Quarto 13")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto13")

    imagebutton auto "mapa_1_quarto14_%s.png":
        focus_mask True
        xpos 330
        ypos 370
        hovered SetVariable("screen_tooltip", "Quarto 14")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto14")

    imagebutton auto "mapa_1_quarto15_%s.png":
        focus_mask True
        xpos 330
        ypos 665
        hovered SetVariable("screen_tooltip", "Quarto 15")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto15")
    
    imagebutton auto "mapa_1_quarto16_%s.png":
        focus_mask True
        xpos 330
        ypos 284
        hovered SetVariable("screen_tooltip", "Quarto 16")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto16")

    imagebutton auto "mapa_1_quarto17_%s.png":
        focus_mask True
        xpos 330
        ypos 752
        hovered SetVariable("screen_tooltip", "Quarto 17")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto17")

    imagebutton auto "mapa_1_quarto18_%s.png":
        focus_mask True
        xpos 330
        ypos 197
        hovered SetVariable("screen_tooltip", "Quarto 18")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto18")
    
    imagebutton auto "mapa_1_quarto19_%s.png":
        focus_mask True
        xpos 71
        ypos 197
        hovered SetVariable("screen_tooltip", "Quarto 19")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto19")

    imagebutton auto "mapa_1_quarto20_%s.png":
        focus_mask True
        xpos 71
        ypos 284
        hovered SetVariable("screen_tooltip", "Quarto 20")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto20")

    imagebutton auto "mapa_1_quarto21_%s.png":
        focus_mask True
        xpos 71
        ypos 370
        hovered SetVariable("screen_tooltip", "Quarto 21")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto21")
    
    imagebutton auto "mapa_1_quarto22_%s.png":
        focus_mask True
        xpos 71
        ypos 491
        hovered SetVariable("screen_tooltip", "Quarto 22")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto22")
    
    imagebutton auto "mapa_1_quarto23_%s.png":
        focus_mask True
        xpos 71
        ypos 578
        hovered SetVariable("screen_tooltip", "Quarto 23")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto23")

    imagebutton auto "mapa_1_quarto24_%s.png":
        focus_mask True
        xpos 71
        ypos 665
        hovered SetVariable("screen_tooltip", "Quarto 24")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto24")

    imagebutton auto "mapa_1_quarto25_%s.png":
        focus_mask True
        xpos 71
        ypos 752
        hovered SetVariable("screen_tooltip", "Quarto 25")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("quarto25")

    imagebutton auto "mapa_1_armario_%s.png":
        focus_mask True
        xpos 134
        ypos 455
        hovered SetVariable("screen_tooltip", "Armário")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("armario")

    imagebutton auto "mapa_1_hall_%s.png":
        focus_mask True
        xpos 1015
        ypos 267
        hovered SetVariable("screen_tooltip", "Hall")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("hall")

    imagebutton auto "mapa_1_gestao_%s.png":
        focus_mask True
        xpos 1051
        ypos 755
        hovered SetVariable("screen_tooltip", "Banheiro")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("banheiro")

    imagebutton auto "mapa_1_deposito_%s.png":
        focus_mask True
        xpos 1047
        ypos 162
        hovered SetVariable("screen_tooltip", "Depósito")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("deposito")

    imagebutton auto "mapa_1_escadas_%s.png":
        focus_mask True
        xpos 859
        ypos 314
        hovered SetVariable("screen_tooltip", "Escadas")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("escadas")

    imagebutton auto "mapa_1_corredor_%s.png":
        focus_mask True
        xpos 196
        ypos 181
        hovered SetVariable("screen_tooltip", "Corredor")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("corredor")
    
    imagebutton auto "mapa_1_piscina_%s.png":
        focus_mask True
        xpos 1583
        ypos 284
        hovered SetVariable("screen_tooltip", "Piscina")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("mapa"), Jump("piscina")

screen inventartio():
    add "bg_inventario.png"
    modal True

    vbox:
        pos 0.1, 0.25
        for item in inventario.items:
            text "[item.name] - [item.description]\n" style "texto_inventario"

    imagebutton auto "inventario_botao_voltar_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Voltar")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("inventario"), Show("hud")

# screen tela_pesquisa_atlas():
