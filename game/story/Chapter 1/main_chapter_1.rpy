label chapter_1:
    
    ## Chamar essa função tá dando errado
    # $ selected_item, selected_info = inventario.select_default_item()
    $ item_given = False

    scene main_hall
    with Fade(2.0, 1.0, 2.0)
    window show
    with dissolve


    a "Este é o Hall Principal do Cruzeiro. Atual culpado é [culpado]."

    scene corredor
    with dissolve

    a "Este é o corredor do cruzeiro. Atual culpado ainda é [culpado]."
  
    