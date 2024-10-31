def gauss_jordan(matriz, n):
    for i in range(n):

        pivo = matriz[i][i]
        for j in range(len(matriz[i])):
            matriz[i][j] /= pivo
        print(f"\nMatriz após normalizar a linha {i + 1}:")
        print_matriz(matriz)

        for k in range(n):
            if k != i:
                fator = matriz[k][i]
                for j in range(len(matriz[i])):
                    matriz[k][j] -= fator * matriz[i][j]
                print(f"\nMatriz após zerar o elemento na linha {k + 1}, coluna {i + 1}:")
                print_matriz(matriz)

def print_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:.2f}" for elem in linha))

def laplace_determinante(matriz, n):
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        determinante = 0
        for j in range(n):
            sub_matriz = [
                [matriz[i][k] for k in range(n) if k != j]
                for i in range(1, n)
            ]
            sinal = (-1) ** j
            determinante += sinal * matriz[0][j] * laplace_determinante(sub_matriz, n - 1)
        return determinante


def main():
    escolha = int(input("Escolaa uma operação: 1 - Teorema Gauss-Jordan, 2 - Determinante (Laplace): "))
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    if escolha == 2 and linhas != colunas:
        print("Precisa ser uma matriz quadratica.")
        return

    matriz = []
    print("Digite os elementos da matriz:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"Elemento [{i + 1},{j + 1}]: "))
            linha.append(valor)
        matriz.append(linha)

    if escolha == 1:
        if colunas != linhas + 1:
            print("precisa ser uma matriz aumentada.")
            return
        gauss_jordan(matriz, linhas)
        print("\nSolução:")
        variaveis = ['x', 'y', 'z', 'w']  
        for i in range(linhas):
            var_nome = variaveis[i] if i < len(variaveis) else f"x{i + 1}"
            print(f"{var_nome} = {matriz[i][-1]:.2f}")
    elif escolha == 2:
        determinante = laplace_determinante(matriz, linhas)
        print(f"\nDeterminante: {determinante:.2f}")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
