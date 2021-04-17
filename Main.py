import tkinter as tk

window = tk.Tk()
lable = tk.Label(text="enter your query")
entry = tk.Text()
output = tk.Label(
    width=90,
    height=15,
    bg="white"
)
button = tk.Button(
    text="Execute",
    width=10,
    height=5,
    bg="white",
)


def execute(event):
    query = entry.get("1.0", tk.END)
    print(query)


if __name__ == '__main__':
    button.bind("<Button-1>", execute)
    lable.pack()
    entry.pack()
    button.pack()
    output.pack()
    window.mainloop()
