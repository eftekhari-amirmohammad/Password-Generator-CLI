# Secure Password Generator (CLI)

A small, secure password generator written in Python using `secrets`, `argparse`, and `pathlib`.  
It supports three modes: **Poor (1)**, **Normal (2)**, **Strong (3)**.

> **Note:** The file name contains a space. Always wrap it in quotes:
> `python3 "Password Generator.py"` or `py "Password Generator.py"`.

---

## Features
- `--type {1,2,3}` **choose strength** (1=Poor, 2=Normal, 3=Strong)
- `--length N` **password length** (> 0)
- `--count N` **number of passwords** (> 0)
- `--print-all` **print all** generated passwords to the console
- `--no-file` **skip writing** the output file
- `--output PATH` **custom output path** (directory or file)
- **Auto-saves** to Desktop/Home with a **timestamped** filename

---

## Requirements
- Python **3.10+**

---

## Quick Start (All OS in one place)
```bash
# Pick the right runner for your OS:
#   Windows (PowerShell / CMD):  py "Password Generator.py" --help
#   Linux / macOS (Terminal):    python3 "Password Generator.py" --help
