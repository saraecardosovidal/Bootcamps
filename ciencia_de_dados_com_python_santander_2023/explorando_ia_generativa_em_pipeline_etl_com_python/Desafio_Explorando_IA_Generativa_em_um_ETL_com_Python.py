## O objetivo desse código é gerar mensagens de parabenização aos colaboradores que venderam acima de R$15.000

from tabulate import tabulate
import pandas as pd
import openai

# Extração
# Realiza a leitura do csv com os colaboradores e seus respectivos valores de venda. Após isso seleciona apenas quem vendeu acima de R$15.000

df = pd.read_csv('C:/Users/User/Documents/Bootcamp_Ciencia_de_Dados_Python/relatorio_vendas.csv', sep=';', header=0)

print(tabulate(df, headers='keys', tablefmt='psql'))

meta_venda=15000

df['valor_venda']=df['valor_venda'].astype(int)

publico=df[df['valor_venda']>15000]

# Transformações
# Cria uma coluna com o nome completo e através da API do OpenAI GPT-3.5 gera uma mensagem de parabenização personalizada para cada colaborador.
publico['nome_completo']=publico['nome'].str.cat(publico['sobrenome'], sep=' ')

openai_api_key='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'

openai.api_key=openai_api_key

def gerando_parabenizacao(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um gerente comercial"
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['nome_completo']} parabenizando pelo atingimento da meta de vendas (máximo de 150 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

mensagens=[]

for colaborador in range(len(publico)):
  mensagem = gerando_parabenizacao(publico.iloc[colaborador])
  mensagens.append(mensagem)

publico['texto']=mensagens

# Carga
# Salva as informações dos colaboradores de alta performance com a mensagem de parabenização em um novo csv para disparos de emails posteriormente.
publico.to_csv('C:/Users/User/Documents/Bootcamp_Ciencia_de_Dados_Python/colaboradores_alta_performance.csv',index=False,sep=";")







