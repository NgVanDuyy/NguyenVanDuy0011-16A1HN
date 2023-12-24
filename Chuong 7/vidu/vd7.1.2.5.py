import tkinter as tk 
class CheckboxApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Checkbox Example") 
        self.root.geometry('300x50') 
        
        self.var = tk.BooleanVar() 
        self.checkbox = tk.Checkbutton(root, text="Check me", 
                                    variable=self.var, 
                                    command=self.on_checkbox_click) 
        self.checkbox.pack() 
    def on_checkbox_click(self): 
        if self.var.get(): 
            print("Checkbox is checked.") 
        else: 
            print("Checkbox is unchecked.") 

if __name__ == "__main__": 
    root = tk.Tk() 
    app = CheckboxApp(root) 
root.mainloop()