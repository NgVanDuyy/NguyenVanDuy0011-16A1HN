import tkinter as tk

def main():
    # Tạo một cửa sổ
    window = tk.Tk()

    # Đặt tiêu đề cho cửa sổ
    window.title("Welcome to Uneti app")
    #Đặt kích thước cửa sổ theo pixels 
    window.geometry('280x60')

    # Tạo một nhãn và thêm vào cửa sổ
    label = tk.Label(window, text="Chào mừng bạn đến với GUI Tkinter!")
    label.pack(padx=20, pady=20)

    # Chạy vòng lặp chính của cửa sổ
    window.mainloop()

if __name__ == "__main__":
    main()
