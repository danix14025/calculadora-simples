def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b

def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "5":
            print("Saindo da calculadora. Até mais!")
            break

        if escolha in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = somar(num1, num2)
                operacao = "+"
            elif escolha == "2":
                resultado = subtrair(num1, num2)
                operacao = "-"
            elif escolha == "3":
                resultado = multiplicar(num1, num2)
                operacao = "*"
            elif escolha == "4":
                resultado = dividir(num1, num2)
                operacao = "/"

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
        else:
            print("Opção inválida! Tente novamente.")

# Executa a calculadora
calculadora()
