init python:
    import renpy.store as store
    import renpy.exports as renpy

    class Quest (store.object):
        def __init__(self, name, description, available = False, started = False, completed = False):
            self.name = name
            self.description = description
            self.available = available
            self.started = started
            self.completed = completed

    class QuestList (store.object):
        def __init__(self):
            self.quest_list = []

        def add_quest(self, quest):
            self.quest_list.append(quest)

        def remove_quest(self, quest):
            self.quest_list.remove(quest)

default my_quests = QuestList()

default atlas_tour_computador = Quest("ATLAS Tour", "Pesquisar sobre a ATLAS Tour")