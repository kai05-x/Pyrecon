import tkinter as tk
from tkinter import font, messagebox
import directory_listing as dl
import subdomain_finder as sf
import status_code as sc
import whois as wi
# Define buttons as global variables
btn_subdomain = None
btn_status_code = None
btn_directory_listing = None
btn_whois = None

def start():
    global btn_subdomain, btn_status_code, btn_directory_listing, btn_whois

    # Change main window background color to black
    root.configure(bg="black")

    # Change the color of the buttons to green and fix their size
    button_width = 20
    button_height = 2
    for btn in [btn_subdomain, btn_status_code, btn_directory_listing, btn_whois]:
        if btn:
            btn.configure( width=button_width, height=button_height)

    # Minimize the main window
    root.iconify()

    # Create a new window for options
    options_window = tk.Toplevel(root)
    options_window.title("Options")
    options_window.geometry("600x400")
    # Step one: Add image as background
    background_label = tk.Label(options_window, bg="black")
    background_label.place(relwidth=1, relheight=1)


    # Set font style to Roboto
    font_style = font.Font(family="Roboto", size=12)



    # Create buttons for each option
    btn_subdomain = tk.Button(options_window, text="Subdomain Finder",bg="light blue", command=sf.create_gui, font=font_style, width=button_width, height=button_height)
    btn_status_code = tk.Button(options_window, text="Status Code", bg="light green", command=sc.main, font=font_style, width=button_width, height=button_height)
    btn_directory_listing = tk.Button(options_window, text="Directory Listing", bg="light blue", command=dl.run_program, font=font_style, width=button_width, height=button_height)
    btn_whois = tk.Button(options_window, text="Whois", bg="light green", command=wi.main1, font=font_style, width=button_width, height=button_height)

    # Place buttons in the options window
    btn_subdomain.pack(pady=25)
    btn_status_code.pack(pady=25)
    btn_directory_listing.pack(pady=25)
    btn_whois.pack(pady=25)
# Create main window
root = tk.Tk()
root.title("Pyrecon GUI")

# Load image
background_image = tk.PhotoImage(file="C:\\Users\\tiwar\\Desktop\\pyrecon\\domain\\hud-screen-sci-fi-cyber-black-white-background_115968-176.png")
# Set screen size to a bigger frame
root.geometry("600x400")
# Prevent window resizing
root.resizable(False, False)

# Set font style to Roboto
font_style = font.Font(family="Roboto", size=19)

# Step one: Add image as background
background_label = tk.Label(root, image=background_image, bg="black")
background_label.place(relwidth=1, relheight=1)

# Step two: Write "Welcome to Pyrecon"
welcome_label = tk.Label(root, text="Welcome to Pyrecon", font=font_style, fg="white", bg="black")
welcome_label.pack(pady=9)

# Step three: Add start button with green color
start_button = tk.Button(root, text="Start", command=start, bg="light green", font=font_style)
start_button.pack(pady=120)

# Run the application
root.mainloop()
