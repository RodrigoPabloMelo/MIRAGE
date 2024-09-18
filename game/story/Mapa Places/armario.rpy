label armario:
    scene corredor
    with fade
    show screen hud
    a "Parece estar trancado."
    a "Tem algo estranho nesse armário."
    a "Não consigo abrir."

    menu armario_opcoes:
        "Tentar abrir":
            jump insira_senha
        "Voltar":
            jump explorar_investigar

    

    label insira_senha:
        show screen hud

        "A fechadura parece ser eletronica, precisa de uma senha para abrir."

        $ senha_armario = renpy.input("Insira a senha:")

        if senha_armario == "2784":
            "Um clique é ouvido."
            "O armário se abre."

            a "A senha estava correta!"
            jump armario_aberto
            
        else:
            "Senha incorreta. O display fica vermelho."
            "\"Tente novamente.\""
            jump insira_senha
