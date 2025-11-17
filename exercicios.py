print('Python na Escola de Programação da Alura. \n Seja Bem vindo!')

nome_aluno = input('Digite seu nome \n')
idade_aluno = input('Informe sua idade \n')

print(f'seja bem vindo {nome_aluno}, bom saber que você tem {idade_aluno} anos')

print("""A
L
U
R
A
""")

# 1. Armazena o valor de pi na variável
pi = 3.14159

# 2. Arredonda o valor de pi para duas casas decimais
pi_arredondado = round(pi, 2)

# 3. Imprime a frase com o valor arredondado
print(f"O valor arredondado de pi é: {pi_arredondado}")

## 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura
## if else para determinar se o número é par ou ímpar.

try:
    # Solicita a entrada e converte para um número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número é par (resto da divisão por 2 é 0)
    if numero % 2 == 0:
        print(f"O número {numero} é **par**.")
    else:
        # Se não for par, é ímpar
        print(f"O número {numero} é **ímpar**.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro válido.")


    ## 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura
## if elif else para classificar a idade em categorias.

try:
    # Solicita a entrada e converte para um número inteiro
    idade = int(input("Digite sua idade: "))
    
    if idade < 0:
        print("Idade inválida. Por favor, insira uma idade não negativa.")
    elif idade <= 12:
        # Criança: 0 a 12 anos
        print("Sua classificação é: **Criança**.")
    elif idade <= 18:
        # Adolescente: 13 a 18 anos
        print("Sua classificação é: **Adolescente**.")
    else:
        # Adulto: acima de 18 anos (idade > 18)
        print("Sua classificação é: **Adulto**.")

except ValueError:
    print("Entrada inválida. Por favor, digite uma idade válida em anos.")

    ## 3 - Solicite um nome de usuário e uma senha e use uma estrutura
## if else para verificar se correspondem aos valores esperados.

# Valores esperados/corretos (definidos por você)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "senha123"

# Solicita as credenciais ao usuário
nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se AMBOS correspondem aos valores esperados
if nome_usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("\n**Login bem-sucedido!** Acesso concedido.")
else:
    print("\n**Falha na autenticação.** Nome de usuário ou senha incorretos.")

    ## 4 - Solicite ao usuário as coordenadas (x, y) de um ponto e utilize uma estrutura
## if elif else para determinar em qual quadrante o ponto se encontra.

try:
    # Solicita as coordenadas e converte para números decimais (float)
    x = float(input("Digite a coordenada X: "))
    y = float(input("Digite a coordenada Y: "))
    
    # 1. Verifica o Primeiro Quadrante
    if x > 0 and y > 0:
        print(f"\nO ponto ({x}, {y}) está no **Primeiro Quadrante** (I).")
    
    # 2. Verifica o Segundo Quadrante
    elif x < 0 and y > 0:
        print(f"\nO ponto ({x}, {y}) está no **Segundo Quadrante** (II).")
    
    # 3. Verifica o Terceiro Quadrante
    elif x < 0 and y < 0:
        print(f"\nO ponto ({x}, {y}) está no **Terceiro Quadrante** (III).")
    
    # 4. Verifica o Quarto Quadrante
    elif x > 0 and y < 0:
        print(f"\nO ponto ({x}, {y}) está no **Quarto Quadrante** (IV).")
    
    # 5. Caso Contrário (Ponto nos eixos ou origem)
    else:
        if x == 0 and y == 0:
            print(f"\nO ponto ({x}, {y}) está na **Origem**.")
        elif x == 0:
            print(f"\nO ponto ({x}, {y}) está no **Eixo Y**.")
        elif y == 0:
            print(f"\nO ponto ({x}, {y}) está no **Eixo X**.")

except ValueError:
    print("Entrada inválida. Por favor, insira coordenadas numéricas válidas.")