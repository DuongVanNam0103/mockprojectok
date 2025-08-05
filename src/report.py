import csv
import time
import argparse
from playwright.sync_api import sync_playwright
from autofill_form import autofill_form

def create_csv_report(num_runs):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        writer = None
        with open('form_submission_report.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Submission Number", "Time", "Status", "Elapsed Time"])

            for i in range(num_runs):
                page.goto("https://demoqa.com/automation-practice-form", timeout=60000)
                start_time = time.time()
                status = autofill_form(page)   # <-- truyền page vào đây
                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_time_str = f"{elapsed_time:.2f} seconds"

                writer.writerow([
                    i + 1,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)),
                    status,
                    elapsed_time_str
                ])
                print(f"Submission {i + 1} - {status} - Time taken: {elapsed_time_str}")
        page.close()
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-fill form multiple times and report.")
    parser.add_argument('-n', '--num', type=int, default=10, help="so lan muon test (default: 10)")
    args = parser.parse_args() 

    create_csv_report(args.num)
