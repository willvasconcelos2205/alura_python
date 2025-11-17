# 1 - Crie um dicionário representando informações sobre uma
# pessoa, como nome, idade e cidade.

pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo"
}

print("\nDicionário Pessoa:", pessoa)

# 2 - Utilizando o dicionário criado no item 1:

print("\n--- Manipulação do Dicionário ---")
print("Estado inicial:", pessoa)

# Modifique o valor de um dos itens no dicionário (ex: atualize a idade da pessoa);
pessoa["idade"] = 31
print("Idade atualizada:", pessoa)

# Adicione um campo de profissão para essa pessoa;
pessoa["profissao"] = "Engenheiro de Software"
print("Campo 'profissao' adicionado:", pessoa)

# Remova um item do dicionário.
# Usamos 'pop' que retorna o valor removido e remove a chave
cidade_removida = pessoa.pop("cidade") 
print(f"Item 'cidade' removido (Valor: {cidade_removida})")
print("Estado final:", pessoa)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos
# seus respectivos quadrados.

quadrados = {} # Começa com um dicionário vazio

# Loop de 1 a 5 (range(1, 6))
for i in range(1, 6):
    # A chave é o número (i), o valor é o seu quadrado (i * i)
    quadrados[i] = i * i

print("\nDicionário de Quadrados:", quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica
# existe dentro desse dicionário.

inventario = {
    "fruta": "Maçã",
    "quantidade": 150,
    "custo": 2.50
}

chave_para_verificar = "quantidade"
chave_inexistente = "fornecedor"

# Usando o operador 'in' (a forma mais "pythonica")
if chave_para_verificar in inventario:
    print(f"\nA chave '{chave_para_verificar}' **existe** no dicionário.")
else:
    print(f"\nA chave '{chave_para_verificar}' não existe no dicionário.")

if chave_inexistente in inventario:
    print(f"A chave '{chave_inexistente}' **existe** no dicionário.")
else:
    print(f"A chave '{chave_inexistente}' **não existe** no dicionário.")

    # 5 - Escreva um código que conte a frequência de cada palavra
# em uma frase utilizando um dicionário.

frase = "Python é divertido e Python é poderoso"
frequencia_palavras = {} # Dicionário vazio para armazenar a contagem

# 1. Limpar e Dividir a frase em palavras
# Converte tudo para minúsculas e divide a string onde há espaços
palavras = frase.lower().split() 
print("\nPalavras a serem contadas:", palavras)

# 2. Iterar sobre as palavras e contar
for palavra in palavras:
    # Verifica se a palavra já está no dicionário
    if palavra in frequencia_palavras:
        # Se estiver, incrementa a contagem
        frequencia_palavras[palavra] += 1
    else:
        # Se não estiver, adiciona a palavra com a contagem 1
        frequencia_palavras[palavra] = 1

print("\nFrequência das palavras:")
print(frequencia_palavras)