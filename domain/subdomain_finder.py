import tkinter as tk
from tkinter import font, filedialog
import requests

def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')

    valid_urls = []  # List to store valid URLs

    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:  # Check if URL is valid
                valid_urls.append(url)
                print(f'[+] {url}')
        except requests.ConnectionError:
            pass
    
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')

    # Writing valid URLs to a file
    with open('valid_urls.txt', 'w') as output_file:
        for url in valid_urls:
            output_file.write(url + '\n')

    print("Valid URLs saved to 'valid_urls.txt'")

def start_scanning(domain_entry, subdomain_key_entry):
    domain_name = domain_entry.get()
    subdomain_key_file = subdomain_key_entry.get()
    
    with open(subdomain_key_file, 'r') as file:
        name = file.read()
        sub_dom = name.splitlines()

    domain_scanner(domain_name, sub_dom)

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def create_gui():
    root = tk.Tk()
    root.title("Domain Scanner")
    root.geometry("600x400")
    root.resizable(False, False)
    root.configure(bg="black")

    # Add notes in the top corner
    note1 = tk.Label(root, text="* domain name not includes 'https://' or 'http://' ", bg="black", fg="white")
    note1.pack(anchor="nw", padx=10, pady=10)

    font_style = font.Font(family="Roboto", size=10)

    domain_label = tk.Label(root, text="Enter Domain Name:", font=font_style, fg="white", bg="black")
    domain_label.pack(pady=10)

    domain_entry = tk.Entry(root, font=font_style, bg="white")
    domain_entry.pack(pady=5)

    subdomain_key_label = tk.Label(root, text="Subdomain Key File Location:", font=font_style, fg="white", bg="black")
    subdomain_key_label.pack(pady=10)

    subdomain_key_entry = tk.Entry(root, font=font_style, bg="white")
    subdomain_key_entry.pack(pady=5)

    browse_button = tk.Button(root, text="Browse" ,width=16, height=1, command=lambda: browse_file(subdomain_key_entry), bg= "pink", font=font_style )
    browse_button.pack(pady=10)

    start_button = tk.Button(root, text="Start Scanning", width=18, height=2 ,command=lambda: start_scanning(domain_entry, subdomain_key_entry), font=font_style, bg="light green")
    start_button.pack(pady=20)

    root.mainloop()

