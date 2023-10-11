# ETL_Python_GPT
Esse repositório possui o desafio de ETL com Python e IA Generativa do Bootcamp Santander Ciencia de Dados com Python da DIO

O objetivo desse código é gerar mensagens de parabenização aos colaboradores que venderam acima de R$15.000
Extração: Realiza a leitura do csv com os colaboradores e seus respectivos valores de venda. Após isso seleciona apenas quem vendeu acima de R$15.000
Transformação: Cria uma coluna com o nome completo e através da API do OpenAI GPT-3.5 gera uma mensagem de parabenização personalizada para cada colaborador.
Carga: Salva as informações dos colaboradores de alta performance com a mensagem de parabenização em um novo csv para disparos de emails posteriormente.
