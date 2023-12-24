import json
import datetime

# Tạo danh sách để lưu trữ các giao dịch
transactions = []

while True:
    # Người dùng nhập thông tin giao dịch
    amount = float(input("Nhập số tiền giao dịch: "))
    type_of_transaction = input("Loại giao dịch (Tiền/Vàng): ")
    
    # Thêm thông tin giao dịch vào danh sách
    transaction = {
        "amount": amount,
        "type": type_of_transaction
    }
    transactions.append(transaction)
    
    # Hỏi người dùng có muốn tiếp tục giao dịch không
    continue_transaction = input("Tiếp tục giao dịch? (Y/N): ")
    if continue_transaction.lower() != 'y':
        break

# Hỏi người dùng có muốn ghi vào tập tin JSON không
write_to_file = input("Bạn muốn ghi vào tập tin JSON? (1: Có, 0: Không): ")
if write_to_file == '1':
    # Lấy thông tin ngày hiện tại theo định dạng nam-thang-ngay-gio-phut-giay
    current_time = datetime.datetime.now()
    filename = current_time.strftime("%Y-%m-%d-%H-%M-%S") + ".json"
    
    # Lưu danh sách giao dịch vào tập tin JSON
    with open(filename, "w") as json_file:
        json.dump(transactions, json_file)
        print(f"Dữ liệu giao dịch đã được lưu vào tệp {filename}.")
else:
    print("Không ghi dữ liệu giao dịch vào tập tin JSON.")
