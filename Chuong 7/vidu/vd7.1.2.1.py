from tkinter import * 
window = Tk() 
window.title("Welcome to Uneti.") 
#Thêm label có nội dung Hello, font chữ “Arial Bold, cỡ chữ 50”
lbl = Label(window, text="Hello", font=("Arial Bold", 50)) 
#Đặt kích thước cửa sổ theo pixels 
window.geometry('280x80') 
#Xác định vị trí của label 
lbl.grid(column=0, row=0) 
# Bắt đầu vòng lặp chạy ứng dụng (lặp vô tận để hiển thị cửa sổ trên màn hình máy tính)
window.mainloop()