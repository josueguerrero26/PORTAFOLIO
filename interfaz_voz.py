import os 
from tkinter import Tk, Text, Button, END, Label
from gtts import gTTS




#Funsiones
def save_text():
    text = text_area.get("1.0", END)
    with open('user_input.txt', 'w', encoding ='utf-8' ) as file:
        file.write(text)
    status_label.config(text='Texto guardado con exito')


def text_voz():
    text = text_area.get('1.0', END)
    voz = gTTS(text=text, lang='es', slow = False)
    voz.save('output.mp3')
    os.system('start output.mp3')
    status_label.config(text='Reproduciendo audio')


#Crear ventana principal 
root = Tk()
root.title("Texto a voz")

text_area = Text(root, height=10, width=30)
text_area.pack()

save_button = Button(root, text="Guardar Texto", command = save_text)
save_button.pack()

play_button = Button(root, text="Reproducir texto", command = text_voz)
play_button.pack()

status_label = Label(root, text="", fg='green')
status_label.pack()

root.mainloop()