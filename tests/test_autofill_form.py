import pytest
from src.autofill_form import autofill_form

def test_autofill_form_success():
    status = autofill_form()  # Kiểm tra nếu hàm autofill_form chạy thành công
    assert status == 'Success'

def test_autofill_form_fail():
    # Giả sử có lỗi trong quá trình gửi form
    status = autofill_form()  
    assert status == 'Failed'
