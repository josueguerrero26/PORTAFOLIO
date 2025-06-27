#vamos a traer las liubrerias necesarias 
from tkinter import Tk, Text, Button, END, Label, Entry
from gtts import gTTS
import os

#Funsiones 
def save_text():
    text = entry_text.get("1.0", END)
    with open('texto_voz.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    status_label.config(text='Texto guardado con exito')

def text_voz():
    text = entry_text.get('1.0', END)
    voz= gTTS(text=text, lang='es-us', slow = False)
    voz.save('texto.mp3')
    os.system('start texto.mp3')
    status_label.config(text='Reproduciendo audio')

# Crear ventana principal 
root = Tk()
root.title("Convertidor de texto")
root.config(bg="#318AFF")

label_style = {
    'bg': '#318AFF',
    'fg': 'white',
    'font': ("Arial", 17)
    
}

entry_style = {
    'bg': '#D3D3D3',
    'fg': 'black',
    'font': ("Arial", 12)
}

label_text =Label(root, text='HOLA... PUEDES ESCRIBIR', **label_style)
label_text.grid(row=0, column=0, padx=5, pady=10)

entry_text = Text(root, height=3, width=20, **entry_style)
entry_text.grid(row= 1, column=0, padx=2, pady=2)

save_button =Button(root, text='Guardar texto', command=save_text )
save_button.grid(row=2, column=0, columnspan= 2, pady=10)

play_button = Button(root, text='Reproducir', command=text_voz)
play_button.grid(row=3, column= 0, columnspan=2, pady= 10)

status_label = Label(root, text='', fg='green',bg = '#318AFF')
status_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()