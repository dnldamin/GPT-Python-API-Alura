from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    organization=os.getenv('OPENAI_ORGANIZATION')
)

resposta = client.chat.completions.create(
  model = "gpt-3.5-turbo",
    messages = [
      {
       "role" : "system",
       "content" : "Gere nomes de produtos de acordo com a requisição do usuário."
      },
      {
       "role" : "user",
       "content" : "Gere 10 produtos sem descrição"
      }
    ]
)

print(resposta.choices[0].message.content)
