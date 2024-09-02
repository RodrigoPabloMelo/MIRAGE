# Personagens: detém informações sobre os personagens do jogo, incluindo preferências, relacionamentos e informações sobre o personagem.
default Characters = {
    "Leo": {
        "neutro": "images/characters/leo_neutro.png",
        "feliz": "images/characters/leo_feliz.png",
        "preferencias": ["chave_quarto", "sketchbook", "pelucia_coelho",],
        "expression": "neutro",
    },
    "Marine": {
        "neutro": "images/characters/marine_neutro.png",
        "feliz": "images/characters/marine_feliz.png",
        "preferencias": ["carta_alex", "diadema_coroa", "foto_gato_marine",],
        "expression": "neutro",
    },
    "Patrícia": {
        "neutro": "images/characters/patricia_neutro.png",
        "feliz": "images/characters/patricia_feliz.png",
        "preferencias": ["carta_marine", "revista_moda", "caneta_dourado",],
        "expression": "neutro",
    },
}

default currentCharacter = "Leo"
default lastGivenItem = None

default selected_info = ""
default selected_item = ""

# Lógica do jogo

# tela para o personagem principal da interação, mostrando os itens disponíveis
screen interact_with_characters():
    zorder 1
    add "images/scenarios/main_hall.png"

    if len(self.items) < 1:
        vbox:
            label "Não tenho nada comigo no momento..."
            textbutton "Voltar" action Return()
    else:
        frame:
            xalign 0.0
            yalign 0.0
            xsize 400
            ysize 600

            vpgrid:
                cols 2
                spacing 10
                draggable False
                mousewheel True

                scrollbars "vertical"
                xalign 0.5

                vbox:
                    for item in self.items:
                        if item_info["disponível"]:
                            textbutton (f"{item.name} - {item.description}.") action [SetVariable("selectd_item", item), SetVariable("selected_info", item.description)]
                        else:
                            text "??? - ???"
        
        if selected_item:
            draggroup:
                drag:
                    drag_name selected_item
                    droppable False
                    dragged character_dragged
                    xalign 0.1
                    yalign 0.8

                drag:
                    drag_name currentCharacter
                    draggable False
                    xalign 0.5
                    yalign 1.0
                    image Characters[currentCharacter][Characters[currentCharacter]["expression"]]