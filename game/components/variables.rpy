# Escolhe os suspeitos aleatóriamente
default suspeitos = ["Patrícia", "Leo", "Marine"]

default culpado = renpy.random.choice(suspeitos)

default inventario = Inventario([], 0)