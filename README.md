# Formatação de Arquivos de Conciliação e Relatórios de Vendas

Este script automatiza a formatação de arquivos de conciliação de cartão de crédito e relatórios de vendas fornecidos pelo banco Rede.

## Funcionalidades

- **Formatação de Arquivos**: O código busca formatar o arquivo de conciliação de cartão de crédito e relatórios de vendas, disponibilizado pelo banco Rede.
- **Filtragem de Colunas**: O código filtra apenas as colunas desejadas, garantindo que somente as informações necessárias sejam mantidas.
- **Processamento de Arquivos em Massa**: O código lê todos os arquivos do repositório local e realiza a formatação de todos os arquivos .csv que contenham o nome "Rede_Rel_Vendas" e "pagamentos-".
- **Automação do Processo**: O código automatiza o processo de formatação, evitando que o processo seja feito manualmente. Dessa forma, o responsável consegue ser mais eficiente e economiza tempo.

## Instruções de Uso

- Crie o seu repositório local
- Coloque os arquivos .csv a serem processados no seu repositório local.
- Altere o caminho do diretório no script para o caminho do seu repositório local. Exemplo:
   nome_arquivos = os.listdir('C:/Seu/Repositorio/Local/')

## Finalidade

- O código foi feito com a finalidade de que o arquivo final seja aceito pelo sistema ERP de vendas de um comércio que atua no atacado e varejo.


