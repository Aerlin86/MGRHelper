import tkinter as tk
from tkinter import *
from tkinter import ttk
from mechanics import *

root = tk.Tk()

root.title('MGRHelper')
root.resizable(0, 0)


logo = ttk.Frame(root)
logo.grid()

text = Label(logo, text="MGR Helper", font=("Helvetica", 20))
text.grid(row=0, column=0)
text = Label(logo, text="Pomoc z organizacją magisterki", font=("Helvetica", 10))
text.grid(row=1, column=0)

buttons = ttk.Frame(root, padding=(20, 10, 20, 0))
buttons.grid()

choosedir_button = ttk.Button(buttons, text="Wybierz folder z pracą magisterską", command=loaddir)
choosedir_button.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E)

choosefile_button = ttk.Button(buttons, text="Wybierz plik z pracą magisterską", command=loadfile)
choosefile_button.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

makedir_button = ttk.Button(buttons, text="Utwórz foldery", command=makedir)
makedir_button.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

clean_button = ttk.Button(buttons, text="Posegreguj pliki", command=cleaning)
clean_button.grid(row=3, column=0, columnspan=3, sticky=tk.W+tk.E)

copy_button = ttk.Button(buttons, text="Wykonaj lokalną kopię pracy", command=makecopy)
copy_button.grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E)

quit_button = ttk.Button(buttons, text="Wyjscie", command=root.destroy)
quit_button.grid(row=5, column=1)

root.mainloop()
