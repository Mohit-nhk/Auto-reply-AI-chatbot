from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="YOUR KEY",
)

command = '''
3:45 pm, 15/9/2025] 1708: Btw how's it?
[3:46 pm, 15/9/2025] Jagannath Poojari: Nice 😊 cute 🥰 no doubt
[3:46 pm, 15/9/2025] 1708: Mere jese hi lagra h na
[3:46 pm, 15/9/2025] 1708: Ya sirf mujhe lagra h
[3:47 pm, 15/9/2025] Jagannath Poojari: Nahi, lag raha hai reh
[3:47 pm, 15/9/2025] Jagannath Poojari: Good
[3:48 pm, 15/9/2025] 1708: Thx🕊️
[3:48 pm, 15/9/2025] 1708: Office mei h?
[3:48 pm, 15/9/2025] Jagannath Poojari: Yes ofc
[3:48 pm, 15/9/2025] 1708: K k
[11:30 am, 17/9/2025] Jagannath Poojari: Aaj sankashti ya kuch hai specific Ganpati ka day
[11:36 am, 17/9/2025] 1708: Ha but i usually go
[11:37 am, 17/9/2025] Jagannath Poojari: Kya hai aaj?
Sankashti or angarika?
[12:40 pm, 17/9/2025] 1708: Ekadashi
False
     
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named 1708 who speaks hindi as well as english. You are from India and is a coder. You analyze chat history and respond like 1708"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)