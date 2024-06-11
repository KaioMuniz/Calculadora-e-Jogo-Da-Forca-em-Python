# Funções para operações matemáticas
def adicionar(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: não se pode dividir por zero!"
    return a / b

def exibir_menu():
    print("\n=== Menu da Calculadora ===")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Sair")
    print("===========================")

def obter_escolha():
    while True:
        try:
            escolha = int(input("Selecione uma opção (1-5): "))
            if escolha in [1, 2, 3, 4, 5]:
                return escolha
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def executar_operacao(escolha, num1, num2):
    if escolha == 1:
        return f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}"
    elif escolha == 2:
        return f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}"
    elif escolha == 3:
        return f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}"
    elif escolha == 4:
        resultado = divisao(num1, num2)
        if resultado == "Erro: não se pode dividir por zero!":
            return resultado
        return f"Resultado: {num1} / {num2} = {resultado}"

def main():
    while True:
        exibir_menu()
        opcao = obter_escolha()

        if opcao == 5:
            print("Saindo... Até a próxima!")
            break

        numero1 = obter_numero("Digite o primeiro número: ")
        numero2 = obter_numero("Digite o segundo número: ")

        resultado = executar_operacao(opcao, numero1, numero2)
        print(resultado)

if __name__ == "__main__":
    main()
