import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from urllib.parse import urljoin

def directory_lister(target_domain, wordlist_path, output_file):
    try:
        with open(wordlist_path, 'r') as f:
            wordlist = f.read().splitlines()
    except FileNotFoundError:
        messagebox.showerror("Error", f"Wordlist file '{wordlist_path}' not found.")
        return

    # Determine output file path
    if output_file:
        output_path = output_file
    else:
        output_path = "dir_output.txt"

    with open(output_path, 'w') as out_file:
        for word in wordlist:
            url = urljoin(target_domain, word)
            print(f"Checking URL: {url}")  # Debugging: Print the URL being checked
            try:
                response = requests.head(url, allow_redirects=True)  # Use HEAD request and allow redirects

                if response.status_code in (200, 301, 302):
                    print(f"URL exists: {url}")
                    out_file.write(url + '\n')
                elif response.status_code == 404:
                    print(f"URL does not exist: {url}")
                else:
                    print(f"Unexpected status code for {url}: {response.status_code}")
            except requests.exceptions.MissingSchema:
                messagebox.showerror("Error", f"Invalid URL: {url}. Please make sure the target domain includes a valid scheme (e.g., 'http://' or 'https://').")
                return  # Terminate the function upon encountering an error

    messagebox.showinfo("Success", f"Directory listing completed successfully. Output saved in '{output_path}'.")

def browse_wordlist():
    wordlist_path = filedialog.askopenfilename()
    if wordlist_path:
        entry_wordlist.delete(0, tk.END)
        entry_wordlist.insert(0, wordlist_path)

def browse_output():
    output_file = filedialog.asksaveasfilename()
    if output_file:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_file)

def run_directory_lister():
    target_domain = entry_domain.get()
    wordlist_path = entry_wordlist.get()
    output_file = entry_output.get()

    directory_lister(target_domain, wordlist_path, output_file)

def run_program():
    # Create main window
    root = tk.Tk()
    root.title("Directory Lister")
    root.geometry("600x400")
    root.resizable(False, False)
    root.configure(bg="black")

    # Add notes in the top corner
    note1 = tk.Label(root, text="* Target domain you input includes the correct scheme (e.g., 'https://' or 'http://')", bg="black", fg="white")
    note1.pack(anchor="nw", padx=10, pady=10)

    note2 = tk.Label(root, text="* It's optional to provide output file path", bg="black", fg="white")
    note2.pack(anchor="nw", padx=10)

    # Create and place widgets
    label_domain = tk.Label(root, text="Target Domain:", bg="black", fg="white")
    label_domain.pack(pady=10)

    global entry_domain
    entry_domain = tk.Entry(root)
    entry_domain.pack()

    label_wordlist = tk.Label(root, text="Wordlist Path:", bg="black", fg="white")
    label_wordlist.pack(pady=10)

    global entry_wordlist
    entry_wordlist = tk.Entry(root)
    entry_wordlist.pack()

    button_browse_wordlist = tk.Button(root, text="Browse", bg="pink", command=browse_wordlist, width=16, height=1)
    button_browse_wordlist.pack(pady=5)

    label_output = tk.Label(root, text="Output File:", bg="black", fg="white")
    label_output.pack(pady=8)

    global entry_output
    entry_output = tk.Entry(root)
    entry_output.pack()

    button_browse_output = tk.Button(root, text="Browse", bg="pink", command=browse_output, width=16, height=1)
    button_browse_output.pack(pady=5)

    button_run = tk.Button(root, text="Start Scanning", bg="light green", command=run_directory_lister, width=18, height=2)
    button_run.pack(pady=10)

    try:
        # Run the Tkinter event loop
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

