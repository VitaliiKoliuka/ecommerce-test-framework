import subprocess
import os

def pytest_sessionfinish(session, exitstatus):
    results_dir = "reports/allure-results"
    report_dir = "reports/allure-report"

    if not os.path.exists(results_dir) or not os.listdir(results_dir):
        print("No Allure results found. Skipping report generation.")
        return

    try:
        print("\nGenerating Allure report...")

        ALLURE_PATH = r"C:\allure\bin\allure.bat"

        subprocess.run([
            ALLURE_PATH, "generate",
            results_dir,
            "-o", report_dir,
            "--clean"
        ])

        print(f"Allure report generated at: {report_dir}")

    except FileNotFoundError:
        print("Allure CLI not installed or not in PATH. Skipping report generation.")