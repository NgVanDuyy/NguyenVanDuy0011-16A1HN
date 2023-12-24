from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style, Entry

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Ứng dụng tính toán")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        clear = Button(self, text="Xóa")
        clear.grid(row=1, column=0)
        back = Button(self, text="Quay lại")
        back.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        close = Button(self, text="Kết thúc")
        close.grid(row=1, column=3)

        mot = Button(self, text="1")
        mot.grid(row=2, column=0)
        hai = Button(self, text="2")
        hai.grid(row=2, column=1)
        ba = Button(self, text="3")
        ba.grid(row=2, column=2)
        Chia = Button(self, text="/")
        Chia.grid(row=2, column=3)

        bon = Button(self, text="4")
        bon.grid(row=3, column=0)
        nam = Button(self, text="5")
        nam.grid(row=3, column=1)
        sau = Button(self, text="6")
        sau.grid(row=3, column=2)
        Nhan = Button(self, text="*")
        Nhan.grid(row=3, column=3)

        bay = Button(self, text="7")
        bay.grid(row=4, column=0)
        tam = Button(self, text="8")
        tam.grid(row=4, column=1)
        chin = Button(self, text="9")
        chin.grid(row=4, column=2)
        Tru = Button(self, text="-")
        Tru.grid(row=4, column=3)

        zero = Button(self, text="0")
        zero.grid(row=5, column=0)
        dau_cham = Button(self, text=".")
        dau_cham.grid(row=5, column=1)
        bang = Button(self, text="=")
        bang.grid(row=5, column=2)
        Cong = Button(self, text="+")
        Cong.grid(row=5, column=3)

        self.pack()

if __name__ == "__main__":
    windows_root = Tk()
    app = Calculator(windows_root)
    windows_root.mainloop()
