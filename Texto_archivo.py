from gtts import gTTS
import os

with open('demo.txt', 'r', encoding="utf-8" ) as file:
    texto = file.read()

output = gTTS(texto, lang = 'es', slow=False)
output.save("output_2.mp3")

os.system('Start output_2.mp3')