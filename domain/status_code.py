import tkinter as tk
from tkinter import filedialog, font
import requests

def check_subdomains_from_file(file_path):
    existing_subdomains = []

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            subdomain = line.strip()
            url_http = f"http://{subdomain}"
            url_https = f"https://{subdomain}"
            try:
                response_http = requests.head(url_http, allow_redirects=True, verify=False)
                response_https = requests.head(url_https, allow_redirects=True, verify=False)

                if response_http.status_code in (200, 301, 302):
                    existing_subdomains.append((subdomain, response_http.status_code))
                    print(f"Subdomain exists (HTTP): {subdomain} ({response_http.status_code})")
                elif response_https.status_code in (200, 301, 302):
                    existing_subdomains.append((subdomain, response_https.status_code))
                    print(f"Subdomain exists (HTTPS): {subdomain} ({response_https.status_code})")
                else:
                    existing_subdomains.append((subdomain, "Not Found"))
                    print(f"Subdomain does not exist: {subdomain}")

            except requests.exceptions.RequestException as e:
                existing_subdomains.append((subdomain, "Error"))
                # Remove the print statement to prevent error message from being displayed
                # print(f"Error occurred for {subdomain}: {e}")
                continue

            except Exception as e:
                existing_subdomains.append((subdomain, "Error"))
                # Remove the print statement to prevent error message from being displayed
                # print(f"An unexpected error occurred for {subdomain}: {e}")
                continue

    return existing_subdomains

def start_scan(entry_location):
    file_path = entry_location.get()
    if not file_path:
        print("Please select a file.")
        return

    try:
        existing_subdomains = check_subdomains_from_file(file_path)
        output_file_path = "status_code_result.txt"

        with open(output_file_path, 'w') as file:
            unique_results = set(existing_subdomains)
            for subdomain, status_code in unique_results:
                file.write(f"{subdomain}: {status_code}\n")

        print("Status codes saved to:", output_file_path)
    except FileNotFoundError:
        print("File not found.")
        return

def browse_file(entry_location):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_location.delete(0, tk.END)
        entry_location.insert(0, file_path)

def main():
    root = tk.Tk()
    root.title("Subdomain Status Checker")
    root.geometry("600x400")
    root.configure(bg='black')
    root.resizable(False, False)
    font_style = font.Font(family="Roboto", size=19)

    note1 = tk.Label(root, text="* You can write a location or select from the system.", bg="black", fg="white")
    note1.pack(anchor="nw", padx=10, pady=10)

    label = tk.Label(root, text="Select a file containing subdomains:", font=font_style, bg='black', fg='white')
    label.pack(pady=20)

    entry_location = tk.Entry(root, font=font_style, width=20)
    entry_location.pack(pady=10)

    browse_button = tk.Button(root, text="Browse", bg="pink", command=lambda: browse_file(entry_location), width=16, height=2)
    browse_button.pack(pady=10)

    scan_button = tk.Button(root, text="Scan", bg="lightblue", command=lambda: start_scan(entry_location), width=16, height=2)
    scan_button.pack(pady=10)

    root.mainloop()


