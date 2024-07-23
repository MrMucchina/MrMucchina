import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

#create window
window = tk.Tk()
window.title("calcolatrice")
window.geometry("400x600")

#style
style = ThemedStyle(window)
style.set_theme("plastik")

#variables
total = ""
operator="no"
primo_numero=0
secondo_numero=0
risultato=0
entry_int = tk.IntVar()

#functions of numbers
def button0():
	global total
	total+= "0"
	output_label.config(text=total)
def button1():
    global total
    total += "1"
    output_label.config(text=total)
def button2():
    global total
    total += "2"
    output_label.config(text=total)
def button3():
    global total
    total += "3"
    output_label.config(text=total)
def button4():
    global total
    total += "4"
    output_label.config(text=total)
def button5():
    global total
    total += "5"
    output_label.config(text=total)
def button6():
    global total
    total += "6"
    output_label.config(text=total)
def button7():
    global total
    total += "7"
    output_label.config(text=total)
def button8():
    global total
    total += "8"
    output_label.config(text=total)
def button9():
    global total
    total += "9"
    output_label.config(text=total)

#functions of operators
def buttonpiu():
    global operatore
    operatore = "add"
    global primo_numero
    global total
    primo_numero = int(total)
    total += "+"
    output_label.config(text=total)
    total = ""
def buttonmeno():
    global operatore
    operatore = "meno"
    global primo_numero
    global total
    primo_numero = int(total)
    total += "-"
    output_label.config(text=total)
    total = ""
def buttonper():
    global operatore
    operatore = "per"
    global primo_numero
    global total
    primo_numero = int(total)
    total += "*"
    output_label.config(text=total)
    total = ""
def buttondiv():
    global operatore
    operatore = "div"
    global primo_numero
    global total
    primo_numero = int(total)
    total += "/"
    output_label.config(text=total)
    total = ""
def buttonclr():
    global total
    global secondo_numero
    global primo_numero
    global operatore
    output_label.config(text="")
    primo_numero=0
    secondo_numero=0
    total=""
    operatore="no"
def buttonug():
    global total
    global secondo_numero
    global primo_numero
    global risultato
    if operatore == "add":
        secondo_numero = int(total)
        risultato = primo_numero + secondo_numero
        output_label.config(text=risultato)
    if operatore == "meno":
        secondo_numero = int(total)
        risultato = primo_numero - secondo_numero
        output_label.config(text=risultato)
    if operatore == "per":
        secondo_numero = int(total)
        risultato = primo_numero * secondo_numero
        output_label.config(text=risultato)
    if operatore == "div":
        secondo_numero = int(total)
        risultato = primo_numero / secondo_numero
        output_label.config(text=risultato)

#frames
first_frame = ttk.Frame(master=window)
second_frame = ttk.Frame(master=window)
third_frame = ttk.Frame(master=window)
fourth_frame = ttk.Frame(master=window)
fifth_frame = ttk.Frame(master=window)

#create buttons
button0 = ttk.Button(master=fourth_frame, text="0", command=button0)
button1 = ttk.Button(master=first_frame, text="1", command=button1)
button2 = ttk.Button(master=first_frame, text="2", command=button2)
button3 = ttk.Button(master=first_frame, text="3", command=button3)
button4 = ttk.Button(master=second_frame, text="4", command=button4)
button5 = ttk.Button(master=second_frame, text="5", command=button5)
button6 = ttk.Button(master=second_frame, text="6", command=button6)
button7 = ttk.Button(master=third_frame, text="7", command=button7)
button8 = ttk.Button(master=third_frame, text="8", command=button8)
button9 = ttk.Button(master=third_frame, text="9", command=button9)
buttonpiu = ttk.Button(master=first_frame, text="+", command=buttonpiu)
buttonmeno = ttk.Button(master=second_frame, text="-", command=buttonmeno)
buttonper = ttk.Button(master=third_frame, text="*", command=buttonper)
buttondiv = ttk.Button(master=fourth_frame, text="/", command=buttondiv)
buttonug = ttk.Button(master=fourth_frame, text="=", command=buttonug)
buttonclr = ttk.Button(master=fourth_frame, text="clear", command=buttonclr)

#pack buttons
buttonclr.pack(side="left")
button0.pack(side="left")
button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")
button4.pack(side="left")
button5.pack(side="left")
button6.pack(side="left")
button7.pack(side="left")
button8.pack(side="left")
button9.pack(side="left")
buttonpiu.pack(side="left")
buttonmeno.pack(side="left")
buttonper.pack(side="left")
buttonug.pack(side="left")
buttondiv.pack(side="left")

#output text
output_label = ttk.Label(master=window, text="", font="arial 20")
output_label.pack(pady=5)

#pack frames
first_frame.pack(pady=5, padx=5)
second_frame.pack(pady=5, padx=5)
third_frame.pack(pady=5, padx=5)
fourth_frame.pack(pady=5, padx=5)
fifth_frame.pack(pady=5, padx=5)

window.mainloop()