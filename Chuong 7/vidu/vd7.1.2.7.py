import tkinter as tk
class TextEditorApp:
    def __init__(self, win):
        self.win = win #Tạo một cửa sổ chính (main window) và lưu vào biến win.
        self.win.title("ScrollText Example")
        self.win.geometry('280x120')
        
        #Đặt màu nền của cửa sổ là màu xanh lam (#CCFFFF).
        self.win.configure(background="#CCFFFF") 
        self.frame1 = tk.Frame(self.win, width=100, height=40, 
                                bg='#BB0000', borderwidth=1, relief='sunken')
        
        #Tạo một thanh cuộn (scrollbar) và đặt nó trong khung frame1.
        self.scrollbar = tk.Scrollbar(self.frame1) 

        
        #Tạo một vùng văn bản (Text) có chiều rộng là 30, chiều cao là 3 và có thể tự động xuống dòng (wrap="word").
        self.editArea = tk.Text(self.frame1, width=30, height=3, 
                            wrap="word", yscrollcommand=self.scrollbar.set,
                            borderwidth=0, highlightthickness=0)
        
        #Thiết lập thanh cuộn để cuộn theo dọc khi vùng văn bản được cuộn.
        self.scrollbar.config(command=self.editArea.yview)
        
        #Đặt thanh cuộn ở phía bên phải của khung và điền cả chiều dọc của khung.
        self.scrollbar.pack(side="right", fill="y")
        
        #Đặt vùng văn bản ở phía bên trái của khung và lấp đầy cả chiều ngang và chiều dọc của khung.
        self.editArea.pack(side="left", fill="both", expand=True)
        
        #Đặt khung frame1 ở tọa độ (x=10, y=30) trong cửa sổ chính.
        self.frame1.place(x=10, y=30)
    
    def run(self):
        self.win.mainloop()#Vòng lặp chính của ứng dụng, giúp cửa sổ hiển thị &

#duy trì liên tục cho đến khi đóng cửa sổ.
if __name__ == "__main__":
    win=tk.Tk()
app = TextEditorApp(win)
app.run()