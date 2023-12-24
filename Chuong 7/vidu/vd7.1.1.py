import tkinter as tk 
# Tạo một cửa sổ chính của ứng dụng
window = tk.Tk() 
# Thêm các thành phần widget vào cửa sổ 
label = tk.Label(window, text="Hello World!") 
label.pack() 
#Thêm tiêu đề cho cửa sổ 
window.title("Wellcome to Uneti!") 
#Đặt kích thước cửa sổ theo pixels 
window.geometry('280x60') 
# Bắt đầu vòng lặp chạy ứng dụng (lặp vô tận để hiển thị cửa sổ trên màn hình máy tính) 
window.mainloop()
