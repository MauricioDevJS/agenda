import openai


API_KEY = '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'

modelo = 'text-davinci-003'
pergunta = 'gerar descrição para o contato contendo no máximo de 255 caracteres'

openai.api_key = API_KEY

#integração gerando texto
# response = openai.Completion.create (
#     engine = modelo,
#     prompt = pergunta,
#     max_tokens = 1024
# )

# print (response.choices[0]['text'])

response = openai.Image.create (
    prompt = 'Gerar um veiculo de duas rodas futurista',
    size = '1024x1024',
    n=2
)

print (response)