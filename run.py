import random, os, subprocess, requests, sys, re
from urllib.parse import quote

project = "your project name"
whatsapp = "your nunber whatsapp"
link = "https://license-key.000webhostapp.com/chek.php"
url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="

def dump_license(intel):
	lis = list("abcdefghijklmnopqrstuvwxyz1234567890")
	xx = [random.choice(lis) for _ in range(intel)]
	return "".join(xx).upper()

def get_license(key):
	cek = requests.get(link+"?project="+project+"&apikey="+key).json()
	if cek["status"] == "error":
		exit("[!] Your key is invalid, please contact admin")
	elif cek["status"] == "expired":
		exit("[!] Your key is expired, please contact admin")
	else:
		open("license.txt","w").write(key)
		return "valid!!", cek["urls"]

def daftar():
	digit_key = random.choice([15,20,25,30])
	digit_key = dump_license(digit_key)

	print("[+] Your key: "+digit_key)
	print("-"*30)
	print("""[1] DAFTAR APIKEY PREMIUM
[2] DAFTAR APIKEY TRIAL
[3] RUN KEY NOW
[0] EXIT""")
	print("-"*30)
	pil = input("[?] choose: ")
	while pil == "":
		print("[!] don't be empty")
		pil = input("[?] choose: ")
	if pil == "1":
		mail = input("\n[?] EMAIL: ")
		name = input("[?] NAME : ")
		tks = "hello admin, please confirm my key to premium :)\n\n"+"* email: "+mail+"\n* nama: "+name+"\n* key: "+digit_key
		subprocess.check_output(["am", "start", url_wa+quote(tks)])
	elif pil == "2":
		mail = input("\n[?] EMAIL: ")
		name = input("[?] NAME : ")
		tks = "hello admin, please confirm my key to trial :)\n\n"+"* email: "+mail+"\n* nama: "+name+"\n* key: "+digit_key
		subprocess.check_output(["am", "start", url_wa+quote(tks)])
	elif pil == "3":
		key = input("[=] Input key: ")
		while key == "":
			print("[!] don't be empty")
			key = input("[=] Input key: ")
		sts, urls = get_license(key)
		if "valid!!" in sts:
			exec(requests.get(urls).text)
		sys.exit()
	else:
		exit("[×] Options not found")

if __name__ == "__main__":
	os.system("clear")

	try:
		xdg = open("license.txt","r").read()
		xdg_find = re.search("[a-z-A-Z-0-9]+", str(xdg))
		if xdg is None:
			os.remove("license.txt")
			daftar()
		else:
			sts, urls = get_license(xdg_find.group(0))
			if "valid!!" in sts:
				exec(requests.get(urls).text)
			else:
				exit("[!] Cookies invalid")
	except:
		daftar()