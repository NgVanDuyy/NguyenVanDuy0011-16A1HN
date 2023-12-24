from tkinter import * # import tất cả các lớp và hàm từ module tkinter vào không gian tên hiện tại, cho phép sử dụng chúng mà không cần tiền tố tkinter. 

parent = Tk() 

# Đặt kích thước của cửa sổ theo pixels, chiều rộng là 200 và chiều cao là 50 
parent.geometry("200x50") 

#Tạo một đối tượng nút (button) có chữ "Red" màu đỏ. Và gán cho biến redbutton. 
redbutton = Button(parent, text="Red", fg="red") 
redbutton.pack(side=LEFT) #sắp xếp nút redbutton vào cửa sổ gốc, đặt nút bên trái. 

#Tiếp tục, tương tự như trên với các biến greenbutton, bluebutton và blackbutton. 
greenbutton = Button(parent, text="Black", fg="black") 
greenbutton.pack(side=RIGHT) 

bluebutton = Button(parent, text="Blue", fg="blue") 
bluebutton.pack(side=TOP) 

blackbutton = Button(parent, text="Green", fg="green") 
blackbutton.pack(side=BOTTOM) 

#Bắt đầu vòng lặp chạy của ứng dụng, cho phép giao diện người dùng hiển thị và xử lý sự kiện cho đến khi cửa sổ được đóng. 
parent.mainloop()
