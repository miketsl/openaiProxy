import openai

openai.api_base = "http://localhost:5000/"
openai.api_key = "sk-lakjdlfkjasdf"
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "will he run for office again?"},
    ]
)

print(response)
