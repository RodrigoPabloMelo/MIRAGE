# Escolhe os suspeitos aleatóriamente
default suspeitos = [(t)]
default culpado = renpy.random.choice(suspeitos)

default inventario = Inventario([], 0)

default ligou_editor = False
default editor_ganha = list(range(1, 5))
default editor_acao = list(range(1, 3))


default investigou_atlas = False
default segurança_confiança = False