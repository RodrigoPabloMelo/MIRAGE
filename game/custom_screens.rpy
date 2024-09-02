screen hud():
    modal False

    imagebutton auto "bg_hud_inventario_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Inventario")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventario"), Hide("hud")

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