import requests
import time

hub_name = "inouyehub5"
site = "http://%s.localtunnel.me" % hub_name
open_hub = """x-terminal-emulator -e 'bash -c "lt --port 3000 --subdomain %s"'""" % hub_name

def check():
    print('trying check')
    try:
        r = requests.head(site)
        if r.status_code != 200:
            import subprocess
            import shlex
            process1 =  subprocess.Popen(shlex.split("""x-terminal-emulator -e 'bash -c "node /home/pi/Desktop/rpi_automation/app.js"'"""), stdout=subprocess.PIPE)

	def pross2():
            v = requests.head("http://inouyehub5.localtunnel.me")
            print (v.status_code)
            if v.status_code != 200:
                process2 = subprocess.Popen(shlex.split(open_hub), stdout=subprocess.PIPE)
                time.sleep(2)
                z = requests.head("http://inouyehub5.localtunnel.me")
		print (z.status_code)
                if z.status_code != 200:
                  pross2()
	pross2()
	
    except requests.ConnectionError:
        print("failed to connect")

x=1
while x > 0:
    check()
    time.sleep(30)
