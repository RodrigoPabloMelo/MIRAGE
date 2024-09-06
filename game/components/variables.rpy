# Escolhe os suspeitos aleatóriamente
default suspeitos = [(t)]
default culpado = renpy.random.choice(suspeitos)

default inventario = Inventario([], 0)

default ligou_editor = False
default investigou_atlas = False
default segurança_confiança = False