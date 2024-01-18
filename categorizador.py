from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    organization=os.getenv('OPENAI_ORGANIZATION')
)

resposta = client.chat.completions.create(
  model = "gpt-3.5-turbo-1106",
    messages = [
      {
       "role" : "system",
       "content" : """
        Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa e de uma descrição da categoria.
       """
      },
      {
       "role" : "user",
       "content" : """
       Escova de dentes de bambu
       """
      }
    ],
    temperature=0.5,
    max_tokens=200,
    n=3
)

for contador in range(0,3):
    print(resposta.choices[contador].message.content)
