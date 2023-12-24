from tkinter import * # import tất cả các lớp và hàm từ module tkinter vào không gian tên hiện tại, cho phép sử dụng chúng mà không cần tiền tố tkinter. 

parent = Tk() 

# Đặt kích thước của cửa sổ theo pixels, chiều rộng là 200 và chiều cao là 100
parent.geometry("200x100") 

#tạo một đối tượng nhãn (label) với văn bản "Name" và gắn nó vào cửa sổ gốc. 
#phương thức grid() được gọi để xác định vị trí của nhãn với row=0 và column=0. 
name = Label(parent, text = "Name").grid(row = 0, column = 0) 

#Tương tự, các dòng mã 14,15,16 tạo và định vị các nhãn và ô nhập liệu khác trong lưới. 

e1 = Entry(parent).grid(row = 0, column = 1) 
password = Label(parent, text = "Password").grid(row = 1, column = 0) 

e2 = Entry(parent).grid(row = 1, column = 1) 
submit = Button(parent, text = "Submit").grid(row = 4, column = 0) 

#Bắt đầu vòng lặp chạy của ứng dụng, cho phép giao diện người dùng hiển thị và xử lý sự kiện cho đến khi cửa sổ được đóng. 
parent.mainloop()
