init python:

    def character_dragged(drags, drop):
        global currentCharacter, lastGivenItem

        if not drop:
            return False

        item = drags[0].drag_name
        character = drop.drag_name
        
        if character in characters and item in self.items and item["disponível"]:
            lastGivenItem = item

            character_expression(character, item)

            self.items(item).disponível = False
            return True

        return False

    # Classe de inventário do jogador   

    class Inventario():
        def __init__(self, items, no_of_items):
            self.items = items
            self.no_of_items = no_of_items

        # adiciona itens ao inventário do jogador
        def add_item(self, item):
            self.items.append(item)
            self.no_of_items += 1
        
        # remove items do inventário do jogador
        def remove_item(self, item):
            self.items.remove(item)
            self.no_of_items -= 1
        
        def list_items(self):
            if len(self.items) < 1:
                a("Não tenho nada comigo.")
            else:
                a("Parece que eu tenho:")
                for item in self.items:
                    a(f"{item.name}. {item.description}.")

        # Verifica se há itens no inventário
        def are_items_available(self):
            return any(item["disponível"] for item in self.items)

        # seleciona o primeiro item disponível no inventário como padrão
        def select_default_item(self):
            for item in self.items:
                if item["disponível"]:
                    return item.name, item.description
            return None, None
        

    class ItemInventario():
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image
            self.disponível = True