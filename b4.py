medical_record = input("Nhập mã bệnh nhân: ")
temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))

print("--- KẾT QUẢ CHUẨN ĐOÁN DỮ LIỆU ---")
print(f"Mã bệnh nhân: {medical_record}")
print(f"Nhiệt độ cơ thể: {temperature} độ C")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(temperature)}")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}")
print("------------------------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối")

# (1) Phân tích và Đề xuất giải pháp
# input: mã bệnh nhân, nhiệt độ cơ thể, nhịp tim
# output: thông tin kết quả chuẩn đoán dữ liệu và kiểm tra dữ liệu nhập vào

# Giải pháp thứ nhất :
    # Cho người dùng nhập dữ liệu vào r mới ép kiểu dữ liệu mong muốn
        # Số lượng biến cần nhiều hơn
        # cú pháp dài dòng hơn
        # Khả năng debug khó hơn
# Giải pháp thứ hai:
    # Ép ngay từ lúc cho người dùng nhập 
        # Số lượng biến cần ít hơn
        # cú pháp ngắn gọn hơn 
        # Khả năng debug dễ hơn 
# ---> Giải pháp thứ 2