import tkinter as tk
import mysql.connector

cnx = mysql.connector.connect(user='root', passwd='Witamserdecznie128', database='sklep')
cur = cnx.cursor(buffered=True)
window = tk.Tk()
lable = tk.Label(text="enter your query")
entry = tk.Text()
output = tk.Label(
    width=90,
    height=15,
    bg="white",
)
button = tk.Button(
    text="Execute",
    width=10,
    height=5,
    bg="white",
)

def execute(event):
    query = entry.get("1.0", tk.END)
    cur.execute(query,multi=True)
    results = cur.fetchall()
    if len(results)>0:
        output.config(text=results[0])
    else:
        output.config(text="done")


if __name__ == '__main__':
    button.bind("<Button-1>", execute)
    lable.pack()
    entry.pack()
    button.pack()
    output.pack()
    window.mainloop()
