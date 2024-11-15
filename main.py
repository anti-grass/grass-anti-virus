import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

def scan_folder():
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showwarning("Input Error", "Please select a folder to scan.")
        return
    
    files_scanned = 0
    files_with_grass = []
    
    total_files = sum([len(files) for _, _, files in os.walk(folder_path)])
    progress_bar['maximum'] = total_files

    for root_dir, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.readlines()  # Read file line by line
                    for line_number, line in enumerate(content, start=1):
                        char_positions = [i for i in range(len(line)) if line.startswith("grass", i)]
                        if char_positions:
                            for char_pos in char_positions:
                                files_scanned += 1
                                files_with_grass.append((file_path, line_number, line.strip(), char_pos))
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
            
            progress_bar['value'] += 1
            root.update_idletasks()

    log_file_path = os.path.join(os.getcwd(), "log.txt")

    with open(log_file_path, "w") as log_file:
        for file_path, line_number, line, char_pos in files_with_grass:
            log_file.write(f"Found 'grass' in:\n"
                           f"Directory: {os.path.dirname(file_path)}\n"
                           f"File: {os.path.basename(file_path)}\n"
                           f"Line {line_number}: {line}\n"
                           f"Character Position: {char_pos + 1}\n\n")

    if files_with_grass:
        result_text = "\n".join([f"Found 'grass' in:\n"
                                f"Directory: {os.path.dirname(file_path)}\n"
                                f"File: {os.path.basename(file_path)}\n"
                                f"Line {line_number}: {line}\n"
                                f"Character Position: {char_pos + 1}\n"
                                for file_path, line_number, line, char_pos in files_with_grass[:2]])

        messagebox.showinfo("Scan Complete", f"Found 'grass' in {len(files_with_grass)} instances.\n\n"
                                            f"First 2 results:\n\n{result_text}\n\nFor more results, the log is saved at: {log_file_path}")
    else:
        messagebox.showinfo("Scan Complete", f"No instances of 'grass' found in any files.\n\nLog saved at: {log_file_path}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

root = tk.Tk()
root.title("Grass Anti Virus")
root.geometry("500x350")
root.config(bg="#2e2e2e")
root.resizable(False, False)

label_font = ('Helvetica', 14)
button_font = ('Helvetica', 12)
button_style = {'font': button_font, 'relief': "flat", 'width': 15, 'height': 2}

title_label = tk.Label(root, text="Grass Anti Virus", font=('Helvetica', 18, 'bold'), bg="#212121", fg="white", pady=20)
title_label.pack(fill="x")

folder_path_var = tk.StringVar()
folder_label = tk.Label(root, text="Select a folder to scan:", font=label_font, bg="#2e2e2e", fg="white")
folder_label.pack(pady=10)

folder_button = tk.Button(root, text="Browse", command=browse_folder, bg="#4CAF50", fg="white", relief="flat", width=15, height=2)
folder_button.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=20)

scan_button = tk.Button(root, text="Scan", command=scan_folder, bg="#2196F3", fg="white", relief="flat", width=15, height=2)
scan_button.pack(pady=20)

root.mainloop()