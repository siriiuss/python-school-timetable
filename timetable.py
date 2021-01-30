try:
    import Tkinter as tk
    import tkFont
    import ttk
    import datetime
    import os.path, time
    import locale
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
    import datetime
    import os.path, time
    import locale

root = tk.Tk()
tree = ttk.Treeview(root)


tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten")
tree.column("one", width=130)
tree.column("two", width=130)
tree.column("three", width=130)
tree.column("four", width=130)
tree.column("five", width=130)
tree.column("six", width=130)
tree.column("seven", width=130)
tree.column("eight", width=130)
tree.column("nine", width=130)
tree.column("ten", width=130)

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


run("data.py")
tree.pack()
root.title("Ders Programı")
root.iconphoto(False, tk.PhotoImage(file='212-512.png'))
root.mainloop()
