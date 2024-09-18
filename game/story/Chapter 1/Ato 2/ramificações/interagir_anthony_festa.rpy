label escolha_interagir_anthony:
    "Enquanto se mistura entre os convidados, Anna nota um homem de estatura média, com um terno impecavelmente ajustado, falando com um pequeno grupo. Ele mantém uma postura confiante, e a maneira como as pessoas ao redor dele o escutam com atenção deixa claro que é alguém de influência."

    show t at center
    with dissolve
    
    "Ela se aproxima sutilmente, sem chamar muita atenção, observando-o com mais detalhes."
    
    "O homem, que parece estar na casa dos 30, tem um cabelo castanho escuro perfeitamente penteado e um físico bem cuidado. Ele fala com firmeza, mas há algo mais... um certo nervosismo que seus olhos traem de vez em quando, como se ele estivesse constantemente calculando seus próximos passos."

    "Anna para a uma distância suficiente para ouvir sem ser notada."

    t "...o problema com esses tipos de escândalos é que, eventualmente, eles afundam qualquer reputação. Não importa quantos favores você tenha feito no passado, quando tudo desmorona, ninguém está lá para segurar a queda."
    
    "Os outros no grupo murmuram em concordância, e Anthony toma um gole de sua bebida, seus olhos varrendo o salão, como se estivesse buscando alguém ou algo."
    
    t "Mas, como eu sempre digo... o segredo é antecipar a queda antes que ela aconteça. Estar dois passos à frente."
    
    "Ele sorri, um sorriso calculado, mas que parece conquistar aqueles ao seu redor. As pessoas ao seu lado riem, e um dos homens dá um tapinha amigável em seu ombro."

    t "Exatamente, precisamos nos proteger. Alianças são úteis... até não serem mais."
    
    "Anna franze o cenho levemente, suas habilidades de repórter despertando para a sutileza nas palavras de Anthony. Ele parece estar se referindo a algo ou a alguém em particular."
    
    if investigou_atlas == True:
        a "{i}Será que ele está falando de Miguel Duval?{/i}"

    else:
        a "{i}Ele está falando de alguém específico... quem?{/i}"
    
    "Ainda sem se aproximar demais, Anna decide observar mais antes de agir. Anthony é claramente alguém que precisa ser abordado com cautela. Ele exala confiança, mas o nervosismo disfarçado em seus olhos revela que ele tem mais em jogo do que aparenta."

    "Anna, com sua intuição aguçada, já pode sentir que há algo mais profundo em Anthony. Ele não é apenas um político influente. Há algo nos bastidores que ele está tentando esconder ou manipular."

    menu escolha_anthony_acao:
        "Se aproximar e iniciar uma conversa com Anthony":
            a "Agora ou nunca..."
            "Anna caminha até o grupo onde Anthony está conversando. Quando chega perto, Anthony interrompe seu discurso por um momento, seu olhar pousando brevemente em Anna antes de voltar a falar."

            show t at left
            with moveinleft

            show a at right
            with moveinright
            
            t "Ah, parece que temos uma nova convidada aqui."
            
            "Ele se vira completamente para Anna, sorrindo com a mesma confiança ensaiada."
            
            t "Você parece familiar. Nos conhecemos de algum lugar?"

            menu apresentacao_anthony:
                "Apresentar-se":
                    a "Não exatamente, mas sou Anna, repórter da Revista {b}Timez{/b}. Fui convidada para cobrir a inauguração do cruzeiro."
            
                    "Anthony levanta uma sobrancelha, claramente interessado. A menção da imprensa sempre desperta uma certa cautela."
            
                    t "Ah, claro. A imprensa sempre tem uma forma única de captar os eventos, não é?"
            
                    a "Sim, principalmente quando os eventos são tão importantes quanto este."
            
                    "Os dois se encaram por um momento, e Anna pode sentir a cautela por trás do sorriso de Anthony."
            
                    t "Bem, espero que você goste do que vai encontrar aqui. Muita história por trás desse cruzeiro, sabe?"
            
                    a "Eu imagino."
            
                    "Anthony parece pesar suas palavras cuidadosamente, como se estivesse sempre em guarda, medindo cada frase que sai de sua boca."

                    t "Mas me diga, Anna, o que você realmente veio buscar aqui?"
            
                    "O tom dele muda levemente, tornando-se mais inquisitivo, mas ainda educado."
            
                    a "{i}Ele está tentando medir minhas intenções...{/i}"
            
                    menu resposta_anthony:
                        "Ser direta":
                            a "Vim atrás de uma boa história. E aqui parece o lugar certo para encontrá-la."

                            t "Ah, a verdade crua. Gosto disso."

                            "Anthony sorri, mas seus olhos ainda brilham com desconfiança."

                            t "Bem, espero que encontre o que procura. Mas lembre-se... algumas histórias são mais seguras se permanecerem não contadas."

                            a "Vou manter isso em mente."

                            t "Se precisar de algo, sinta-se à vontade para me procurar."

                            jump explorar_investigar

                        "Ser evasiva":
                            a "Estou apenas acompanhando o evento. Meu trabalho é observar e relatar."

                            t "Claro, claro. Observar é uma habilidade subestimada."

                            "Anthony parece satisfeito com a resposta, mas ainda mantém um olhar atento em Anna."

                            t "Bem, espero que aproveite a festa. Apenas tome cuidado com o que observa."

                            a "Com certeza."

                            jump explorar_investigar

                "Mentir sobre a identidade":
                    $ use_new_name = True
                    $ new_name = renpy.input("Eu sou...")

                    a "Eu sou [new_name]"

                    "Anthony arqueia uma sobrancelha, claramente desconfiado."

                    t "Hmm... interessante. E o que faz uma pessoa como você em um lugar como este?"

                    menu resposta_anthony_mentira:
                        "Mencionar interesse na inauguração":
                            a "A ATLAS Tour me convidou para o evento."
            
                            "Anthony parece considerar a resposta por um momento, antes de sorrir de forma sutil."
            
                            t "Ah, e... perdão a pergunta, mas o que você... "
                            extend "faz... exatamente?"
            
                            menu:
                                "Não interessa":
                                    a "Não é importante. Estou apenas aqui para observar."
            
                                    "Anthony parece intrigado, mas não insiste."
            
                                    t "Entendo. Bem, espero que encontre o que procura."
            
                                    a "Obrigada."
            
                                    jump explorar_festa
                            
                                "Mencionar interesse em Anthony":
                                    a "Estou interessada em pessoas como você, Anthony. Pessoas influentes, que sabem como manter o controle."
            
                                    "Anthony parece surpreso por um momento, mas logo recupera a compostura."
            
                                    t "Ah, então você é uma observadora. Interessante."
            
                                    a "Algo assim."
            
                                    t "Bem, espero que encontre o que procura. Mas lembre-se... nem tudo é o que parece."
            
                                    a "Vou manter isso em mente."
            
                                    jump explorar_festa
            
                            jump explorar_festa
        
        "Observar à distância":
            a "{i}Ainda é cedo para me aproximar... Melhor observar mais.{/i}"
            
            "Anna decide manter distância e continuar observando Anthony por mais tempo."
            
            "Ele conversa animadamente com as pessoas ao redor, mas a tensão em seu rosto nunca desaparece por completo. Ele é o tipo de homem que gosta de estar no controle, mas parece preocupado com algo que pode estar além de seu alcance."

            a "{i}Ele está escondendo alguma coisa, mas o que será?{/i}"

            "Depois de mais alguns minutos, Anna decide que está na hora de explorar outras partes da festa."

            jump explorar_investigar
    return