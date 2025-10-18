# Secure Password Generator (CLI)

A small, secure password generator written in Python using `secrets`, `argparse`, and `pathlib`.  
It supports three modes: **Poor (1)**, **Normal (2)**, **Strong (3)**.

## Features
- `--type {1,2,3}` to choose strength (Poor/Normal/Strong)
- `--length N` password length (> 0)
- `--count N` number of passwords (> 0)
- `--print-all` print all generated passwords to the console
- `--no-file` skip writing the output file
- `--output PATH` custom output path (file or directory)
- Auto-saves to Desktop/Home with a timestamped filename

> **Note:** Because the file name contains a space, wrap it in quotes when running:
> `python3 "Password Generator.py" ...`

## Requirements
- Python **3.10+**

## Usage

### Linux / macOS
```bash
python3 "Password Generator.py" --type 3 --length 16 --count 5 --print-all
