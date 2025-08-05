import pytest
from playwright.sync_api import sync_playwright
from faker import Faker
import random
from datetime import datetime
import os

# GLOBAL SELECTORS
FIRSTNAME_FIELD = "input#firstName"
LASTNAME_FIELD = "input#lastName"
EMAIL_FIELD = "input#userEmail"
MOBILE_FIELD = "input#userNumber"
GENDER_OPTIONS = ["#gender-radio-1", "#gender-radio-2", "#gender-radio-3"]
HOBBY_OPTIONS = ["#hobbies-checkbox-1", "#hobbies-checkbox-2", "#hobbies-checkbox-3"]
ADDRESS_FIELD = "textarea#currentAddress"
DOB_FIELD = "input#dateOfBirthInput"  # Selector cho trường ngày sinh
SUBJECT = ["Math"]  # Ví dụ các môn học, "Physics", "Computer Science", "Biology", "Chemistry"
SUBJECT_FIELD = "#subjectsInput"
CLOSE = "#closeLargeModal"
URL = "https://demoqa.com/automation-practice-form"  # Global URL
IMAGE_PATH = "/home/nam/python/mock/src/image.jpg"
states = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }

    #Random state, then random city based on choosen state
state_choice = random.choice(list(states.keys())) 
city_choice = random.choice(states[state_choice])
# PYTEST FIXTURE
@pytest.fixture(scope="session")
# Đánh dấu hàm này là một fixture trong pytest, nghĩa là hàm này sẽ chuẩn bị (setup) một tài nguyên dùng chung cho các test.

# scope="session" nghĩa là fixture này chỉ được tạo một lần duy nhất cho toàn bộ phiên test. 
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # headless=True nếu muốn chạy ẩn
        yield browser
        browser.close()

@pytest.fixture
# Mặc định là scope="function", nghĩa là mỗi test function sẽ được tạo một instance page mới (tab mới).

# Dùng browser từ fixture ở trên làm đối số (pytest sẽ tự động inject browser).
def page(browser):
    page = browser.new_page()
    page.goto(URL, timeout=60000)
    yield page
    page.close()

# Take screenshot function
def take_screenshot(page, prefix="form_submission"):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/{prefix}_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    return screenshot_path

# Fill in personal info (name, email, mobile number)
def fill_personal_info(page, fake):
    page.fill(FIRSTNAME_FIELD, fake.first_name())
    page.fill(LASTNAME_FIELD, fake.last_name())
    page.fill(EMAIL_FIELD, fake.email())
    page.fill(MOBILE_FIELD, str(random.randint(1000000000, 9999999999)))

# Fill in Date of Birth
def fill_date_of_birth(page):
    # Tạo ngày sinh ngẫu nhiên
    birth_date = datetime(random.randint(1960, 2000), random.randint(1, 12), random.randint(1, 28))  # Giới hạn ngày trong tháng từ 1 đến 28
    formatted_date = birth_date.strftime("%d %b %Y")  # Định dạng ngày như "11 Feb 2013"
    # Điền vào trường Date of Birth
    page.fill(DOB_FIELD, formatted_date)
    
# Select subjects
def select_subjects(page):
    # Lặp qua list subject (ví dụ “Math”), click vào field subject, 
    # nhập text, đợi dropdown hiện rồi nhấn Enter để chọn.
    subjects_input = page.locator(SUBJECT_FIELD)
    for subject in SUBJECT:
        print(f"Filling subject: {subject}")
        subjects_input.click()
        page.wait_for_timeout(500)  # Wait after click
        subjects_input.type(subject, delay=50) 
        page.wait_for_timeout(1000)  # Wait for autocomplete dropdown
        subjects_input.press("Enter")
        page.wait_for_timeout(2000)  # Wait for subject to be added

# Pick random gender
def pick_gender(page):
    gender_choice = random.choice(GENDER_OPTIONS)
    page.locator(f"label[for='{gender_choice[1:]}']").click()

# Pick random hobby
def pick_hobby(page):
    hobby_choice = random.choice(HOBBY_OPTIONS)
    page.locator(f"label[for='{hobby_choice[1:]}']").click()

# Fill in address
def fill_address(page, fake):
    page.fill(ADDRESS_FIELD, fake.address())

# Upload picture
def upload_picture(page, image_path):
    # Sử dụng page.set_input_files để chọn ảnh từ hệ thống
    page.set_input_files("#uploadPicture", image_path)
    print(f"Uploaded picture: {image_path}")

# Select state and city
def select_state_and_city(page):
    # Click state dropdown
    page.locator("#state").click()
    page.wait_for_timeout(2000)  # Wait for dropdown to open
    
    # Select state option using text content
    print(f"Selecting state: {state_choice}")
    page.get_by_text(state_choice, exact=True).click()
    
    # Wait for city options to load after state selection
    page.wait_for_timeout(2000)
    
    # Click city dropdown
    page.locator("#city").click()
    page.wait_for_timeout(2000)  # Wait for city dropdown to open
    
    # Select city option using text content
    print(f"Selecting city: {city_choice}")
    page.get_by_text(city_choice, exact=True).click()

# Submit the form
def sumit_form(page):
    page.locator("#submit").click()

# Close modal window
def close_modal(page):
    page.evaluate("() => { document.querySelectorAll('#adplus-anchor,.adsbygoogle').forEach(el => el.remove()); }")
    page.locator(CLOSE).scroll_into_view_if_needed()
    page.locator(CLOSE).click()
    
# AUTOFILL FUNCTION
def autofill_form(page):
    fake = Faker("en_US")
    try:
          # Tạo thư mục screenshots nếu chưa tồn tại
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        select_subjects(page)
        select_state_and_city(page)
        fill_personal_info(page, fake)
        fill_date_of_birth(page)
        pick_gender(page)
        pick_hobby(page)
        fill_address(page, fake)
        # Tải lên ảnh (chỉ định đường dẫn của file ảnh)
        upload_picture(page,IMAGE_PATH) 
        sumit_form(page)
        take_screenshot(page)
        close_modal(page)
        return "Success"
    except Exception as e:
        print(f"Error send form: {e}")
        return "Failed"

# # ========== PYTEST TEST CASE ==========
# def test_autofill_form(page):
#     result = autofill_form(page)
#     assert result == "Success"
