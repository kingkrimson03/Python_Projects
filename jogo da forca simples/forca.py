import random 

# lista de palavras
palavras = ['abacaxi', 'melancia', 'morango', 'laranja', 'banana', 'uva', 'pera', 'abacate', 'manga', 'goiaba', 'cereja', 'amora', 'caju', 'acerola', 'tangerina', 'limao', 'pessego', 'mamao', 'pitanga', 'maracuja', 'graviola', 'coco', 'pitanga', 'jabuticaba', 'ameixa', 'caqui', 'carambola', 'framboesa', 'jaca', 'kiwi', 'litchi', 'mexerica', 'nectarina', 'papaya', 'pessego', 'pitanga', 'romã', 'tamar']

def forca():
    # seleção de palavras aleatórias
    palavra_selecionada = random.choice(palavras)

    # criar uma string com o tamanho da palavra
    palavra = '-' * len(palavra_selecionada)

    # inicializa as variáveis
    letras_advinhadas = []
    maxima_tentativas = 6
    tentativas = 0

    # loop principal
    while tentativas < maxima_tentativas and '-' in palavra:

        print(f'PALAVRA: {palavra}')
        print(f'TENTATIVAS RESTANTES: {maxima_tentativas - tentativas}')
        print(f'LETRAS ADVINHADAS: {",".join(letras_advinhadas)}')

        # pedir ao usuário para digitar uma letra
        advinhar = input('DIGITE UMA LETRA: ').lower()

        # verificar se a letra já foi adivinhada
        if advinhar in letras_advinhadas:
            print(f'Você já tentou a letra "{advinhar}" antes. Tente outra letra.\n')
            continue
          
        # adicionar a letra às letras adivinhadas
        letras_advinhadas.append(advinhar)

        # verificar se a letra está na palavra selecionada
        if advinhar in palavra_selecionada:
            print(f'ACERTOU!! A letra "{advinhar}" está na palavra.\n')
            # atualiza a string com a letra correta
            palavra = ''.join([c if c == advinhar else palavra[i] if palavra_selecionada[i] in letras_advinhadas else '-' for i, c in enumerate(palavra_selecionada)])
        else:
            print(f'ERROU!! A letra "{advinhar}" não está na palavra.\n')
            tentativas += 1

    # verificar o resultado do jogo
    if '-' not in palavra:
        print(f'PARABÉNS!! VOCÊ GANHOU!! A PALAVRA ERA: {palavra_selecionada}')
    else:
        print(f'VOCÊ PERDEU!! A PALAVRA ERA: {palavra_selecionada}')


forca()
