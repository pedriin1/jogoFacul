import random

print("Developed by Pedro Maia, Vitor Uema, Leonardo Rocha, Fred ")

perguntasFaceis = [(" __________________ foi o inventor da primeira calculadora, essa que era mecânica e possuia as funções de soma e subtração", "A- Blaise Pascal", "B- Gottfried Leibnitz","C- Joseph Jacquard", "D- Charles Babbage" ),("______ pode ser considerado o pai do binário, pois ele facilitou o funcionamento dos sistemas por utilizar dois dígitos ou condições.", "A - Allan Turing", "B - Von Neumann", "C - George Boole", "D - Bill Gates"), ("Atuou com afinco na segunda grande guerra, criando uma máquina que viria ser batizada com o seu nome, trabalhou para agência de segurança inglesa e atualmente foi homenageado na nota de cinquenta libras:", "A - George Stibitz", "B - Allan Turing", "C - Vannevar Bush", "D - Claude Shannon"),("Surgiu, em 1944, o primeiro computador eletromecânico, construído em Harvard pela equipe do professor H. Aiken em parceria com a IBM:", "A - ENIAC", "B - ESVAC", "C - ZUSE ONE", "D - MARK 1"), ("Projetado por Turing, _______, foi um projeto britânico que criou uma das máquinas mais imponentes, essa utilizava válvulas eletromecanicas e, realizava a leitura fotoelétrico.", "A - MS DOS", "B - Windows", "C - ENIAC", "D - Colossus")]

perguntasMedias = [("Devemos importar a biblioteca _____ para ter acesso às funções matemáticas na linguagem Python", "A - Math", "B - Pandas", "C - Random", "D - Theano"), ("Quais são as funções trigonométricas? Selecione a alternativa que possua todas elas: ", "A - Sqrt(x), math.pi, math.log(x) e math.floor(x)", "B - Cos(x), sin(x), tan(x), acos(x), asin(x) e atan(x)", "C - Math.ceil(x), math.floor(x), math.copysign(x) e math.fabs(x)", "D - Trigosen(x), trigocos(x) e trigotang(x)"),("Qual função da biblioteca math devo aplicar na variável N1 = 3 para que o resultado apresentado seja N1 = 9?", "A - Math.print(N1**2)", "B - Math.lop1pi(x)", "C - Math.pow(x,y)", "D - Math.degress(x)" )]

perguntasDificeis = [("Qual dos intervalos abaixo representa o sistema hexadecimal?", "A - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 e 15", "B - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 e 16", "C - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e F", "D - 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F e G"), ("Qual dos números abaixo apresenta inverso?", "A - 5 mod 4", "B - 150 mod 30", "C - 8 mod 2", "D - 25 mod 5")]
pontos = 0
def Acerto():
    print("=========================================")
    print("--------------VOCE ACERTOU---------------")
    print("=========================================")
semRepeticaoFacil = []
loop1 = 0
pontuacao = 0
while True:

    # Perguntas Faceis
    perguntaAleatoriaFacil = random.choice(["0", "1", "2", "3", "4"])
    if perguntaAleatoriaFacil not in semRepeticaoFacil:
        loop1 += 1

        for c in range(0, 5, 1):
            print(perguntasFaceis[int(perguntaAleatoriaFacil)][c])
            
        semRepeticaoFacil.append(perguntaAleatoriaFacil)
        resposta = input("Digite uma resposta: ")

        if int(perguntaAleatoriaFacil) == 0 and resposta == "a":
            Acerto()
            pontos += 100
            pontuacao += 1
        if int(perguntaAleatoriaFacil) == 1 and resposta == "c":
            Acerto()
            pontos += 100
            pontuacao += 1
        if int(perguntaAleatoriaFacil) == 2 and resposta ==  "b":
            Acerto()
            pontos += 100
            pontuacao += 1
        if int(perguntaAleatoriaFacil) == 3 and resposta == "d":
            Acerto()
            pontos += 100
            pontuacao += 1
        if int(perguntaAleatoriaFacil) == 4 and resposta == "d":
            Acerto()
            pontos += 100
            pontuacao += 1
        if loop1 == 5:
            break


print("Acabou")
semRepeticaoMedia = []
loop2 = 0
while True:
    perguntaAleatoriaMedia = random.choice(["0", "1", "2"])
    if perguntaAleatoriaMedia not in semRepeticaoMedia:
        loop2 += 1

        for c in range(0, 5, 1):
            print(perguntasMedias[int(perguntaAleatoriaMedia)][c])
            
        semRepeticaoMedia.append(perguntaAleatoriaMedia)
        resposta = input("Digite uma resposta: ")

        if int(perguntaAleatoriaMedia) == 0 and resposta == "a":
            Acerto()
            pontos += 150
            pontuacao += 1
        if int(perguntaAleatoriaMedia) == 1 and resposta == "b":
            Acerto()
            pontos += 150
            pontuacao += 1
        if int(perguntaAleatoriaMedia) == 2 and resposta ==  "c":
            Acerto()
            pontos += 150
            pontuacao += 1
        if loop2 == 3:
            break

semRepeticaoDificil = []
loop3 = 0

while True:
    perguntasAleatoriaDificil = random.choice(["0", "1"])
    if perguntasAleatoriaDificil not in semRepeticaoDificil:
        loop3 += 1

        for c in range(0, 5, 1):
            print(perguntasDificeis[int(perguntasAleatoriaDificil)][c])

        semRepeticaoDificil.append(perguntasAleatoriaDificil)
        resposta = input("Digite uma resposta: ")

        if int(perguntasAleatoriaDificil) == 0 and resposta == "c":
            Acerto()
            pontos += 200
            pontuacao += 1
        if int(perguntasAleatoriaDificil) == 1 and resposta == "a":
            Acerto()
            pontos += 200
            pontuacao += 1
        if loop3 == 2:
            break

if pontos > 300 and pontos <= 650:
    print(f"Pontuação abaixo da media, Você tirou {pontos} pontos do maximo de 1350, acertando {pontuacao} questões")
elif pontos > 650 and pontos <= 950:
    print(f"Pontuação mediana, Você tirou {pontos} pontos do maximo de 1350, acertando {pontuacao} questões")
elif pontos > 950:
    print(f"Pontuação alta, Você tirou {pontos} pontos do maximo de 1350, acertando {pontuacao} questões")
elif pontos <= 300:
    print(f"Pontuação muito abaixo da media, Você tirou {pontos} pontos do maximo de 1350, acertando {pontuacao} questões")
