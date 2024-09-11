# Escolhe os suspeitos aleatóriamente
default suspeitos = [(t)]
default culpado = renpy.random.choice(suspeitos)

default inventario = Inventario([], 0)

default ligou_editor = False
# 0 = nada | 1 = exclusividade | 2 = reputação | 3 = visibilidade
default editor_ganha = list(range(0, 3))
default editor_acao = list(range(0, 2))

# horarios 0 = manha | 1 = tarde | 2 = noite
default horario = list(range(0, 2))

default investigou_atlas = False
default segurança_confiança = False