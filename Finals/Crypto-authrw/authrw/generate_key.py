## Use this program only once..
## Enter your team password [The exact password used for team registration]
## Using different password or changing the key file may bring down your service
import md5
passw = raw_input("Enter your Team Password: ")
if (passw == raw_input("Enter password again to confirm: ")): open("key.txt",'w').write(md5.new(passw).digest())
else: print "Password dosen't match, try again"
