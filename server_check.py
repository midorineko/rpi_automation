import requests
import time

hub_name = "inouyehub"

site = "http://%s.localtunnel.me" % hub_name
open_hub = """x-terminal-emulator -e 'bash -c "lt --port 3000 --subdomain %s"'""" % hub_name

def check():
    try:
        r = requests.head(site)
        print(r.status_code)
        if r.status_code != 200:
            import subprocess
            import shlex
            process = subprocess.Popen(
                shlex.split("""x-terminal-emulator -e 'bash -c "node /home/pi/rpi_automation/app.js"'"""), stdout=subprocess.PIPE)
           

            print (process.returncode)
            process2 = subprocess.Popen(
                shlex.split(open_hub), stdout=subprocess.PIPE)
            
            print (process2.returncode)
    except requests.ConnectionError:
        print("failed to connect")

x=1
while x > 0:
    check()
    time.sleep(300)
