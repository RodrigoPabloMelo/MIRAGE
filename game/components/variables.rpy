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

default see_actions = False
default see_actions_after = False

default falou_anthony = False
default falou_veronica = False


default falou_sophie = False
default sophie_amigavel = False

default falou_anthony_ato2 = False
default falou_veronica_ato2 = False
default falou_sophie_ato2 = False

default all_actions_ato2 = False

default veronica_brava = False
default veronica_confortada = False

default use_new_name = False
default new_name = "Anna"