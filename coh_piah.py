import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    ass_cp = [wal, ttr, hlr, sal, sac, pal]
    return ass_cp

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentencas):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases_de_todas_sentencas = []
    for sentenca in sentencas:
        frases = re.split(r'[,:;]+', sentenca)
        for frase in frases:
            frases_de_todas_sentencas.append(frase)
    return frases_de_todas_sentencas

def separa_palavras(frases):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavras_de_todas_sentencas = []
    for frase in frases:
        novas_palavras = frase.split()
        for palavra in novas_palavras:
            palavras_de_todas_sentencas.append(palavra)
    return palavras_de_todas_sentencas

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases_de_todas_sentencas = separa_frases(sentencas)
    palavras_de_todas_sentencas = separa_palavras(frases_de_todas_sentencas)
    média1 = traço1(palavras_de_todas_sentencas)
    ty_to = traço2(palavras_de_todas_sentencas)
    hapax = traço3(palavras_de_todas_sentencas)
    media2 = traço4(sentencas)
    complexidade = traço5(sentencas)
    media3 = traço6(frases_de_todas_sentencas)
    ass = [média1, ty_to, hapax, media2, complexidade, media3]    
    return ass

def n_palavras_unicas(palavras_de_todas_sentencas):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in palavras_de_todas_sentencas:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(palavras_de_todas_sentencas):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in palavras_de_todas_sentencas:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    diferentes = len(freq)
    return diferentes

def compara_assinatura(ass, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(len(ass)):
        x = abs(ass[i] - ass_cp[i])
        soma = soma + x
    grau = soma/6
    return grau

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_S = []
    for texto in textos:
        ass = calcula_assinatura(texto)
        grau = compara_assinatura(ass, ass_cp)
        lista_S.append(grau)
        men = 0
    for c in range(len(lista_S)):
        if c == 0:
            Menor_Grau = lista_S[c]
        else:
            if lista_S[c] < Menor_Grau:
                Menor_Grau = lista_S[c]
    print("O autor do texto",(c+1),"está infectado com COH-PIAH")

def traço1 (palavras_de_todas_sentencas):
    #Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    soma = 0
    for palavra in palavras_de_todas_sentencas:
        soma = soma + len(palavra)
    média1 = soma/(len(palavras_de_todas_sentencas))
    return média1

def traço2 (palavras_de_todas_sentencas):
    #Relação Type-Token 
    return n_palavras_diferentes(palavras_de_todas_sentencas)/len(palavras_de_todas_sentencas)

def traço3 (palavras_de_todas_sentencas):
    #Razão Hapax Legomana
    return n_palavras_unicas(palavras_de_todas_sentencas)/len(palavras_de_todas_sentencas)

def traço4 (sentencas):
    #Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    soma = 0
    for s in sentencas:
        soma = soma + len(s)
    media2 = soma/len(sentencas)
    return media2

def traço5 (sentencas):
    #Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    frases_de_todas_sentencas = separa_frases(sentencas)
    return len(frases_de_todas_sentencas)/len(sentencas)

def traço6 (frases_de_todas_sentencas):
    #Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto 
    soma = 0
    for frase in frases_de_todas_sentencas:
        soma = soma + len(frase)
    media3 = soma/len(frases_de_todas_sentencas)
    return media3


'''ass_cp = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
textos = ["Meu nome é Ana, te[nh]o 26 anos, sou dentista. É isto.","Oi, tudo bem? lalala. lala."]
'''
'''textos = ["Navegar é preciso; viver não é preciso".Quero para mim o espírito 
[d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; 
o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.
Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma)
a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha 
de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência 
anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara 
a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.",
"Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos
 a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas,
  mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. 
  Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, 
  pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. 
  Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu
 poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal 
era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever,
 sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
 "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma 
 construção do pensamento, em que a organização espiritual do mundo se mostra 
 num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da 
 estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena 
 afinal, que a atividade artística nos proporciona quando cria a ordem e a forma 
 a nos permite abranger com a vista o caos da vida, dando-lhe transparência"]

ass_cp = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
'''
ass_cp = le_assinatura()
textos = le_textos()
avalia_textos(textos, ass_cp)
