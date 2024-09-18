label escolha_interagir_veronica:
    a "Aquela mulher loira parece deslocada... Ela está sozinha, o que é estranho em uma festa tão cheia de pessoas importantes."

    "Anna observa a mulher por alguns instantes. Alta, elegante, com um vestido caro e cabelos loiros impecáveis, ela exala uma aura de sofisticação, mas algo está fora de lugar."

    a "{i}Quem será ela?{/i}"

    menu:
        "Aproximar-se e iniciar uma conversa educada":
            jump conversar_educadamente_veronica
        "Observar mais antes de agir":
            jump observar_mais_veronica

label observar_mais_veronica:
    "Anna decide observar mais um pouco antes de se aproximar. Verônica parece desconfortável, seu olhar percorre o salão de forma distante."
    
    a "Ela parece tão distante de tudo... e todos."

    "Um garçom se aproxima de Verônica, oferecendo uma taça de champanhe, que ela aceita com um leve aceno de cabeça, mas não diz uma palavra."

    a "{i}Algo está definitivamente errado. Ela parece tão... amarga. Ou é só impressão minha?{/i}"

    "Anna decide que é o momento de agir."

    jump conversar_educadamente_veronica

label conversar_educadamente_veronica:
    a "Com licença."

    "Verônica vira a cabeça levemente para Anna, sem demonstrar muita emoção. Seus olhos frios examinam Anna de cima a baixo, antes de responder."

    v "Sim?"

    menu revelação:
        "Apresentar-se":
            a "Eu sou Anna, repórter da revista {b}Timez{/b}. Fui convidada para cobrir a inauguração do cruzeiro."

            "Verônica arqueia uma sobrancelha, claramente desinteressada."

            v "Repórter? Interessante."

            "Ela toma um pequeno gole da taça, mantendo sua expressão impassível."
            pass

        "Mentir sobre a identidade":
            $ use_new_name = True
            $ new_name = renpy.input("Eu sou...")

            a "Eu sou [new_name], e você?"
    

    a "{i}Ela não parece exatamente animada com minha presença...{/i}"

    menu:
        "Perguntar sobre a inauguração":
            jump perguntar_inauguracao_veronica
        "Perguntar se está tudo bem":
            jump perguntar_estado_veronica
        "Mencionar o nome de Miguel Duval" if investigou_atlas == True:
            jump mencionar_miguel_duval_veronica

label perguntar_inauguracao_veronica:
    a "E o que você está achando da inauguração?"

    "Verônica suspira, como se a pergunta fosse um aborrecimento."

    v "A inauguração... É uma ocasião necessária, suponho. Um espetáculo que todos esperavam."

    "Ela dá de ombros, como se a festa não tivesse qualquer importância para ela."

    v "Eu preferiria estar em qualquer outro lugar."

    a "{i}Interessante... ela parece estar totalmente desinteressada no evento. Por que alguém com tanto prestígio não se importaria?{/i}"

    jump continuar_interacao_veronica

label perguntar_estado_veronica:
    a "Você parece... desconfortável. Está tudo bem?"

    "Por um breve momento, o olhar de Verônica endurece, mas logo ela recupera sua compostura."

    v "Desconfortável? Não. Só cansada dessas festas e dessas... pessoas."

    "Ela olha ao redor do salão, como se estivesse examinando cada um dos convidados com desdém."

    v "Todos fingem ser algo que não são. No final, só resta a falsidade."

    a "{i}Ela definitivamente não está aproveitando a festa... mas o que será que está por trás disso?{/i}"

    jump continuar_interacao_veronica

label mencionar_miguel_duval_veronica:
    a "Você conhece o Miguel Duval, o proprietário deste cruzeiro?"

    "Os olhos de Verônica estreitam-se por um breve momento, antes que ela recupere a postura."

    v "Conheço... muito bem, na verdade."

    "A resposta dela é fria, mas carregada de subtexto. Anna sente a tensão no ar."

    a "{i}Há algo mais nessa resposta. Ela claramente tem algum tipo de relação complicada com Miguel...{/i}"

    v "Se me permite um conselho, senhorita... não faça muitas perguntas sobre Miguel... ou sobre mim."

    "Verônica toma um longo gole de champanhe, seu olhar distante novamente."

    jump continuar_interacao_veronica

label continuar_interacao_veronica:
    "A conversa com Verônica chega a um ponto em que ela parece querer se afastar."

    a "{i}Ela definitivamente está escondendo algo. Vou precisar descobrir mais...{/i}"

    "Antes que Anna possa continuar a conversa, Verônica interrompe educadamente."

    if use_new_name == True:
        v "Foi um prazer, [new_name], mas agora preciso cuidar de... outras coisas."
    else:
        v "Foi um prazer, senhorita Anna, mas agora preciso cuidar de... outras coisas."

    "Ela se afasta lentamente, deixando Anna com mais perguntas do que respostas."

    a "{i}Isso foi... estranho.{/i}"

    jump explorar_festa
