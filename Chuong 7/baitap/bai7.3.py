import tkinter as tk
from tkinter import font

def change_label_font(label, font_name, font_weight, font_size):
    new_font = tk.font.Font(family=font_name, weight=font_weight, size=font_size)
    label.config(font=new_font)

def main():
    # Tạo cửa sổ
    window = tk.Tk()
    window.title("Thay đổi phông chữ của nhãn")

    # Tạo nhãn
    label = tk.Label(window, text="Chào mừng bạn đến với GUI Tkinter!")

    # Đặt mặc định cho font
    default_font = tk.font.nametofont("TkDefaultFont")
    default_font_size = default_font.actual()["size"]

    # Tạo nút để thay đổi phông chữ nhãn
    change_font_button = tk.Button(window, text="Thay đổi Phông Chữ", command=lambda: change_label_font(label, font_name.get(), font_weight.get(), font_size.get()))

    # Tạo các Entry để nhập thông tin về phông chữ
    font_name_label = tk.Label(window, text="Tên Phông Chữ:")
    font_name = tk.Entry(window)

    font_weight_label = tk.Label(window, text="Đậm (normal, bold):")
    font_weight = tk.Entry(window)

    font_size_label = tk.Label(window, text="Kích Thước Phông Chữ:")
    font_size = tk.Entry(window)
    font_size.insert(0, str(default_font_size))  # Đặt giá trị mặc định là kích thước phông chữ hiện tại

    # Bố trí các thành phần trên cửa sổ
    label.pack(pady=10)
    change_font_button.pack(pady=10)
    font_name_label.pack(pady=5)
    font_name.pack(pady=5)
    font_weight_label.pack(pady=5)
    font_weight.pack(pady=5)
    font_size_label.pack(pady=5)
    font_size.pack(pady=5)

    # Chạy vòng lặp chính của cửa sổ
    window.mainloop()

if __name__ == "__main__":
    main()
