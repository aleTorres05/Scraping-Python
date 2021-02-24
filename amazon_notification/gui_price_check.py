import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
button = tk.Button(text="Click Me!!", fg="blue", bg="black")
entry = tk.Entry(width=50)
entry.pack()
window.mainloop()