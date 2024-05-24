import pandas as pd
import os

# Obtém a lista de todos os arquivos no diretório especificado
nome_arquivos = os.listdir('C:/Users/operacional/Desktop/Leitor')

# Percorre cada arquivo na lista de arquivos
for nome_arquivo in nome_arquivos:
    
    # Verifica se o nome do arquivo começa com 'Rede_Rel_Vendas'
    if nome_arquivo.startswith('Rede_Rel_Vendas'):
        nome = nome_arquivo
        # Lê o arquivo CSV correspondente com separador ';'
        df = pd.read_csv('C:/Users/operacional/Desktop/Leitor/' + nome, sep=';')

        # Seleciona colunas específicas do DataFrame
        dados = df[['data da venda', 'modalidade', 'número de parcelas', 'bandeira', 
                    'valor da venda original', 'valor líquido', 'hora da venda']]

        # Salva o DataFrame filtrado de volta como um novo arquivo CSV
        dados.to_csv('C:/Users/operacional/Desktop/Leitor/' + nome, sep=';', index=False)

    # Verifica se o nome do arquivo começa com 'pagamentos-'
    elif nome_arquivo.startswith('pagamentos-'):
        nome = nome_arquivo

        # Lê o arquivo CSV correspondente com separador ';'
        df = pd.read_csv('C:/Users/operacional/Desktop/Leitor/' + nome, sep=';')

        # Seleciona colunas específicas do DataFrame
        dados = df[['data original da venda', 'data do recebimento', 'modalidade', 
                    'número de parcelas', 'bandeira', 'valor bruto da parcela original', 
                    'valor líquido da parcela']]

        # Extrai a data do recebimento do primeiro registro e formata para criar um novo nome de arquivo
        nome2 = df.loc[0, 'data do recebimento']
        nome2 = nome2.replace("/", "-")
        nome2 = nome2[0:5]

        # Salva o DataFrame filtrado como um novo arquivo CSV com o nome formatado
        dados.to_csv('C:/Users/operacional/Desktop/Leitor/' + "recebimento " + nome2 + ".csv", sep=';', index=False)

        # Remove o arquivo original
        os.remove('C:/Users/operacional/Desktop/Leitor/' + nome)

    # Caso o arquivo não atenda a nenhuma das condições anteriores, 'nome' é definido como None
    else:
        nome = None
