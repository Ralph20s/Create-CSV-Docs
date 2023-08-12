import csv 

with open('nomes.csv', 'w', newline='') as arquivo_csv:
    campo_cabecalho = ['nomes', 'idade', 'sexo', 'cor favorita']
    writer = csv.DictWriter(arquivo_csv, fieldnames=campo_cabecalho)

    writer.writeheader()
    writer.writerow({'nomes':'Vitor', "idade":'19', 'sexo':'Masculino', 'cor favorita':'Preto'})
    writer.writerow({'nomes':'Alberico', "idade":'25', 'sexo':'Masculino', 'cor favorita':'Azul'})
    writer.writerow({'nomes':'Lucas', "idade":'18', 'sexo':'Masculino', 'cor favorita':'Vermelho'})