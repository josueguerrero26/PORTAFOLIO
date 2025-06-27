#from gtts import gTTS
#import os

#texto = "Hoy es un buen dia para aprender python"

#output = gTTS(texto, lang='es', slow=False)
#output.save("output.mp3")

#os.system('start output.mp3')



import pyttsx3

engine = pyttsx3.init()  # Inicializa el motor

engine.say("Hola, esto es una prueba de pyttsx3")  # Texto a leer
engine.runAndWait()  # Reproduce el audio