# Escolhe os suspeitos aleatóriamente
default suspeitos = [(p), (t)]
default culpado = renpy.random.choice(suspeitos)

default inventario = Inventario([], 0)

default ligou_editor = False
default investigou_atlas = False