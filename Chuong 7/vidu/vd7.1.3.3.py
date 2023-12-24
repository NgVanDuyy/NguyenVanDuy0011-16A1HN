from tkinter import * 
 
#tạo một đối tượng cửa sổ gốc (root window) sử dụng lớp Tk trong Tkinter và gán cho biến top. Cửa sổ gốc là cửa sổ chính của ứng dụng.
windows = Tk() 

#Thêm tiêu đề cho cửa cửa sổ 
windows.title("Wellcome to Uneti!") 
windows.geometry("400x150") #Xác định kích thước của sổ tính theo pixels 

# tạo một nhãn (label) có văn bản "Name" và gắn nó vào cửa sổ windows. 
# Sau đó, gọi phương thức place() để đặt nhãn tại tọa độ tuyệt đối (30, 50). 
name = Label(windows, text = "Name").place(x = 30, y = 30) 

#Tương tự: Tạo các nhãn (label) "Email", "Password" với các ô nhập liệu (entry) tương ứng. 
# Gọi phương thức place() để đặt các nhãn đó tại các tọa độ tuyệt đối x,y. 
email = Label(windows, text = "Email").place(x = 30, y = 60) 
password = Label(windows, text = "Password").place(x = 30, y = 90) 

#Tương tự như trên, các dòng mã sau đó tạo và định vị các nhãn và ô nhập liệu khác. 
e1 = Entry(windows).place(x = 95, y = 30) 
e2 = Entry(windows).place(x = 95, y = 60) 
e3 = Entry(windows).place(x = 95, y = 90) 

windows.mainloop() 
