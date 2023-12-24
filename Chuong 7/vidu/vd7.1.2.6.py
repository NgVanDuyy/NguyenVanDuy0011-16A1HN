import tkinter as tk
class RadioButtonExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Radio Button Example")
        self.root.geometry('300x80')
        
        # Biến kiểu IntVar để lưu giá trị radio button được chọn
        self.selected_option = tk.IntVar()

        
        # Tạo các radio button và liên kết với biến selected_option
        self.radio1 = tk.Radiobutton(self.root, text="Option 1", 
                                    variable=self.selected_option,value=1,
                                    command=self.on_radio_select)
        self.radio2 = tk.Radiobutton(self.root, text="Option 2", 
                                    variable=self.selected_option, value=2,
                                    command=self.on_radio_select)
        self.radio3 = tk.Radiobutton(self.root, text="Option 3", 
                                    variable=self.selected_option, value=3,
                                    command=self.on_radio_select)
        
        # Đặt các radio button vào cửa sổ giao diện
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
    
    def on_radio_select(self):
        selected_value = self.selected_option.get()
        print(f"Câu trả lời số {selected_value} đã được chọn.")
if __name__ == "__main__":
    root = tk.Tk()
app = RadioButtonExample(root)
root.mainloop()