
# GUI Form Autofill Bot

## Description:
This project automatically fills in information on a form at [demoqa.com](https://demoqa.com/automation-practice-form), submits the form, and takes a screenshot of the result. It uses **Playwright** for browser automation and **Faker** to generate random data for the form fields.

## Installation:

To install and run the project, follow these steps:

### 1. **Create a Virtual Environment** (recommended):
Before installing the required libraries, you can create a virtual environment to manage the dependencies efficiently:

- Create a virtual environment:
  ```bash
  python3 -m venv venv
  ```

- Activate the virtual environment:
  - On **Windows**:
    ```bash
    venv\Scripts\ctivate
    ```
  - On **MacOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 2. **Install the Required Libraries**:
Run the following command to install all the necessary libraries from **`requirements.txt`**:
```bash
pip install -r requirements.txt
```

### 3. **Install Playwright**:
After installing the libraries from **`requirements.txt`**, you need to install the Playwright browsers (Chromium, Firefox, WebKit):
```bash
playwright install
```

### 4. **Check Playwright Version**:
After installation, you can verify that Playwright is installed successfully by running the command:
```bash
playwright --version
```
If the command runs successfully and displays the version of Playwright, you have installed it correctly.

## Usage:

1. **Run the Autofill Form**:
   - Once the installation is complete, you can run the script to automatically fill in the form and take a screenshot of the result:
   ```bash
   python3 src/report.py --num help
   ```

   - Each time you run this, a screenshot of the form after submission will be saved.

2. **Run Tests**:
   - If you want to run automated tests to check if the `autofill_form()` function works as expected, you can use **pytest**:
   ```bash

   pytest tests/test_autofill_form.py
   ```

   This will ensure that the functions of the project are working correctly.

## Project Structure:

```
gui_form_autofill_bot/
│
├── src/                           # Main source code
│   ├── __init__.py                # Initialize src as a package
│   ├── autofill_form.py           # Autofill form automation
│   └── report.py                  # Report generation (CSV)
│
├── tests/                         # Test cases
│   └── test_autofill_form.py      # Automated tests
│
├── docs/                          # Project documentation
│   └── README.md                  # Project guide and description
│
├── .gitignore                     # Files to exclude from Git
├── requirements.txt               # Required libraries to install
└── setup.py                       # Optional packaging for the project
```

## Required Libraries:

The project requires the following libraries:

- **Playwright**: Used for browser automation.
- **Faker**: Used to generate random data for the form.
- **pytest**: Used for writing and running test cases.
- **pytest-playwright**: pytest plugin to integrate Playwright with pytest.

These libraries are listed in the `requirements.txt` file, and you can install them by running:
```bash
pip install -r requirements.txt
```

## Troubleshooting:

- **"Executable doesn't exist" Error**:
  If you encounter the error after installing Playwright and running the script:
  ```
  Error when submitting form: BrowserType.launch: Executable doesn't exist
  ```
  Make sure you have run **`playwright install`** to download the necessary Playwright browsers (Chromium, WebKit, Firefox):
  ```bash
  playwright install
  ```

- **"command not found" Error**:
  If you encounter the error when running **`playwright --version`**:
  ```bash
  playwright: command not found
  ```
  You need to add **`~/.local/bin`** to your **`PATH`**. Open your shell configuration file (e.g., `.bashrc` or `.zshrc`) and add the following line:
  ```bash
  export PATH=$PATH:/home/nam/.local/bin
  ```
  Then, reload the shell configuration:
  ```bash
  source ~/.bashrc  # If using Bash
  # Or
  source ~/.zshrc   # If using Zsh
  ```

## Customization:
- You can easily modify **`autofill_form.py`** to change the data being filled into the form or add new features.

---

##  Contact:
- **Author**: [NamDV36]
- **Email**: [NamDV36@fpt.com]

## References:
- [Playwright](https://playwright.dev/)
- [Faker](https://faker.readthedocs.io/en/master/)
- [pytest](https://docs.pytest.org/en/stable/)
- [pytest-playwright](https://pytest-playwright.readthedocs.io/en/latest/)