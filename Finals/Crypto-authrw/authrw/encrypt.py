#!/usr/bin/env python
import os, sys
from Crypto.Cipher import AES

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'

iv = open("iv.txt").read()
key = open("key.txt").read()

def pad(m):
    padbyte = 16 - (len(m) % 16)
    s = m + padbyte*chr(padbyte)
    print(s)
    print(len(s))
    return s

def unpad(m):
    lastchar = ord(m[-1])
    return m[:-lastchar]

def _encrypt(message, iv, key):
    message = pad(message)
    obj1 = AES.new(key, AES.MODE_CBC, iv)
    return obj1.encrypt(message)

def _decrypt(ciphertext, iv, key):
    obj1 = AES.new(key, AES.MODE_CBC, iv)
    return unpad(obj1.decrypt(ciphertext))

def register(username):
    global iv, key
    username = "username=" + username + ":role=ordinary"
    print(username.encode('hex'))
    print(username)
    print(len(username))
    cookie = iv + _encrypt(username, iv, key)
    return cookie.encode("hex")

def login(cookie):
    cookie = cookie.decode("hex")
    iv = cookie[:16]

    print(iv.encode('hex'))
    global key
    ciphertext = cookie[16:]
    plaintext = _decrypt(ciphertext, iv, key)
    print("pt = ")
    print(plaintext)
    plaintext = plaintext.split(":")

    assert len(plaintext) == 2
    assert plaintext[0][:9] == "username="
    assert plaintext[1][:5] == "role="
    return (plaintext[0][9:], plaintext[1][5:])
    print colors.red + "[-] Invalid cookie!" + colors.reset

def read_flag():
    return open("flag.txt").read().strip()

def write_flag(flag):
    open("flag.txt","w").write(flag)

if __name__ == "__main__":
    print colors.blue + "Welcome to InCTF authenticated login service" + colors.reset
    print "[1] Register"
    print "[2] Login\n"
    try:
        choice = int(raw_input("[*] Enter your choice: "))
    except:
        print ""
        print colors.red + "[-] What are you trying?" + colors.reset
        sys.exit(0)
    if choice == 1:
        username = raw_input("[*] Enter username: ")
        print ""
        try:
            assert username != "admin"
        except:
            print colors.red + "[-] Username cannot be admin" + colors.reset
            sys.exit(0)
        print colors.green + "[+] Here, take your cookie: " +  colors.reset + register(username)
    elif choice == 2:
        print "[*] Enter your cookie (hex): "
        _cookie = raw_input()
        print ""
        user, role = login(_cookie)

        if user == "admin" and role == "ordinary":
            print colors.green + "[+] Are you really admin? Here, take your flag anyway!" + colors.reset
            print read_flag()
        elif user == "admin" and role == "admin":
            # print colors.green + "[+] Welcome real Admin!" + colors.reset
            print "[+] Welcome real Admin!"
            print "Choose whether you want to read[1] or write[2]:"
            adm_choice = int(raw_input())
            print ""
            if adm_choice == 1:
                print read_flag()
                sys.exit(0)
            elif adm_choice == 2:
                content = raw_input("Enter what you want to write to the flag file: ")
                write_flag(content)
                print "[#] Flag written successfully"
                sys.exit(0)
            else:
                print colors.red + "[-] Bad choice admin" + colors.reset
        elif role == "ordinary":
            print colors.green + "[+] Welcome user: " + user + colors.reset
            print colors.orange + "[-] You need to be admin to read/write to the flag file" + colors.orange
            print colors.orange + "Bye!" + colors.reset
        else:
            print colors.red + "[-] Looks like an invalid cookie" + colors.reset
    else:
        print colors.red + "[-] Invalid choice!" + colors.reset
        sys.exit(0)
