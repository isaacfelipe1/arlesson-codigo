# Inicializando as variáveis
total_salarios = 0
total_filhos = 0
pessoas_acima_2000 = 0
pessoas_ate_150 = 0
pessoas_sem_filhos = 0
contador = 0

# Coletando dados das 200 pessoas
while contador < 200:
    contador += 1
    salario = float(input(f"Digite o salário da pessoa {contador}: "))
    num_filhos = int(input(f"Digite o número de filhos da pessoa {contador}: "))

    total_salarios += salario
    total_filhos += num_filhos

    if salario > 2000:
        pessoas_acima_2000 += 1

    if salario <= 150:
        pessoas_ate_150 += 1

    if num_filhos == 0:
        pessoas_sem_filhos += 1

# Calculando as médias
media_salarios = total_salarios / 200
media_filhos = total_filhos / 200

# Calculando as porcentagens
percentual_ate_150 = (pessoas_ate_150 / 200) * 100

# Exibindo os resultados
print(f"Média do salário: R${media_salarios:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Número de pessoas que ganham acima de R$ 2.000,00: {pessoas_acima_2000}")
print(f"Percentagem de pessoas com salários até R$ 150,00: {percentual_ate_150:.2f}%")
print(f"Número de pessoas sem filhos: {pessoas_sem_filhos}")
