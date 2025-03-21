# 🔄 Smart File Sorter
Tired of messy folders full of PDFs, images, and random files?  
This lightweight Python script **automatically sorts your files into folders based on their type** — no more clutter, no manual effort!

✅ Simple to use  
✅ No extra installations needed  
✅ Works like magic using the `file` command

🎯 Just run the script, select your folder — and watch it organize itself!
---

## 📂 What It Does

This script scans through files in a selected folder, detects their file types (e.g., `PDF document`, `ASCII text`, `PNG image`, etc.), and moves each file into a corresponding subfolder.

For example:
Before: 
📁 MyDownloads/
├── resume.pdf
├── photo.png
├── notes.txt


After: 
📁MyDownloads/
├── PDF document/
│   └── resume.pdf
├── PNG image/
│   └── photo.png
├── ASCII text/
│   └── notes.txt



---

## 🚀 How to Run

1. Clone this repository or download the code:
   ```bash
   git clone https://github.com/YourUsername/smart-file-sorter.git
   cd smart-file-sorter

2.Run the script 
    python3 file_sorter.py

3.Enter the folder path when prompted:
    Enter the folder path: /Users/yourname/Downloads

##📦 Dependencies
No external libraries required.
Uses only Python standard library modules:

os
shutil
subprocess
re

##⚠️ Note: Works on Unix-based systems (Linux/macOS) that have the file command available.

##✨ Features

1.Detects file types dynamically using file command
2.Automatically creates subfolders for each type
3.Handles file/folder name spaces and special characters
4.Skips hidden files and directories
5.Clean and modular code

##💡 Ideas to Improve (Optional Future Enhancements)
1.Add command-line arguments (e.g., --dry-run, --verbose)
2.Add support for Windows (via mimetypes or magic library)
3.Add logging or summary report

##👩‍💻 Author
Pragya Richa
📫 richapragya003@gmail.com

⭐ Star this repo if you find it helpful!
