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

#    imagebutton auto "mapa_botao_voltar_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Voltar")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Show("hud")
#    
#    imagebutton auto "mapa_botao_2_andar_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "2º Andar")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Show("mapa_2_andar")
#    
#    imagebutton auto "mapa_1_quarto1_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 1")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto1")
#    
#    imagebutton auto "mapa_1_quarto2_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 2")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto2")
#    
#    imagebutton auto "mapa_1_quarto3_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 3")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto3")
#    
#    imagebutton auto "mapa_1_quarto4_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 4")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto4")
#
#    imagebutton auto "mapa_1_quarto5_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 5")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto5")
#
#    imagebutton auto "mapa_1_quarto6_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 6")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto6")
#
#    imagebutton auto "mapa_1_quarto7_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 7")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto7")
#    
#    imagebutton auto "mapa_1_quarto8_%s.png":
#        focus_mask True
#        hovered SetVariable("screen_tooltip", "Quarto 8")
#        unhovered SetVariable("screen_tooltip", "")
#        action Hide("mapa"), Jump("quarto8")

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
