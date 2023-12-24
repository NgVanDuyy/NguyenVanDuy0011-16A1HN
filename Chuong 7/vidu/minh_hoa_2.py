from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Demo_2(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Khoa Khoa học ứng dụng")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Giảng viên:", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

if __name__ == "__main__":
    windows_root = Tk()
    app = Demo_2(windows_root)
    windows_root.mainloop()
