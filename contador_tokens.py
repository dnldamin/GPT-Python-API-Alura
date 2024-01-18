from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

modelo = "gpt-3.5-turbo-1106"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.001}")