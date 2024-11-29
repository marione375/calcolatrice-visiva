import math
import tkinter as tk

#definisco le variabili
Condizionale = 0
SommaButt = 0
Numero1 = 0
Numero2 = 0
SottrazioneButt = 0
MoltiplicazioneButt = 0
DivisioneButt = 0
#impostazioni dello schermo

screen = "-fullscreen"
full = bool[True,False]
full = True
window = tk.Tk()
window.attributes = (screen,full)
window.title("Calcolatrice")
window.geometry("1920x1080")
window.resizable(False, False)
window.configure(background= "DarkGray")

etichetta=tk.Label(window, text="Calcolatrice",fg="#D13562",font=("Arial",32))

etichetta.grid(row=0, column=0, sticky="W", padx=0, pady=0)

#bottone delle operazioni

def Somma():
    
    text=" + "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16), SommaButt = SommaButt + 1 )
    text_output.grid(row=1, column=0, sticky="w")

def Sottrazione():
    
    text=" - "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16))
    text_output.grid(row=1, column=1, sticky="w")

def Moltiplicazione():
    
    text=" * "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16))
    text_output.grid(row=1, column=2, sticky="w")

def Divisione ():
    
    text=" / "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16))
    text_output.grid(row=1, column=3, sticky="w")

def Potenza():
    
    text=" + "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16))
    text_output.grid(row=1, column=0, sticky="w")

def Radice():
    
    text=" - "
    text_output=tk.Label(window, text=text, fg="#000000", font=("Arial", 16))
    text_output.grid(row=1, column=0, sticky="w")

def InputNumero1():

   Numero1 = InputNumero1.get()
   text_output1 = tk.Label(window, fg="white", font=("Times New Roman", 12))
   text_output1.grid(row=0, column=0, sticky="S")

def RisultatoSomma():

    while SommaButt >= 0:

        Condizionale = Condizionale + 1
        RisultatoS = Numero1 + Numero2
        
        while Condizionale >= 0:
        
            Numero1 = RisultatoS
            Numero2 = 0
        


def RisultatoCasella():

    text = f"{RisultatoOperazioni}"
    text_outputR = tk.Label(window, fg="white", font=("Times New Roman", 12))
    text_outputR.grid(row=0, column=0, sticky="S")
