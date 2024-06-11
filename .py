import random

# Função para escolher uma palavra aleatória da lista de palavras
def escolher_palavra():
    palavras = [
        "desenvolvimento", "tecnologia", "programacao", 
        "logica", "inovacao", "tendencias", "computacao", 
        "algoritmo", "dados", "software"
    ]
    # Retorna uma palavra escolhida aleatoriamente
    return random.choice(palavras)

# Função para exibir o estado atual da forca com base nas tentativas
def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(estagios[tentativas])

# Função principal do jogo da forca
def jogar():
    palavra = escolher_palavra()  # Seleciona uma palavra aleatória
    palavra_oculta = ["_"] * len(palavra)  # Inicializa a palavra oculta com sublinhados
    tentativas = 0  # Contador de tentativas
    letras_tentadas = set()  # Conjunto para armazenar letras já tentadas
    max_tentativas = 6  # Número máximo de tentativas permitidas

    print("Bem-vindo ao Jogo da Forca!")  # Mensagem de boas-vindas
    exibir_forca(tentativas)  # Exibe o estado inicial da forca
    print(" ".join(palavra_oculta))  # Exibe a palavra oculta com sublinhados
    print("\n")

    # Loop principal do jogo
    while tentativas < max_tentativas:
        letra = input("Digite uma letra: ").lower()  # Solicita uma letra ao jogador

        # Verifica se a letra já foi tentada
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.add(letra)  # Adiciona a letra ao conjunto de letras tentadas

        # Atualiza a palavra oculta se a letra estiver na palavra
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1  # Incrementa o número de tentativas em caso de erro

        exibir_forca(tentativas)  # Exibe o estado atual da forca
        print(" ".join(palavra_oculta))  # Exibe a palavra oculta atualizada
        print("\n")

        # Verifica se o jogador ganhou
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        # Mensagem de derrota se o jogador exceder o número máximo de tentativas
        print("Você perdeu! A palavra era:", palavra)

    print("Obrigado por jogar!")  # Mensagem de agradecimento

# Executa o jogo quando o script é rodado
if __name__ == "__main__":
    jogar()
