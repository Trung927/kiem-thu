* **Điều đã học được:**
  * Lần đầu tiên tự viết và chạy thành công một kịch bản kiểm thử tự động Web bằng Selenium và pytest.
  * Hiểu cơ chế phân biệt các file hệ thống do Python/pytest tự sinh ra như `__pycache__` hay `.pytest_cache` để tránh đẩy lên GitHub.
  * Hiểu cách pytest báo lỗi khi mình cố ý sửa sai câu lệnh `assert`.

* **Trả lời câu hỏi đọc tài liệu:**
  * **Câu 1:** *Một script Selenium gồm những bước nào, tương ứng dòng nào?*
    - Bước 1: Khởi tạo trình duyệt (`driver = webdriver.Chrome()`)
    - Bước 2: Điều hướng đến trang web (`driver.get("https://the-internet.herokuapp.com/")`)
    - Bước 3: Thao tác/Lấy dữ liệu (`actual_title = driver.title`)
    - Bước 4: Kiểm tra kết quả kỳ vọng (`assert actual_title == "The Internet"`)
    - Bước 5: Đóng trình duyệt (`driver.quit()`)
  * **Câu 2:** *pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?*
    - pytest tìm các tệp tin có tên dạng `test_*.py` hoặc `*_test.py` và các hàm bắt đầu bằng `test_*`.

* **Nhật ký sử dụng AI:**
  * **Nội dung đã hỏi:** Hỏi cách cố ý làm cho bài test bị sai để xem thông báo lỗi FAILED của pytest.
  * **Đánh giá câu trả lời:** ĐÚNG. AI hướng dẫn đổi chuỗi kỳ vọng từ `"The Internet"` thành `"The Internet 123"`.
  * **Kiến thức hiểu thêm:** Nhận biết được cấu trúc thông báo lỗi `AssertionError` của pytest để phục vụ việc debug sau này.