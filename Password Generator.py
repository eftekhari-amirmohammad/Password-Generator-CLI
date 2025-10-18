from pathlib import Path
import secrets
import string
from datetime import datetime
import argparse
import sys


LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#~$%^&*()_+=-\\|?/>.<,`"

ALPHABETS = {
    "1": ("Poor",   LOWER),
    "2": ("Normal", LOWER + UPPER + DIGITS),
    "3": ("Strong", LOWER + UPPER + DIGITS + SYMBOLS),
}

def parse_args():
    p = argparse.ArgumentParser(description="---Secure password generator---")
    p.add_argument("--type", choices=["1","2","3"], required=True, help="1=Poor, 2=Normal, 3=Strong")
    p.add_argument("--length", type=positive_int, required=True, help="Password length (>0)")
    p.add_argument("--count", type=positive_int, default=1, help="How many passwords (default: 1)")
    p.add_argument("--print-all", action="store_true", help="Print all passwords to console")
    p.add_argument("--no-file", action="store_true", help="Do not write to file")
    p.add_argument("--output", type=str, help="Custom output path (file or directory)")
    return p.parse_args()



def positive_int(value: str) -> int:
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer.")
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Must be > 0.")
    return ivalue


def generate_passwords(alphabet: str, length: int, count: int) -> list[str]:
    
    return [
        "".join(secrets.choice(alphabet) for _ in range(length))
        for _ in range(count)
    ]

def desktop_path() -> Path:
    home = Path.home()
    desk = home / "Desktop"
    return desk if desk.exists() else home

def main():

    args = parse_args()
    label, alphabet = ALPHABETS[args.type]
    passwords = generate_passwords(alphabet, args.length, args.count)
    
    if args.print_all:
        print("\n".join(passwords))
    else:
        print("(showing 1)")
        print(passwords[0])
    
    if not args.no_file:
        if args.output:
            out_path = Path(args.output)
            if out_path.is_dir():
                ts = datetime.now().strftime("%Y%m%d-%H%M%S")
                out_file = out_path / f"{label} Passwords {ts}.txt"
            else:
                out_file = out_path
        else:
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            out_file = (desktop_path() / f"{label} Passwords {ts}.txt")

        out_file.write_text("\n".join(passwords), encoding="utf-8")
        print(f"\nSaved: {out_file}")


if __name__ == "__main__":
    main()
