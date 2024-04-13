import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
euro = cotacoes['EURBRL']['bid']
bitcoin = cotacoes['BTCBRL']['bid']


escolha = str(input('Escolha uma opção de cotação:\n1- Dolar\n2- Euro\n3- Bitcoin\n'))
while escolha not in '123' or escolha == '':
    escolha = str(input('Opção Inválida!\n---------------------------\nEscolha uma opção de cotação:\n1- Dolar\n2- Euro\n3- Bitcoin\n'))
escolha = int(escolha)
if escolha == 1:
    print('R$ ',dolar)
elif escolha == 2:
    print('R$ ',euro)
else:
    print('R$ ',bitcoin)
