import tkinter as tk
import mysql.connector

class User:
    def __init__(self,role,idd,name=None):
        self.name=name
        self.id=idd
        self.role=role


class Role:
    write_words={"insert","drop","create"}
    tables={"sprzedaz","produkt","pracownik","sklep","rola"}
    perms={
        "admin":{"write","pprzedaz","produkt","pracownik","sklep","rola"},
        "pracownik":{"read","sklep","produkt"},
        "właściciel":{"read","sprzedaz","produkt","pracownik","sklep","rola"}
    }
    def __init__(self,name,idd):
        self.name=name
        self.id=idd
        self.perms=self.perms[name]

    def checkPerms(self,query):
        write_perms=True if "write" in self.perms else False
        query.lower()
        if not write_perms:
            for word in self.write_words:
                if word in query:
                    return False
        for table in self.tables:
            if table in query and table not in self.perms:
                return False
        return True


class DataAcces:
    cnx = mysql.connector.connect(user='root', passwd='Witamserdecznie128', database='sklep')
    cur = cnx.cursor(buffered=True)
    window = tk.Tk()
    log_lable = tk.Label(text="you're not logged in")
    role_lable=tk.Label()
    entry = tk.Text(
        height=10
    )
    output = tk.Label(
        width=90,
        height=10,
        bg="white",
        text="output"
    )
    passwd_input = tk.Entry(
        show="*",
        width=45,
        bg="white",
    )
    id_input = tk.Entry(
        width=45,
        bg="white"
    )
    button = tk.Button(
        text="Execute",
        width=50,
        height=5,
        bg="white"
    )
    login_button = tk.Button(
        text="login",
        width=40,
        height=5,
        bg="white"
    )
    logout_button = tk.Button(
        text="logout",
        width=40,
        height=5,
        bg="white"
    )

    def __init__(self):
        self.log_lable.grid(row=0,column=0)
        self.role_lable.grid(row=0,column=1)
        self.passwd_input.insert(tk.END, "password")
        self.id_input.insert(tk.END,"your ID")
        self.passwd_input.grid(row=1, column=1)
        self.id_input.grid(row=1, column=0)
        self.button.bind("<Button-1>", self.execute)
        self.login_button.bind("<Button-1>", self.login_event)
        self.login_button.grid(row=2, column=0)
        self.logout_button.grid(row=2,column=1)
        self.entry.insert(tk.END,"your query here")
        self.entry.grid(row=3,columnspan=2)
        self.button.grid(row=4,columnspan=2)
        self.output.grid(row=5,columnspan=2)
        self.window.mainloop()

    def verification(passwd):
        pass

    def verify(self,passwd,idd):
        query = "SELECT haslo FROM pracownik WHERE id={}".format(idd)
        self.cur.execute(query)
        results = self.cur.fetchone()[0]
        return passwd == results

    def login_event(self,event):
        idd=self.id_input.get()
        passwd=self.passwd_input.get()
        if self.verify(passwd,idd):
            self.output.config(text="logged in correctly")
            self.login_success(idd)
        else:
            self.output.config(text="wrong passwd")

    def login_success(self,idd):
        role_id_query = "SELECT rola FROM pracownik WHERE id={}".format(idd)
        self.cur.execute(role_id_query)
        role_id = self.cur.fetchone()[0]
        role_name_query = "SELECT nazwa FROM rola WHERE id={}".format(role_id)
        self.cur.execute(role_name_query)
        role_name = self.cur.fetchone()[0]
        name_query = "SELECT imie FROM pracownik WHERE id={}".format(idd)
        self.cur.execute(name_query)
        name = self.cur.fetchone()[0]
        self.log_lable.config(text="You're logged in as {}".format(name))
        self.role_lable.config(text="Your role is {}".format(role_name))
        role=Role(idd=role_id,name=role_name)
        self.currentUser=User(name=name,role=role,idd=idd)

    def execute(self,event):
        if hasattr(self,'currentUser'):
            query = self.entry.get("1.0", tk.END)
            if not self.currentUser.role.checkPerms(query):
                self.output.config(text="you have no permisions to do that")
                return
            self.cur.execute(query)
            results = self.cur.fetchall()
            out=""
            if len(results)>0:
                for text in results:
                    out+=str(text)
                    out+='\n'
                self.output.config(text=out)
            else:
                self.output.config(text="done (output was empty)")
        else:
            self.output.config(text="you have to log in first")


if __name__ == '__main__':
    app=DataAcces()
