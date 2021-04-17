import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    lable=tk.Label(text="enter your query");
    entry= tk.Text()
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
    lable.pack()
    entry.pack()
    button.pack()
    output.pack()
    window.mainloop()

