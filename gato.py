# Importamos la librería tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import messagebox  # Importamos messagebox para mostrar mensajes emergentes

# Variables del juego
player = 'X'  # Variable que indica el jugador actual ('X' o 'O')
game_over = False  # Variable que indica si el juego ha terminado

# Función para verificar si hay un ganador
def check_winner():
    """
    Esta función verifica si hay un ganador en el tablero.
    Revisa filas, columnas y diagonales para determinar si tres botones tienen el mismo texto ('X' o 'O').
    """
    for i in range(3):
        # Verifica filas: si los tres botones de una fila tienen el mismo texto y no están vacíos
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        # Verifica columnas: si los tres botones de una columna tienen el mismo texto y no están vacíos
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    # Verifica la diagonal principal: si los tres botones de la diagonal tienen el mismo texto y no están vacíos
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    # Verifica la diagonal secundaria: si los tres botones de la diagonal tienen el mismo texto y no están vacíos
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False  # Si no hay ganador, retorna False

# Función que se ejecuta cuando un botón del tablero es presionado
def button_click(row, col):
    """
    Esta función maneja el evento de clic en un botón del tablero.
    Marca el botón con el símbolo del jugador actual ('X' o 'O') y verifica si hay un ganador o empate.
    """
    global player, game_over  # Usamos las variables globales player y game_over
    if buttons[row][col]['text'] == '' and not game_over:  # Solo permite marcar botones vacíos si el juego no ha terminado
        buttons[row][col]['text'] = player  # Marca el botón con el símbolo del jugador actual
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'  # Cambia el color del botón según el jugador
        if check_winner():  # Verifica si hay un ganador
            messagebox.showinfo("Ganador", f"El jugador {player} ha ganado!")  # Muestra un mensaje indicando el ganador
            game_over = True  # Marca el juego como terminado
        elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):  # Verifica si hay empate
            messagebox.showinfo("Empate", "El juego ha terminado en empate!")  # Muestra un mensaje indicando empate
            game_over = True  # Marca el juego como terminado
        else:
            player = 'O' if player == 'X' else 'X'  # Cambia el turno al otro jugador

# Función para reiniciar el juego
def reset_game():
    """
    Esta función reinicia el juego, limpiando el tablero y restableciendo las variables globales.
    """
    global player, game_over  # Usamos las variables globales player y game_over
    player = 'X'  # Reinicia el jugador inicial a 'X'
    game_over = False  # Reinicia el estado del juego a no terminado
    for row in range(3):  # Recorre las filas del tablero
        for col in range(3):  # Recorre las columnas del tablero
            buttons[row][col]['text'] = ''  # Limpia el texto de cada botón
            buttons[row][col]['bg'] = '#607D8B'  # Restablece el color de fondo de cada botón

# Crear la ventana principal
root = tk.Tk()  # Crea la ventana principal de la aplicación
root.title("Gato")  # Establece el título de la ventana
root.geometry("400x450")  # Establece el tamaño de la ventana
root.configure(bg='#263238')  # Establece el color de fondo de la ventana

# Crear un botón para reiniciar el juego
reset_button = tk.Button(root, text='Reiniciar', font=('Arial', 12), command=reset_game, bg='#FF5722', fg='white')
reset_button.place(relx=0.5, rely=0.9, anchor='center')  # Posiciona el botón en la parte inferior de la ventana

# Crear un marco para el tablero
frame = tk.Frame(root, bg='#263238')  # Crea un marco para contener los botones del tablero
frame.place(relx=0.5, rely=0.5, anchor='center')  # Centra el marco en la ventana

# Crear los botones del tablero
buttons = [[tk.Button(frame, text='', font=('Arial', 24), width=5, height=2, bg='#263238', fg='white',
                      command=lambda row=row, col=col: button_click(row, col))  # Asigna la función button_click a cada botón
             for col in range(3)] for row in range(3)]  # Crea una matriz de 3x3 de botones

# Posicionar los botones en el marco
for row in range(3):  # Recorre las filas
    for col in range(3):  # Recorre las columnas
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)  # Posiciona cada botón en la cuadrícula del marco

# Inicia el bucle principal de la aplicación
root.mainloop()  # Mantiene la ventana abierta y espera interacciones del usuario