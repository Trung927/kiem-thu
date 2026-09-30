import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_title_and_heading_trung():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    try:
        # 1. Truy cập trang web
        driver.get("https://the-internet.herokuapp.com/")
        
        # 2. Kiểm tra tiêu đề tab trình duyệt
        assert driver.title == "The Internet", f"Kỳ vọng 'The Internet', thực tế: '{driver.title}'"
        
        # 3. Kiểm tra tiêu đề h1 trên trang
        heading_text = driver.find_element(By.TAG_NAME, "h1").text
        assert heading_text == "Welcome to the-internet", f"Thẻ h1 thực tế: '{heading_text}'"
        
        print("\n[TRUNG - PASS] Kiểm thử tiêu đề trang thành công!")
    finally:
        driver.quit()