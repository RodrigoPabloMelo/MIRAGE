label sala_segurança:
    play audio "sfx/sea_waves.mp3" loop volume 0.05
    scene sala_segura
    with fade

    show a at center with dissolve

    "Anna é escoltada por dois seguranças até uma pequena sala com câmeras de vigilância, com monitores mostrando diferentes partes do navio."
    
    "A sala de segurança tem uma iluminação fria, quase estéril, e o som abafado das ondas do mar só aumenta a tensão do momento."
    
    se "Por favor, sente-se aqui."
    
    "Anna se senta em uma cadeira dura de metal, desconfortável, enquanto os seguranças a observam de pé."

    a "{i}Isso está ficando ridículo.{/i}"
    
    se "Vamos verificar sua história."
    
    "Um dos seguranças começa a digitar algo em um computador, provavelmente confirmando a legitimidade do convite."
    
    "Enquanto isso, o outro segurança não tira os olhos de Anna."
    
    menu interrogatorio_segurança:
        "Tentar justificar" if segurança_confia == False:
            a "Olha, eu sei que tudo parece estranho, mas eu realmente fui convidada para cobrir a inauguração."
            a "A empresa me enviou o convite por conta da revista em que trabalho. Não vejo o motivo dessa confusão."
            
            "O segurança que estava de pé cruza os braços, mantendo uma expressão séria."
            
            se "E quem seria o seu contato direto na empresa? Alguma prova disso?"
            
            menu prova_contato:
                "Citar Miguel Duvall" if investigou_atlas == True:
                    a "Eu estava em contato com Miguel Duvall, o CEO da ATLAS Tour. Ele me garantiu acesso total."
                    
                    "Os seguranças se entreolham, e o que estava no computador rapidamente busca informações sobre Duvall."
                    
                    se "Sr. Duvall, é? Hmm... já ouvi esse nome."
                    
                    "O segurança que estava digitando para por um momento e se vira para Anna, com uma expressão mais suave."
                    
                    se "Se isso for verdade, é uma peça importante."
                    se "Mas mesmo assim, você vai precisar aguardar um pouco até confirmarmos tudo."
                    
                    "Anna suspira, mas mantém a calma. Após alguns minutos, um dos seguranças recebe uma ligação."
                    
                    se "Entendido. Sim, já está tudo claro."
                    
                    "O segurança desliga o telefone e se aproxima de Anna."
                    
                    se "Parece que tudo está em ordem, Senhorita Anna."
                    se "Pedimos desculpas pelo transtorno."
                    
                    a "{i}Finalmente...{/i}"
                    
                    se "Está livre para voltar à festa."

                    stop audio
                    stop music
                    stop sound
                    
                    jump sala_festa

                "Não tenho contato direto":
                    a "Na verdade, eu não tenho um contato direto. Foi um convite da própria empresa."
                    
                    "Os seguranças trocam olhares novamente, dessa vez um pouco mais desconfiados."
                    
                    se "Sem um contato direto? Estranho..."
                    se "Nós realmente não podemos liberar alguém assim tão facilmente sem verificarmos mais detalhes."
                    
                    "O segurança digita mais algumas informações no computador."
                    
                    se "Vamos precisar de mais tempo para confirmar a veracidade do seu convite. Pode demorar um pouco."
                    
                    a "{i}Isso vai atrasar tudo...{/i}"
                    
                    "Anna percebe que será interrogada por mais tempo. Ela precisa manter a calma e ser cooperativa."
                    
                    "Os minutos passam, e eventualmente os seguranças recebem uma confirmação da legitimidade do convite."
                    
                    se "Certo, parece que tudo está em ordem. Pedimos desculpas pelo inconveniente."
                    
                    a "Tudo bem. Vou tentar aproveitar a festa agora."

                    stop audio
                    stop music
                    stop sound
                    
                    jump sala_festa

        "Manter a calma":
            a "Entendo que estão apenas fazendo o trabalho de vocês. Vou cooperar o máximo que puder."
            
            "O segurança observa Anna por mais alguns instantes, tentando avaliar a sua expressão."
            
            se "Aguarde aqui. Não deve demorar muito."
            
            "Os minutos se arrastam, com Anna sentada na cadeira desconfortável, observando os seguranças verificarem as informações."
            
            "Finalmente, após alguns minutos de silêncio, o segurança recebe uma ligação em seu rádio."
            
            se "Entendido. Parece que tudo está confirmado."
            
            "Ele se aproxima de Anna, devolvendo o convite."
            
            se "Pedimos desculpas por qualquer inconveniente, senhorita. Pode prosseguir para a festa."
            
            a "Obrigada. Sem problemas."
            
            "Os seguranças abrem a porta, permitindo que Anna siga seu caminho."

            stop audio
            stop music
            stop sound
            
            jump sala_festa

        "Ficar na defensiva":
            a "Isso é um absurdo! Estou aqui a trabalho, e vocês estão me tratando como uma criminosa."
            
            "O segurança levanta uma sobrancelha, intrigado pela mudança de tom de Anna."
            
            se "Senhorita, não queremos causar problemas. Apenas seguimos protocolos."
            
            a "Protocolos ou não, estou começando a achar que vocês estão tentando esconder algo!"
            
            "Os dois seguranças se olham, claramente incomodados com o tom de Anna."
            
            se "Eu sugiro que a senhora tenha paciência e coopere. Caso contrário, a situação pode se complicar ainda mais."
            
            "Anna percebe que a atitude agressiva não está funcionando e opta por silenciar."
            
            "Depois de alguns minutos, os seguranças recebem uma confirmação."
            
            se "Parece que sua história está correta, afinal. Pode ir."
            
            a "{i}Que perda de tempo.{/i}"

            stop audio
            stop music
            stop sound
            
            jump sala_festa
