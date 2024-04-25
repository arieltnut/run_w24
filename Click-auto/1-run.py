import os
import subprocess
import time
from telegram import Bot  # Assuming you'll use this for Telegram integration

def open_files():
    files_to_open = 1  # Number of files to open sequentially
    directory = r"C:\uChrome"
    auto_click_path = r"C:\Users\dell\PycharmProjects\Click-auto\auto-click.exe"

    # Function to check if a process is running
    def check_process_running(process_name):
        output = subprocess.check_output(["tasklist", "/fi", f"imagename eq {process_name}"]).decode("utf-8")
        return process_name in output

    # Count the number of .lnk files
    lnk_files = [filename for filename in os.listdir(directory) if filename.endswith(".lnk")]
    num_lnks = len(lnk_files)
    send_telegram_notification(f"Number of .lnk files: {num_lnks}")

    count = 0
    for index, filename in enumerate(lnk_files, start=1):
        send_telegram_notification(f"Opening file {index}/{num_lnks}: {filename}")
        os.startfile(os.path.join(directory, filename))
        subprocess.Popen([auto_click_path])  # Execute auto-click.exe
        send_telegram_notification("auto-click.exe has been executed.")
        count += 1
        send_telegram_notification("File opened successfully.")
        # Check and wait until the required number of files are opened
        if count >= files_to_open:
            while True:
                if not check_process_running("chrome.exe"):
                    count = 0  # Reset count
                    break  # Exit the while loop
                time.sleep(1)  # Wait 1 second before checking again


def close_chrome():
    # Use os.system to execute the taskkill command
    os.system('taskkill /F /IM chrome.exe /T')
    time.sleep(1)  # Wait for 1 second before further checks
    send_telegram_notification("Chrome has been closed.")

def send_telegram_notification(message):
    # Implement sending notification via Telegram here
    print(message)  # For demonstration purposes

if __name__ == "__main__":
    close_chrome()
    open_files()
