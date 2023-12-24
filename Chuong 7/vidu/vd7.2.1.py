import sys 
from PyQt5.QtWidgets import QApplication, QLabel, QWidget 
# Khởi tạo ứng dụng
app = QApplication(sys.argv) 
# Tạo một cửa sổ
window = QWidget() 
window.setWindowTitle('Hello World!') 
# Thêm các thành phần vào cửa sổ
label = QLabel(window) 
label.setText('Hello World!') 
label.move(50, 50) 
# Hiển thị cửa sổ
window.show() 
# Chạy vòng lặp ứng dụng
sys.exit(app.exec_()) 