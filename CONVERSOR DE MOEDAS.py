#Valores de cambio com base na data 20/10/2023 as 20:00

taxas = {
    "EURO": {
        "USD": 1.06,
        "GBP": 0.87,
        "AOA": 879.64,
        "JPY": 158.85
    },
    "DOLAR": {
        "EUR": 0.94,
        "GBP": 0.82,
        "AOA": 829.50,
        "JPY": 149.86
    },
    "LIBRA": {
        "EUR": 1.15,
        "USD": 1.22,
        "AOA": 1007.93,
        "JPY": 182.09
    },
    "KWANZA": {
        "EUR": 0.0011,
        "USD": 0.0012,
        "GBP": 0.00099,
        "JPY": 0.18
    },
    "IENE": {
        "EUR": 0.0063,
        "USD": 0.0067,
        "GBP": 0.0055,
        "AOA": 5.54
    },
    "EUR": {
        "USD": 1.06,
        "GBP": 0.87,
        "AOA": 879.64,
        "JPY": 158.85
    },
    "USD": {
        "EUR": 0.94,
        "GBP": 0.82,
        "AOA": 829.50,
        "JPY": 149.86
    },
    "GBP": {
        "EUR": 1.15,
        "USD": 1.22,
        "AOA": 1007.93,
        "JPY": 182.09
    },
    "AOA": {
        "EUR": 0.0011,
        "USD": 0.0012,
        "GBP": 0.00099,
        "JPY": 0.18
    },
    "JPY": {
        "EUR": 0.0063,
        "USD": 0.0067,
        "GBP": 0.0055,
        "AOA": 5.54
    }
}

#Variaveis definidas dentro do dicionario, agora seguimos ao input do usuario
#enquanto tiver um valor dentro do input, o programa continua rodando, desde que esse valor esteja dentro do dicionario
#nesse "While" vamos determinar a moeda de origem e de destino, que ficarão armazenadas pelo programa como variaveis (Origem e Destino)
print("Conversor Limitado, possuimos apenas:\n\n          Kwanza(AOA)\n          Euro(EUR)\n          Dolar(USD)\n          Iene(JPY)\n          Libra(GBP)\n")
while True:
    origem = input("Digite a moeda de origem: ").strip().upper()
    if origem not in taxas:
        print("Moeda de origem não suportada.")
        continue

    destino = input("Digite a moeda de destino: ").strip().upper()
    if destino not in taxas:
        print("Moeda de destino não suportada.")
        continue

#se as variaveis (moedas) não existem dentro do dicionario, ele printa na tela, que não existe a moeda
#e se mantem nisso, até que as condições do while sejam atendidas

    valor = float(input("Qual o valor da moeda de origem que deseja converter? "))
#a variavel valor, tem a funcção float, pra caso o usuario queira converter um numero quebrado, por exemplo, 10.20USD para EUR.
    valor_convertido = valor * taxas[origem][destino]

    print(f"{valor:.2f} {origem} equivalem a {valor_convertido:.2f} {destino}.")
#Esta linha realiza o cálculo de conversão de moeda com base nas taxas de câmbio armazenadas no dicionário taxas. Vamos analisá-la parte por parte:

#valor: Esta variável armazena o valor da moeda de origem que o usuário deseja converter.

#taxas: Este é o dicionário que armazena as taxas de câmbio entre diferentes moedas.

#origem: Esta é a moeda de origem que o usuário escolheu. Por exemplo, "Euro" ou "Dólar".

#destino: Esta é a moeda de destino para a qual o usuário deseja converter. Por exemplo, "USD" (Dólar Americano) ou "JPY" (Iene Japonês).

    opcao = input("O que deseja fazer?\n1-Calcular outro valor\n2-Calcular mesmo valor para outra moeda de destino\n0-Sair do Programa\nOpção: ")

    if opcao == '0':
        break
    elif opcao != '1' and opcao != '2':
        print("Opção inválida. Encerrando o programa.")
        break

    if opcao == '2':
        destino = input("Digite a moeda de destino: ").strip().upper()
print("Agradeçemos a preferência!")
#mais um comentario pra fechar as 110 linhas de codigo kkkkkkkkkkkk