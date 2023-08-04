import os
import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "챗GPT가 뭔지 설명해줘"}
  ]
)

print(completion.choices[0].message.content)