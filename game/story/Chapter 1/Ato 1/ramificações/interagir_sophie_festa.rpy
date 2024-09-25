label escolha_interagir_sophie:
    $ falou_sophie = True

    hide t
    hide veronica_neutral
    with dissolve
    show sophie_neutral at center
    with moveinright

    a "Aquela mulher de vestido vermelho parece ser o centro das atenções. Ela está sozinha, mas parece não se importar com isso."

    menu:
        "Abordá-la amigavelmente":
            show a at right
            show sophie_neutral at left
            with moveinright

            if investigou_atlas == True:
                a "Olá, me chamo Anna. Que bela festa Miguel organizou, não?"
            else:
                a "Olá, me chamo Anna. Que bela festa, não?"

            "Anna tenta dar um sorriso caloroso e apertar a mão de Sophie"
            if investigou_atlas == True:
                s "Boa noite! Sim, Miguel é ótimo para esses eventos grandiosos."
                jump sophie_festa_conversa_amiga
            else:
                s "Boa noite! Sim, é uma festa maravilhosa. {b}Ele{/b} sempre sabe como impressionar..."

                menu:
                    "Quem é 'Ele'?":
                        a "\'Ele\'? De quem você está falando?"
                        s "Ah, desculpe, me referi a Miguel. Ele é o organizador da festa."

                        jump sophie_festa_conversa_amiga

                    "Quem é você?":
                        a "E qual é o seu nome?"

                        jump sophie_festa_conversa_amiga

            "Ela aperta a mão de Anna..."
        
        "Abordagem formal":
            show a at right
            show sophie_neutral at left
            with moveinright
            
            "Anna decide que é melhor manter uma postura formal ao se aproximar de Sophie."
            a "Olá, boa noite"

            "Anna estende a mão para cumprimentar Sophie, que a aperta com firmeza."

            s "Boa noite, senhorita. Quem é você? Como posso ajudá-la?"

            menu:
                "Apresentar-se":
                    a "Me chamo Anna. Sou uma repórter."
                    
                    s "Repórter? Que bom pra você."
                    jump sophie_festa_conversa_formal

                "Mentir sobre a identidade":
                    $ use_new_name = True
                    $ new_name = renpy.input("Me chamo...")

                    a "Me chamo [new_name]"
                    jump sophie_festa_conversa_formal

label sophie_festa_conversa_formal:
    s "Me chamo Sophie. Sophie Blanc."

    a "Muito prazer, Sophie. Você se destaca bastante, não é?"

    s "Ah, obrigada. Eu tento."

    "Ela dá um sorriso, ajustando um cabelo. Parece estar sem graça."

    a "É difícil não reparar."

    s "Você é muito gentil, querida."

    s "Mas me diga, você é uma repórter, não é? Gostaria de uma notícia de primeira mão?"

    a "É... "
    extend "Claro, adoraria."

    a "Do que se trata?"

    s "Ah, querida... "
    extend "está vendo aquela mulher ali? A loira, alta?"

    a "O que tem ela?"

    s "O que? "
    extend "Não notou?"

    s "Ela mal falou com o marido durante a inauguração. Eles mal se olharam."
    s "{b}Com certeza{/b} ela deve estar traindo ele."

    a "Como assim?"

    s "Você não sabe? "
    extend "Ela é a esposa do Miguel."

    if investigou_atlas == True:
        a "Miguel, o dono da ATLAS?"

        s "Sim, querida. O próprio."
        pass
    else:
        a "Quem?"

        s "Miguel, o organizador da festa."
        s "CEO da ATLAS Tour."

        a "Ah, entendi."
        pass

    s "Se eu fosse você, ficaria com um olho no evento e outro na Verônica."

    a "Isso me parece intrigante. Manterei isso em mente."

    a "Consegue me manter informada?"

    s "Com todo o prazer..."

    "Sophie sorri maliciosamente."

    s "Mas, agora, se me der licença, tenho que resolver umas coisas, querida, foi um prazer."

    "Sophie se afasta, deixando Anna sozinha."

    jump explorar_festa


label sophie_festa_conversa_amiga:
    s "Eu me chamo Sophie. Sophie Blanc."

    a "Você já esteve em muitos eventos como esse?"

    s "Amiga, estive! São sempre muito divertidos."

    menu:
        "O que você vê nesses tipos de eventos?":
            a "Mesmo? Eu sempre acho esses eventos tão maçantes... "
            extend "O que você vê de tão especial neles?"

            s "Ah, querida... "
            extend "você precisa abrir os olhos para as possibilidades."
            s """
            Nesses eventos, você pode encontrar de tudo. Pessoas interessantes, histórias incríveis, glamour...

            E, claro, fazer contatos.

            Você nunca sabe quem pode estar observando.

            Quem sabe até conseguir um pretendente—
            """

            "Sophie dá uma risadinha e uma piscada, mas Anna percebe um brilho de malícia em seus olhos."

            a "É... "
            extend "definitivamente um jeito de ver as coisas."

            s "Você não acha?"
            s "Devia experimentar."

            a "Eu... vou pensar sobre isso."

            "A mulher de vestido vermelho dá um sorriso misterioso e se aproxima, sussurrando para Anna:"

            s "{i}Mas, eu recomendo que você tome cuidado com quem fala.{/i}"
            s "{i}Aquela mulher ali, por exemplo{/i}"

            if falou_veronica == True:
                "Sophie acena para Verônica, Ela parecia estar em uma espécie de Lounge."
            else:
                "Sophie acena para uma mulher elegante de cabelos loiros."

            a "O que há com ela?"

            s """
            Ela é... complicada.

            Super interesseira. Caça-níqueis, sabe?

            Recomendo você manter a postura caso ela venha falar com você, amiga.
            """

            a "Eu vou com certeza ter isso em mente."

            s "Muito bem... "
            extend "Agora, se me der licença, tenho que resolver umas coisas."

            "Sophie dá um sorriso e se afasta, deixando Anna sozinha."

            jump explorar_festa

        "Como você é convidada?":
            a "E como você é convidada para essas festas?"

            s "Ah, querida, tenho os meus contatos."

            a "O Miguel? "
            extend "Vocês se conhecem?"

            s "Ah... Você sabe. Posso dizer que sou uma ótima amiga."

            a "Jura?"

            s "Sim, ele super confia em mim..."
            extend "Somos muito próximos."

            "Há uma pausa entre elas, Sophie pondera sobre o que acabou de dizer."

            s "Só não sai por aí falando isso para todo mundo, ok?"
            s "Aquela mulher ali, por exemplo... "
            extend "morre de ciúmes dele. A esposa."

            if falou_veronica == True:
                a "{i}Ela está falando da Verônica{/i}"
                pass
            else:
                a "{i}Ela está olhando para aquela mulher loira{/i}"
                pass

            a "Ela não gosta que seja amiga dele?"

            s "Ah, amiga. Essas mulheres são assim."
            s "Não é culpa minha se ela é insegura demais, invejando que o marido dela confie mais em mim do que nela."

            a "Entendi..."

            s "Querida, eu preciso urgente dar uma escapadinha, se me der licença."

            "Sophie dá um sorriso e se afasta, deixando Anna sozinha."

            "Anna fica claramente surpresa com a revelação de Sophie."

            a "{i}Que figura interessante.{/i}"

            jump explorar_festa
