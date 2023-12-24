import tkinter as tk

def submit_form():
    student_name = name_entry.get()
    student_id = id_entry.get()
    password = password_entry.get()

    # Kiểm tra xem tất cả các trường đã được điền đầy đủ
    if student_name and student_id and password:
        result_label.config(text=f"Đã nhận thông tin:\nTên: {student_name}\nID: {student_id}\nMật khẩu: {password}")
    else:
        result_label.config(text="Vui lòng điền đầy đủ thông tin.")

def main():
    # Tạo cửa sổ
    window = tk.Tk()
    window.title("Form Đăng Ký Sinh Viên")

    # Tạo các Entry (hộp văn bản) cho tên, ID và mật khẩu
    name_label = tk.Label(window, text="Tên sinh viên:")
    name_entry = tk.Entry(window)

    id_label = tk.Label(window, text="ID sinh viên:")
    id_entry = tk.Entry(window)

    password_label = tk.Label(window, text="Mật khẩu:")
    password_entry = tk.Entry(window, show="*")

    # Tạo nút "Gửi"
    submit_button = tk.Button(window, text="Gửi", command=submit_form)

    # Hiển thị kết quả sau khi gửi
    result_label = tk.Label(window, text="")

    # Bố trí các thành phần trên cửa sổ
    name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    id_entry.grid(row=1, column=1, padx=10, pady=5)

    password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Chạy vòng lặp chính của cửa sổ
    window.mainloop()

if __name__ == "__main__":
    main()
