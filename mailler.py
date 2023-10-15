import openai
import pandas as pd

openai.api_key = "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"

df = pd.read_excel('data.xlsx') 

template = """
isim: [$name],
soyisim: [$surname],
sirket: [$company],
pozisyon: [$position],

Ben bir yazilimciyim ve ismim alper ve belirttigim bilgilere dayanarak cold reach out mail yaz """

messages = []
for index, column in df.iterrows():
  name = column['name']
  surname = column['surname']
  sirket = column['company']
  pozisyon = column['position']


  prompt = template.replace("$name", name).replace("$surname", surname).replace("company", sirket).replace("position", pozisyon)
  
  response = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=prompt,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.5,
  )

  ai_text = response.choices[0].text
  messages.append(ai_text)

with open('outputs.txt', 'w', encoding='utf-8') as f:
  for name, message in zip(df['name'], messages):
    f.write(name + ": " + message + "\n")

print("Responses saved to outputs.txt")

