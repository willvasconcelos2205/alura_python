# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com quatro nomes
lista_nomes = ["Ana", "Bruno", "Carla", "Daniel"]

# Lista com o ano que você nasceu e o ano atual
# (Usaremos 2000 como exemplo de ano de nascimento e 2025 como ano atual,
# que é o ano atual do sistema, para fins de demonstração)
ano_nascimento = 2000
ano_atual = 2025
lista_anos = [ano_nascimento, ano_atual]

print("Lista de Números:", lista_numeros)
print("Lista de Nomes:", lista_nomes)
print("Lista de Anos:", lista_anos)


# 2 - Crie uma lista e utilize um loop for para percorrer
# todos os elementos da lista.

minha_lista = ["Maçã", "Banana", "Laranja", "Pera"]

print("\nPercorrendo a lista de frutas:\n")
for fruta in minha_lista:
    print(fruta)

    # 3 - Loop para calcular a soma dos números ímpares de 1 a 10

soma_impares = 0
    for numero in range(1, 11):
        if numero % 2 != 0:
            soma_impares += numero

    print(f"\n A soma dos números ímpares de 1 a 10 é: **{soma_impares}**")