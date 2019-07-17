# quantidade = int(input('Quantos lances?'))

# while int == quantidade:
#     quantidade = input('Você digitou um valor incorreto, digite novamente com um valor númerico.')



# caractere = input('Qual material?')
# lances = ''

# while len(lances) <= quantidade:
#     lances += caractere
#     print(lances)

# Criar um programa que avalia uma proposta de empréstimo.
#    O programa recebe: idade do cliente, quanto dinheiro ele quer emprestar, quanto ele ganha por mês.

#    REGRAS para aceita o empréstimo:
#    - Entre 22 e 55 anos;
#    - Valor a partir de 1000 reais;
#    - Valor não pode ultrapassar 15x o que ele recebe

#    RESPONDER: ACEITO OU NÃO ACEITO

#    EXTRA:
#    - Perguntar também a quantidade de parcelas (3 a 20 vezes) e calcular juros de 8% ao mês (COMPOSTO)    
#    RESPONDER VALOR TOTAL DO EMPRESTIMO E VALOR Da PARCELA.

salario = input('Valor do salario:')
idade = input('Sua idade:')
valorEmprestimo = input('Qual o valor do imprestimo:')
qtdParcelas = input('Quantas parcelas:')

def emprestimo(idade, valorEmprestimo, salario, qtdParcelas):
    if idade < 22 and idade > 55 and valorEmprestimo < 1000 and valorEmprestimo>(salario * 15) and qtdParcelas < 3 and qtdParcelas > 20:
        print('Não aceito')
    
    else:
        print('Aceito')
        # montante = 0
        # montante = valorEmprestimo * (1 + 0.08) * qtdParcelas
        # montante = montante.toFixed(2)
        # parcela = montante/qtdParcelas
        # parcela = parcela.toFixed(2)
        # print(f'O valor total do empréstimo é de {montante} e o valor da parcela é de{parcela}')