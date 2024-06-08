import tkinter as tk


def do_it():
    new_txt = "Привет, " + entry.get() + "\n"
    label.config(text=new_txt)


root = tk.Tk()
root.title("Задача OP07")

label = tk.Label(root, text="Давай знакомиться\nКак тебя зовут?")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Жми здесь!", command=do_it)
button.pack()

root.mainloop()
