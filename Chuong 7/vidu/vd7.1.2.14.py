import tkinter as tk 
from tkinter import ttk 

root = tk.Tk() 
root.title("Tabs Example") 
root.geometry('300x80') 

notebook = ttk.Notebook(root) 

tab1 = ttk.Frame(notebook) 
tab2 = ttk.Frame(notebook) 

notebook.add(tab1, text="Tab 1") 
notebook.add(tab2, text="Tab 2") 

label1 = tk.Label(tab1, text="This is Tab 1") 
label1.pack(padx=5,pady=5) 

label2 = tk.Label(tab2, text="This is Tab 2") 
label2.pack(padx=5,pady=5) 

notebook.pack(fill="both", expand=True) 

root.mainloop()