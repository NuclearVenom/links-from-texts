import tkinter as tk
from tkinter import messagebox
import subprocess
import re

def extract_links_from_text(text):
    # Find all http/https links
    links = re.findall(r'https?://[^\s>]+', text)
    return list(set(links))  # remove duplicates

def write_links_to_file(links, file_name='links.txt'):
    with open(file_name, 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')

def run_node_script(script='link_opener.js'):
    try:
        node_path = r"C:\Program Files\nodejs\node.exe"  # Change if needed
        subprocess.run([node_path, script], check=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Node.js not found. Check the path in your script.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Node.js Error", str(e))

def on_open_button():
    text = text_box.get("1.0", tk.END)
    if not text.strip():
        messagebox.showwarning("Empty", "Please paste some text.")
        return

    links = extract_links_from_text(text)

    if not links:
        messagebox.showinfo("No Links Found", "No links were found in the pasted text.")
        return

    write_links_to_file(links)
    run_node_script()

# GUI setup
root = tk.Tk()
root.title("Paste WhatsApp Text to Open Links")
root.geometry("600x400")

label = tk.Label(root, text="Paste your WhatsApp messages below:")
label.pack(pady=10)

text_box = tk.Text(root, wrap=tk.WORD, height=15, width=70)
text_box.pack(padx=10)

open_button = tk.Button(root, text="Open Links", command=on_open_button, width=20, height=2)
open_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=10)
exit_button.pack()

root.mainloop()
